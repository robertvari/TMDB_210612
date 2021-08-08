import QtQuick 2.0


Item {
    ListModel {
        id: movie_list

        ListElement {
            tmdb_id: "497698"
            title: "Black Widow"
            poster: "dq18nCTTLpy9PmtzZI6Y2yAgdw5.jpg"
            date: "2021-07-07"
            rating: 79
        }

        ListElement {
            tmdb_id: "451048"
            title: "Jungle Cruise"
            poster: "bwBmo4I3fqMsVvVtamyVJHXGnLF.jpg"
            date: "2021-07-28"
            rating: 80
        }

        ListElement {
            tmdb_id: "385128"
            title: "F9"
            poster: "xXHZeb1yhJvnSHPzZDqee0zfMb6.jpg"
            date: "2021-05-19"
            rating: 77
        }
    }


    GridView{
        id: movie_list_view
        anchors.fill: parent
        clip: true

        model: movie_list
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
