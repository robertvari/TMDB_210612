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
            show_icon: MovieListModel_Proxy.current_sorting === "title"

            onClicked: MovieListModel_Proxy.set_current_sorting("title")
        }

        TextLink{
            link_text: "Release date"
            defaultColor: "black"
            font.pixelSize: 16
            show_icon: MovieListModel_Proxy.current_sorting === "date"

            onClicked: MovieListModel_Proxy.set_current_sorting("date")
        }

        TextLink{
            link_text: "Rating"
            defaultColor: "black"
            font.pixelSize: 16
            show_icon: MovieListModel_Proxy.current_sorting === "rating"

            onClicked: MovieListModel_Proxy.set_current_sorting("rating")
        }

        Item{
            Layout.fillHeight: true
        }
    }
}
