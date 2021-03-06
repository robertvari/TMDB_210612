import tmdbsimple as tmdb
from dotenv import load_dotenv
from PySide6.QtCore import QAbstractListModel, QSortFilterProxyModel, Qt, QModelIndex, QObject, QRunnable, \
    QThreadPool, Signal, QUrl, Slot, Property
import os, shutil, time
from os.path import expanduser
from datetime import datetime
from Utilities.downloader import download_image

USER_HOME = expanduser("~")
CACHE_FOLDER = os.path.join(USER_HOME, "TMDB_CACHE")

# get absolute path ("~to .env
ENV_PATH = os.path.dirname(__file__).replace("Modules", ".env")

# load .env to os env
load_dotenv(ENV_PATH)

# configure our API_KEY
tmdb.API_KEY = os.getenv("TMDB_API_KEY")


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole
    movie_list_changed = Signal()
    download_progress_changed = Signal()

    def __init__(self):
        super(MovieList, self).__init__()

        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(1)
        self.movie_list_worker = MovieListWorker()

        self._items = []
        self._fetch()

    def _fetch(self):
        self._reset()

        self.movie_list_worker = MovieListWorker()

        self.movie_list_worker.is_working = True
        self.download_progress_changed.emit()

        self.movie_list_worker.signals.download_process_stopped.connect(self._refresh_process_continues)
        self.movie_list_worker.signals.movie_data_downloaded.connect(self._insert_movie)
        self.movie_list_worker.signals.download_process_finished.connect(self._download_process_finished)
        self.pool.start(self.movie_list_worker)

    def _download_process_finished(self):
        self.download_progress_changed.emit()

    def _reset(self):
        self.beginResetModel()
        self._items.clear()
        self.movie_list_changed.emit()
        self.endResetModel()

    @Slot()
    def refresh_list(self):
        if self.movie_list_worker.is_working:
            self.movie_list_worker.stop()
        else:
            self._refresh_process_continues()

    def _refresh_process_continues(self):
        # delete cache folder
        if os.path.exists(CACHE_FOLDER):
            shutil.rmtree(CACHE_FOLDER, ignore_errors=True)

        self._reset()
        self._fetch()

    def _insert_movie(self, movie_data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(self._serializer(movie_data))
        self.movie_list_changed.emit()
        self.endInsertRows()

    def _serializer(self, movie_data):
        def get_formatted_date():
            datetime_obj = datetime.strptime(movie_data.get("release_date"), "%Y-%m-%d")
            return datetime_obj.strftime("%Y %b. %d")

        return {
            "id": movie_data["id"],
            "poster": QUrl().fromLocalFile(movie_data["local_poster"]),
            "title": movie_data["title"],
            "date": get_formatted_date(),
            "sort_date": datetime.strptime(movie_data.get("release_date"), "%Y-%m-%d"),
            "rating": int(movie_data["vote_average"] * 10),
            "overview": movie_data["overview"]
        }

    def rowCount(self, parent=QModelIndex):
        return len(self._items)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == MovieList.DataRole:
            return self._items[row]

    def roleNames(self):
        return {
            MovieList.DataRole: b'movie_item'
        }

    def _get_is_downloading(self):
        print(f"_get_is_downloading {self.movie_list_worker.is_working}")
        return self.movie_list_worker.is_working

    def _get_movie_count(self):
        return len(self._items)

    is_downloading = Property(bool, _get_is_downloading, notify=download_progress_changed)
    movie_count = Property(int, _get_movie_count, notify=movie_list_changed)


class MovieListProxy(QSortFilterProxyModel):
    sorting_changed = Signal()

    def __init__(self):
        super(MovieListProxy, self).__init__()
        self.sort(0, Qt.AscendingOrder)

        self._filter = ""
        self._sort_mode = "title"

        self.sorting_changed.emit()

    @Slot(str)
    def set_filter(self, movie_name):
        self._filter = movie_name
        self.invalidateFilter()

    @Slot(str)
    def set_current_sorting(self, sort_mode):
        # check if sort mode is the same as previously
        if sort_mode == self._sort_mode:
            # check current sortOrder()
            if self.sortOrder() == Qt.AscendingOrder:
                self.sort(0, Qt.DescendingOrder)
            else:
                self.sort(0, Qt.AscendingOrder)
        else:
            self.sort(0, Qt.AscendingOrder)

        self._sort_mode = sort_mode
        self.sorting_changed.emit()
        self.invalidate()

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        movie_data = self.sourceModel()._items[source_row]

        return self._filter.lower() in movie_data["title"].lower()

    def lessThan(self, source_left, source_right) -> bool:
        left_movie = self.sourceModel().data(source_left, Qt.UserRole)
        right_movie = self.sourceModel().data(source_right, Qt.UserRole)

        if self._sort_mode == "date":
            return left_movie["sort_date"] < right_movie["sort_date"]

        return left_movie[self._sort_mode] < right_movie[self._sort_mode]

    def _get_current_sorting(self):
        return self._sort_mode

    def _get_sort_direction(self):
        if self.sortOrder() == Qt.AscendingOrder:
            return 0
        return 180

    current_sorting = Property(str, _get_current_sorting, notify=sorting_changed)
    sort_direction = Property(int, _get_sort_direction, notify=sorting_changed)


class WorkerSignals(QObject):
    download_process_started = Signal()
    download_process_stopped = Signal()
    download_process_finished = Signal()
    movie_data_downloaded = Signal(dict)

    def __init__(self):
        super(WorkerSignals, self).__init__()


class MovieListWorker(QRunnable):
    def __init__(self):
        super(MovieListWorker, self).__init__()
        self.signals = WorkerSignals()

        self._movies = tmdb.Movies()
        self.is_working = False

    def _check_movie(self, movie_data):
        if not movie_data.get("poster_path"):
            return False

        if not movie_data.get("vote_average"):
            return False

        if not movie_data.get("backdrop_path"):
            return False

        if not movie_data.get("release_date"):
            return False

        return True

    def _cache_data(self):
        if not self.is_working:
            self.signals.download_process_stopped.emit()
            return

        self.signals.download_process_started.emit()

        if not os.path.exists(CACHE_FOLDER):
            os.makedirs(CACHE_FOLDER)

        for movie_data in self._movies.popular(page=1)["results"]:
            if not self.is_working:
                print("Download process stopped!")
                self.signals.download_process_stopped.emit()
                break

            if not self._check_movie(movie_data):
                continue

            local_poster_path = download_image(movie_data["poster_path"], CACHE_FOLDER)
            if not local_poster_path:
                continue

            movie_data["local_poster"] = local_poster_path

            # time.sleep(0.2)
            self.signals.movie_data_downloaded.emit(movie_data)

        print("Download finished.")
        self.is_working = False
        self.signals.download_process_finished.emit()

    def stop(self):
        self.is_working = False

    def run(self):
        print("Download started...")
        self.is_working = True
        self._cache_data()


if __name__ == '__main__':
    MovieList()