import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import "Components"


Window {
    width: 1280
    height: 720
    visible: true
    title: qsTr("TMDB")

    ColumnLayout{
        id: main_layout
        anchors.fill: parent
        state: "list"
        spacing: 0

        states: [
            State {
                name: "details"
                PropertyChanges {
                    target: movie_details
                    visible: true
                }
            },
            State {
                name: "list"
                PropertyChanges {
                    target: movie_list_layout
                    visible: true
                }
            }
        ]

        // navbar
        Navbar{
            id: navbar
            Layout.fillWidth: true
            implicitHeight: 64
            state: "grid_view"

            states: [
                State {
                    name: "list_view"
                    PropertyChanges {
                        target: movie_list_view
                        visible: true
                    }
                },

                State {
                    name: "grid_view"
                    PropertyChanges {
                        target: movie_grid_view
                        visible: true
                    }
                }
            ]
        }

        // Download Progressbar
        Rectangle{
            Layout.fillWidth: true
            implicitHeight: 10
            color: "#05B4E3"
        }

        // Search and Movie list layout
        RowLayout{
            id: movie_list_layout
            Layout.fillHeight: true
            Layout.fillWidth: true
            visible: false

            // search SearchBar
            SearchBar{
                id: search_bar
                Layout.fillHeight: true
                Layout.topMargin: 5
                implicitWidth: 200
            }

            // movie List
            MovieListGrid{
                id: movie_grid_view
                Layout.fillHeight: true
                Layout.fillWidth: true
                visible: false
            }

            MovieList{
                id: movie_list_view
                Layout.fillHeight: true
                Layout.fillWidth: true
                visible: false
            }
        }

        MovieDetails{
            id: movie_details
            visible: false
            Layout.fillHeight: true
            Layout.fillWidth: true
        }
    }
}
