import tmdbsimple as tmdb
from dotenv import load_dotenv
from PySide6.QtCore import QAbstractListModel
import os

# get absolute path to .env
ENV_PATH = os.path.dirname(__file__).replace("Modules", ".env")

# load .env to os env
load_dotenv(ENV_PATH)

# configure our API_KEY
tmdb.API_KEY = os.getenv("TMDB_API_KEY")


class MovieList(QAbstractListModel):
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


if __name__ == '__main__':
    MovieList()