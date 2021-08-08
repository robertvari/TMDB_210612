import tmdbsimple as tmdb
from dotenv import load_dotenv
import os

# get absolute path to .env
ENV_PATH = os.path.dirname(__file__).replace("Modules", ".env")

# load .env to os env
load_dotenv(ENV_PATH)

# configure our API_KEY
tmdb.API_KEY = os.getenv("TMDB_API_KEY")

movies = tmdb.Movies()
result = movies.popular()

for i in result["results"]:
    print(i)