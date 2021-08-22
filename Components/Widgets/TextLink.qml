import QtQuick 2.0

Text {
    id: root
    property string link_text: "Link Text"
    property color defaultColor: "white"
    property color hoverColor: "#c9c9c9"

    property bool show_icon: false
    property int icon_rotation: 0

    color: defaultColor
    font.pixelSize: 20
    font.bold: true

    text: link_text

    signal clicked

    Image{
        source: Resources.get_image("arrow.svg")
        visible: root.show_icon
        sourceSize: Qt.size(20, 20)

        anchors.left: root.right
        anchors.verticalCenter: root.verticalAlignment
        anchors.leftMargin: 10

        rotation: MovieListModel_Proxy.sort_direction
    }

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        hoverEnabled: true

        onEntered: parent.color = hoverColor
        onExited: parent.color = defaultColor

        onClicked: root.clicked()
    }
}
