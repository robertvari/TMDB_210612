import os, requests, shutil


def download_image(image_url, cache_folder, backdrop=False):
    poster_file_name = image_url[1:]
    poster_path = os.path.join(cache_folder, poster_file_name)

    if os.path.exists(poster_path):
        return poster_path

    poster_url = f"https://image.tmdb.org/t/p/w300{image_url}"

    if backdrop:
        poster_url = f"https://image.tmdb.org/t/p/w1920_and_h800_multi_faces{image_url}"

    response = requests.get(poster_url, stream=True)

    if response.status_code == 200:
        with open(poster_path, "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

        return poster_path


if __name__ == '__main__':
    download_image("/uHA5COgDzcxjpYSHHulrKVl6ByL.jpg", r"C:\Work\_PythonSuli\pycore-210612\workshop2\cache_folder")