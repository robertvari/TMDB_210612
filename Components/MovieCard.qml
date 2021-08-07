import QtQuick 2.0
import QtQuick.Layouts

Rectangle {
    radius: 5
    border.color: Qt.rgba(0, 0, 0, 0.1)

    ColumnLayout{
        anchors.fill: parent
        spacing: 0

        Rectangle{
            id: poster_rect
            color: "black"
            Layout.fillWidth: true
            Layout.fillHeight: true

            Text{
                text: "Poster..."
                color: "white"
                anchors.centerIn: parent
            }
        }

        Rectangle{
            id: title_rect
            color: "lightgray"
            Layout.fillWidth: true
            implicitHeight: 70

            Text{
                text: "Title/Release date"
                anchors.centerIn: parent
            }
        }
    }


}
