import QtQuick 2.0

Text {
    property string link_text: "Link Text"

    color: "white"
    font.pixelSize: 20
    font.bold: true

    text: link_text

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        hoverEnabled: true

        onEntered: parent.color = "#c9c9c9"
        onExited: parent.color = "white"
    }
}
