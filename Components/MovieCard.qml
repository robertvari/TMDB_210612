import QtQuick 2.0
import QtQuick.Layouts

Rectangle {
    radius: 5
    border.color: Qt.rgba(0, 0, 0, 0.1)
    clip: true

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

        Item{
            id: title_container
            Layout.fillWidth: true
            implicitHeight: 70

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                Text{
                    text: "Black Widow"
                    font.pixelSize: 16
                    font.bold: true
                }

                Text{
                    text: "Jul 07, 2021"
                    color: "#888888"
                    font.pixelSize: 16
                }
            }


        }
    }


}
