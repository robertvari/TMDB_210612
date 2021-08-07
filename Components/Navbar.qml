import QtQuick 2.0
import QtQuick.Layouts


Rectangle {
    color: "#032541"

    RowLayout{
        anchors.fill: parent
        anchors.margins: 10

        // Logo
        Image{
            source: Resources.get_image("logo.svg")
            Layout.rightMargin: 20
        }

        // nav menu
        Repeater{
            model: ["Movies", "TV Shows", "People", "More"]

            Text{
                color: "white"
                font.bold: true
                text: modelData
                font.pixelSize: 20
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
