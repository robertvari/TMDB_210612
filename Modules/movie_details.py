from PySide6.QtCore import QObject, Slot, Property, Signal, QUrl
import tmdbsimple as tmdb
from dotenv import load_dotenv
import os
from os.path import expanduser
from datetime import datetime, timedelta
from Utilities.downloader import download_image


USER_HOME = expanduser("~")
CACHE_FOLDER = os.path.join(USER_HOME, "TMDB_CACHE")

# get absolute path ("~to .env
ENV_PATH = os.path.dirname(__file__).replace("Modules", ".env")

# load .env to os env
load_dotenv(ENV_PATH)

# configure our API_KEY
tmdb.API_KEY = os.getenv("TMDB_API_KEY")


class MovieDetails(QObject):
    movie_loaded = Signal()

    def __init__(self):
        super(MovieDetails, self).__init__()
        self._title = ""
        self._tagline = ""
        self._overview = ""
        self._poster = QUrl()
        self._backdrop = QUrl()
        self._overview = ""
        self._release_date = ""
        self._runtime = ""
        self._vote_average = 0
        self._original_language = ""
        self._genres = ""

    @Slot(str)
    def set_movie(self, movie_id):
        movie = tmdb.Movies(movie_id)
        response = movie.info()

        if not response:
            return

        def get_formatted_date():
            datetime_obj = datetime.strptime(response.get("release_date"), "%Y-%m-%d")
            return datetime_obj.strftime("%Y %b. %d")

        def get_formatted_runtime():
            if not response.get("runtime"):
                return ""

            tdelta = timedelta(seconds=response.get("runtime"))
            d, h, m = str(tdelta).split(":")

            h = int(h)
            m = int(m)
            return f"{h}h {m}m"

        def get_formatted_genres():
            if not response.get("genres"):
                return ""

            return ", ".join([i["name"] for i in response.get("genres")])

        self._title = response.get("title")
        self._tagline = response.get("tagline")

        self._poster = self._get_poster_path(response.get("poster_path"))
        self._backdrop = self._get_backdrop_path(response.get("backdrop_path"))

        self._overview = response.get("overview")
        self._release_date = get_formatted_date()
        self._runtime = get_formatted_runtime()
        self._vote_average = int(response.get("vote_average") * 10)
        self._original_language = response.get("original_language")
        self._genres = get_formatted_genres()

        self.movie_loaded.emit()

    @staticmethod
    def _get_poster_path(url):
        local_path = download_image(url, CACHE_FOLDER)
        return QUrl().fromLocalFile(local_path)

    @staticmethod
    def _get_backdrop_path(url):
        local_path = download_image(url, CACHE_FOLDER, backdrop=True)
        return QUrl().fromLocalFile(local_path)

    def _get_title(self):
        return self._title

    def _get_overview(self):
        return self._overview

    def _get_tagline(self):
        return self._tagline

    def _get_date(self):
        return self._release_date

    def _get_language(self):
        return self._original_language

    def _get_genres(self):
        return self._genres

    def _get_runtime(self):
        return self._runtime

    def _get_vote_average(self):
        return self._vote_average

    def _get_poster(self):
        return self._poster

    def _get_backdrop(self):
        return self._backdrop

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