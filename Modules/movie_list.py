import tmdbsimple as tmdb
from dotenv import load_dotenv
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QObject, QRunnable, QThreadPool, Signal
import os
from os.path import expanduser
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

    def __init__(self):
        super(MovieList, self).__init__()

        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(1)

        self._items = []
        self._fetch()

    def _fetch(self):
        self._items.clear()

        self.movie_list_worker = MovieListWorker()
        self.movie_list_worker.signals.movie_data_downloaded.connect(self._insert_movie)
        self.pool.start(self.movie_list_worker)

    def _insert_movie(self, movie_data):
        print(movie_data)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(self._serializer(movie_data))
        self.endInsertRows()

    def _serializer(self, movie_data):
        return {
            "id": movie_data["id"],
            "poster": movie_data["poster_path"],
            "title": movie_data["title"],
            "date": movie_data["release_date"],
            "rating": movie_data["vote_average"] * 10
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


class WorkerSignals(QObject):
    download_process_started = Signal()
    download_process_stopped = Signal()
    download_process_finished = Signal()
    movie_data_downloaded = Signal(dict)


class MovieListWorker(QRunnable):
    def __init__(self):
        super(MovieListWorker, self).__init__()
        self.signals = WorkerSignals()

        self._movies = tmdb.Movies()
        self._is_working = False

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
        self.signals.download_process_started.emit()

        if not os.path.exists(CACHE_FOLDER):
            os.makedirs(CACHE_FOLDER)

        for movie_data in self._movies.popular(page=1)["results"]:
            if not self._check_movie(movie_data):
                continue

            local_poster_path = download_image(movie_data["poster_path"], CACHE_FOLDER)
            if not local_poster_path:
                continue

            movie_data["local_poster"] = local_poster_path
            self.signals.movie_data_downloaded.emit(movie_data)

        print("Download stopped.")
        self.signals.download_process_finished.emit()
        self._is_working = False

    def run(self):
        print("Download started...")
        self._is_working = True
        self._cache_data()


if __name__ == '__main__':
    MovieList()