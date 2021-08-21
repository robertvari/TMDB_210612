import QtQuick
import QtQuick.Layouts
import "Widgets"

Rectangle {
    color: "lightblue"

    ColumnLayout{
        Text{
            text: MovieDetailsModel.title
            font.pixelSize: 30
        }

        Text{
            text: MovieDetailsModel.overview
        }

        Text{
            text: MovieDetailsModel.tagline
        }

        Text{
            text: MovieDetailsModel.release_date
        }

        Text{
            text: MovieDetailsModel.language
        }

        Text{
            text: MovieDetailsModel.genres
        }

        Text{
            text: MovieDetailsModel.runtime
        }

        PopularityProgress{
            percentage: MovieDetailsModel.vote_average
        }
    }
}
