import QtQuick
import QtQuick.Layouts

import "Widgets"
Item {
    ColumnLayout{
        anchors.fill: parent

        Rectangle{
            Layout.fillWidth: true
            implicitHeight: 570
            color: "black"

            Image{
                source: MovieDetailsModel.backdrop
                opacity: 0.3

                width: parent.width
                height: parent.height
                fillMode: Image.PreserveAspectCrop
            }


            RowLayout{
                anchors.fill: parent
                anchors.leftMargin: 20

                Item{
                    id: poster_container
                    Layout.fillHeight: true
                    Layout.minimumWidth: 400

                    Image{
                        source: MovieDetailsModel.poster
                        anchors.fill: parent
                        fillMode: Image.PreserveAspectFit
                    }
                }

                ColumnLayout{
                    id: movie_title_container
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.rightMargin: 20

                    Text{
                        text: MovieDetailsModel.title
                        color: "white"
                        font.pixelSize: 40
                        font.bold: true
                    }

                    Text{
                        text: MovieDetailsModel.release_date + " | " + MovieDetailsModel.genres + " | " + MovieDetailsModel.runtime
                        color: "white"
                        font.pixelSize: 16
                    }

                    PopularityProgress{
                        percentage: MovieDetailsModel.vote_average
                    }

                    Text{
                        text: MovieDetailsModel.tagline
                        color: "#999999"
                        font.pixelSize: 16
                        font.italic: true
                    }

                    Text{
                        text: "Overview"
                        color: "white"
                        font.pixelSize: 20
                        font.bold: true
                    }

                    Text{
                        text: MovieDetailsModel.overview
                        color: "white"
                        font.pixelSize: 16
                        Layout.fillWidth: true
                        wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                    }
                }
            }
        }


        Item{Layout.fillHeight: true}
    }
}
