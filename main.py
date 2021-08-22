# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from Modules.resource_loader import Resources
from Modules.movie_list import MovieList, MovieListProxy
from Modules.movie_details import MovieDetails


class TMDB:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()

        self.resource_loader = Resources()
        self.context.setContextProperty("Resources", self.resource_loader)

        self.movie_list = MovieList()
        self.context.setContextProperty("MovieListModel", self.movie_list)

        self.movie_list_proxy = MovieListProxy()
        self.movie_list_proxy.setSourceModel(self.movie_list)
        self.context.setContextProperty("MovieListModel_Proxy", self.movie_list_proxy)

        self.movie_details = MovieDetails()
        self.context.setContextProperty("MovieDetailsModel", self.movie_details)

        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)

        self.app.lastWindowClosed.connect(self._close_app)
        sys.exit(self.app.exec())

    def _close_app(self):
        self.movie_list.movie_list_worker.stop()


if __name__ == "__main__":
    TMDB()
