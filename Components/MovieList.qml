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

            movie_title: title
            movie_date: date
            movie_rating: rating
            movie_id: tmdb_id
        }
    }
}
