from PySide6.QtCore import QObject, Slot, Property
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
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        if not response:
            return

    title = Property(str, _get_title, notify=movie_loaded)
    overview = Property(str, _get_overview, notify=movie_loaded)
    tagline = Property(str, _get_tagline, notify=movie_loaded)
    release_date = Property(str, _get_date, notify=movie_loaded)
    poster = Property(QUrl, _get_poster, notify=movie_loaded)
    backdrop = Property(QUrl, _get_backdrop, notify=movie_loaded)
    language = Property(str, _get_language, notify=movie_loaded)
    genres = Property(str, _get_genres, notify=movie_loaded)
    runtime = Property(str, _get_runtime, notify=movie_loaded)
    vote_average = Property(int, _get_vote_average, notify=movie_loaded)