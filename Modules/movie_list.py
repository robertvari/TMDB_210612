import tmdbsimple as tmdb
from dotenv import load_dotenv
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QObject, QRunnable, QThreadPool, Signal
import os

# get absolute path to .env
ENV_PATH = os.path.dirname(__file__).replace("Modules", ".env")

# load .env to os env
load_dotenv(ENV_PATH)

# configure our API_KEY
tmdb.API_KEY = os.getenv("TMDB_API_KEY")


class MovieList(QAbstractListModel):
    DataRole = Qt.UserRole

    def __init__(self):
        super(MovieList, self).__init__()
        self._movies = tmdb.Movies()

        self._items = []
        self._fetch()

    def _fetch(self):
        self._items.clear()

        for movie_data in self._movies.popular()["results"]:
            self._insert_movie(self._serializer(movie_data))

    def _insert_movie(self, movie_data):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(movie_data)
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


if __name__ == '__main__':
    MovieList()