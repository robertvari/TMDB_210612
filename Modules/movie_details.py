from PySide6.QtCore import QObject, Slot
import tmdbsimple as tmdb
from dotenv import load_dotenv
import os
from os.path import expanduser

USER_HOME = expanduser("~")
CACHE_FOLDER = os.path.join(USER_HOME, "TMDB_CACHE")

# get absolute path ("~to .env
ENV_PATH = os.path.dirname(__file__).replace("Modules", ".env")

# load .env to os env
load_dotenv(ENV_PATH)

# configure our API_KEY
tmdb.API_KEY = os.getenv("TMDB_API_KEY")


class MovieDetails(QObject):
    @Slot(str)
    def set_movie(self, movie_id):
        print(f"Get details for movie: {movie_id}")