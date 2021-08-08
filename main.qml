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
        anchors.fill: parent

        states: [
            State {
                name: "details"
                PropertyChanges {
                    target: movie_list_layout
                    visible: false
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
            Layout.fillWidth: true
            implicitHeight: 64
        }

        // Search and Movie list layout
        RowLayout{
            id: movie_list_layout
            Layout.fillHeight: true
            Layout.fillWidth: true

            // search SearchBar
            SearchBar{
                id: search_bar
                Layout.fillHeight: true
                implicitWidth: 200
            }

            // movie List
            MovieList{
                id: movie_list
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }
    }
}
