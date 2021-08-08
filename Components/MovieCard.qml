import QtQuick 2.0
import QtQuick.Layouts
import "Widgets"

Rectangle {
    id: root

    property string movie_title: "Black Widow"
    property string movie_date: ""
    property int movie_rating: 0
    property string movie_id: ""

    radius: 5
    border.color: Qt.rgba(0, 0, 0, 0.1)
    clip: true

    ColumnLayout{
        anchors.fill: parent
        spacing: 0

        Item{
            id: poster_rect
            Layout.fillWidth: true
            Layout.fillHeight: true

            Image{
                source: Resources.get_image("poster.jpg")
                sourceSize: Qt.size(poster_rect.width - 10, poster_rect.height)
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 5
                anchors.top: parent.top
            }

            PopularityProgress{
                x: 5
                anchors.bottom: parent.bottom
                percentage: root.movie_rating
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
                    text: root.movie_title
                    font.pixelSize: 16
                    font.bold: true
                }

                Text{
                    text: root.movie_date
                    color: "#888888"
                    font.pixelSize: 16
                }
            }


        }
    }

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        onClicked: main_layout.state = "details"
    }
}
