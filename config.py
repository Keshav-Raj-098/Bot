
from dotenv import load_dotenv
import os

load_dotenv()  # load from .env


BOT_TOKEN = os.getenv("BOT_TOKEN")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

OMDB_DATA_URL="http://www.omdbapi.com/"
TMDB_URL="https://api.themoviedb.org/3"

TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")


Top_Movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1" 
In_Theatre = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1&region=IN"

Top_rated = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&region=IN"

upcoming = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

img_api = "https://image.tmdb.org/t/p/w500/"

