from config import BOT_TOKEN,TMDB_ACCESS_TOKEN,TMDB_URL


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"
}
    