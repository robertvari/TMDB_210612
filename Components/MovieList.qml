import QtQuick 2.0


Rectangle {



    GridView{
        id: grid_view
        anchors.fill: parent
        clip: true

        model: 100
        cellWidth: 210
        cellHeight: 383

        delegate: MovieCard{
            width: grid_view.cellWidth - 10
            height: grid_view.cellHeight - 10
        }
    }
}
