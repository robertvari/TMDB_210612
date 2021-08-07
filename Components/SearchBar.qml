import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls
import "Widgets"

Rectangle {
    ColumnLayout{
        anchors.fill: parent
        anchors.leftMargin: 10

        TextField{
            placeholderText: "Search..."
            Layout.fillWidth: true
            font.pixelSize: 16
        }

        TextLink{
            link_text: "Title"
            color: "black"
        }

        TextLink{
            link_text: "Release date"
            color: "black"
        }

        TextLink{
            link_text: "Rating"
            color: "black"
        }

        Item{
            Layout.fillHeight: true
        }
    }
}
