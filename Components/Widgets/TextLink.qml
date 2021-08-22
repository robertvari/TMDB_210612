import QtQuick 2.0

Text {
    id: root
    property string link_text: "Link Text"
    property color defaultColor: "white"
    property color hoverColor: "#c9c9c9"

    color: defaultColor
    font.pixelSize: 20
    font.bold: true

    text: link_text

    signal clicked

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        hoverEnabled: true

        onEntered: parent.color = hoverColor
        onExited: parent.color = defaultColor

        onClicked: root.clicked()
    }
}
