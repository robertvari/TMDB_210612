from PySide6.QtCore import QObject, Slot


class MovieDetails(QObject):
    @Slot(str)
    def set_movie(self, movie_id):
        print(f"Get details for movie: {movie_id}")