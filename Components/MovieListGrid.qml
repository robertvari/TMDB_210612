import QtQuick 2.0


Item {
    GridView{
        id: movie_list_view
        anchors.fill: parent
        clip: true

        model: MovieListModel
        cellWidth: 210
        cellHeight: 383

        delegate: MovieCard{
            width: movie_list_view.cellWidth - 10
            height: movie_list_view.cellHeight - 10

            movie_title: movie_item.title
            movie_date: movie_item.date
            movie_rating: movie_item.rating
            movie_id: movie_item.id
            movie_poster: movie_item.poster
        }
    }
}
