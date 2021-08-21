import QtQuick 2.0

Item {
    id: root

    property string icon
    property int size: 30

    implicitWidth: root.size
    implicitHeight: root.size

    signal clicked

    Image{
        source: root.icon
         sourceSize: Qt.size(root.size, root.size)
    }
}
