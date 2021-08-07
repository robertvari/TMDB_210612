import QtQuick 2.0

Rectangle {
    color: "#032541"

    Image{
        source: Resources.get_image("logo.svg")
        anchors.left: parent.left
        anchors.margins: 10
        anchors.verticalCenter: parent.verticalCenter
    }
}
