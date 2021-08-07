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

        // navbar
        Navbar{
            Layout.fillWidth: true
            implicitHeight: 64
        }

        // Search and Movie list layout
        RowLayout{
            Layout.fillHeight: true
            Layout.fillWidth: true

            // search SearchBar
            SearchBar{
                Layout.fillHeight: true
                implicitWidth: 200
            }

            // movie List
            MovieList{
                Layout.fillHeight: true
                Layout.fillWidth: true
            }
        }
    }
}
