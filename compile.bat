pyinstaller --add-data "Components;Components" --add-data "Images;Images" --add-data ".env;." --add-data "main.qml;." --noconsole --name "TMDB" .\main.py