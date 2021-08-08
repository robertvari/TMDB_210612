import QtQuick 2.0
import QtQuick.Layouts
import "Widgets"


Rectangle {
    color: "#032541"

    RowLayout{
        anchors.fill: parent
        anchors.margins: 10

        // Logo
        Image{
            source: Resources.get_image("logo.svg")
            Layout.rightMargin: 20

            MouseArea{
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onClicked: main_layout.state = "list"
            }
        }

        // nav menu
        Repeater{
            model: ["Movies", "TV Shows", "People", "More"]

            TextLink{
                link_text: modelData
                Layout.rightMargin: 10
            }
        }

        Item{
            Layout.fillWidth: true
        }

        // refresh button
        Image{
            source: Resources.get_image("refresh.svg")
            sourceSize: Qt.size(30, 30)
        }
    }
}
