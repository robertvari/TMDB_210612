import QtQuick 2.0

Item{
    id: root
    implicitHeight: 10
    visible: MovieListModel.is_downloading

    property int value: MovieListModel.movie_count
    property int maxValue: 20

    Rectangle{
        height: root.height
        width: (root.width / root.maxValue) * root.value
        color: "#05B4E3"
    }
}
