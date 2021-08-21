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


            RowLayout{
                anchors.fill: parent

                Item{
                    Layout.fillHeight: true
                    Layout.minimumWidth: 500

                    Image{
                        source: MovieDetailsModel.poster
                        anchors.fill: parent
                        fillMode: Image.PreserveAspectFit
                    }
                }
            }
        }


        Item{Layout.fillHeight: true}
    }
}
