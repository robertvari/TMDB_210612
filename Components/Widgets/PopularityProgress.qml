import QtQuick 2.0

Rectangle {
    id: root

    implicitHeight: 50
    implicitWidth: 50
    color: "#141414"
    radius: width

    property int percentage: 50

    onParentChanged: canvas.requestPaint()

    Canvas{
        id: canvas
        width: parent.width
        height: parent.height

        onPaint: {
            var ctx = getContext("2d");
            ctx.reset();

            var radiant = root.percentage * 0.062831853071796

            ctx.beginPath();
            ctx.fillStyle = "lightgreen";

            var centerX = width / 2;
            var centerY = height / 2;
            var radius = width / 2;

            ctx.arc(centerX, centerY, radius, 0, radiant, false);

            ctx.lineTo(centerX, centerY);
            ctx.fill();
        }

        rotation: -90
    }

    Rectangle{
        color: root.color
        width: root.width -10
        height: width
        anchors.centerIn: parent
        radius: width

        Item{
            anchors.centerIn: parent
            width: childrenRect.width
            height: childrenRect.height

            Text{
                id: popularity_text
                text: root.percentage
                color: "white"
                font.bold: true
                font.pixelSize: 22
            }

            Text{
                text: "%"
                color: "white"
                font.bold: true
                font.pixelSize: 10
                anchors.left: popularity_text.right
                anchors.top: popularity_text.top
            }
        }
    }
}
