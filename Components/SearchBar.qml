import QtQuick
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
            leftPadding: 10

            onTextChanged: MovieListModel_Proxy.set_filter(text)
        }

        TextLink{
            link_text: "Title"
            defaultColor: "black"
            font.pixelSize: 16
        }

        TextLink{
            link_text: "Release date"
            defaultColor: "black"
            font.pixelSize: 16
        }

        TextLink{
            link_text: "Rating"
            defaultColor: "black"
            font.pixelSize: 16
        }

        Item{
            Layout.fillHeight: true
        }
    }
}
