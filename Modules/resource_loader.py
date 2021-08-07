import os
from PySide6.QtCore import QObject, Slot, QUrl


IMAGES_DIR = os.path.dirname(__file__).replace("Modules", "Images")


class Resources(QObject):
    @Slot(str, result=QUrl)
    def get_image(self, image_name):
        image_path = os.path.join(IMAGES_DIR, image_name)
        return QUrl().fromLocalFile(image_path)