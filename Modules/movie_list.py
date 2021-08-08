import tmdbsimple as tmdb
from dotenv import load_dotenv
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
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
        popular_movies = self._movies.popular()

        for i in popular_movies["results"]:
            self._items.append(i)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == MovieList.DataRole:
            return self._items[row]

    def roleNames(self):
        return {
            MovieList.DataRole: b'movie_item'
        }

    def rowCount(self, parent=QModelIndex):
        return len(self._items)


if __name__ == '__main__':
    MovieList()