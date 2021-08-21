import QtQuick 2.0

Rectangle {
    color: "lightblue"

    Text{
        text: MovieDetailsModel.title
        anchors.centerIn: parent
        font.pixelSize: 30
    }
}
