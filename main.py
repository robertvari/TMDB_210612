# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from Modules.resource_loader import Resources


class TMDB:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()

        self.resource_loader = Resources()
        self.context.setContextProperty("Resources", self.resource_loader)

        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec())


if __name__ == "__main__":
    TMDB()
