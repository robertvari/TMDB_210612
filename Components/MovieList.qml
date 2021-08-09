import QtQuick 2.0
import QtQuick.Layouts
import "Widgets"

Item {
    ListView{
        id: list_view
        anchors.fill: parent
        model: MovieListModel
        spacing: 5
        clip: true

        delegate: Rectangle{
            id: delegate
            width: list_view.width
            height: 150
            border.color: Qt.rgba(0, 0, 0, 0.2)
            radius: 5

            RowLayout{
                anchors.fill: parent

                // poster here
                Image{
                    sourceSize: Qt.size(delegate.height -5, delegate.height -5)
                    source: movie_item.poster
                }

                Text{
                    text: movie_item.title
                    font.bold: true
                    font.pixelSize: 24
                }

                Text{
                    text: "( " + movie_item.date + " )"
                }



                Text{
                    text: movie_item.overview
                    Layout.fillWidth: true
                    wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                }

                PopularityProgress{
                    percentage: movie_item.rating
                }
            }


        }
    }
}
