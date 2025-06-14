from typing import List, Dict, Any
from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,Application, filters,CallbackQueryHandler

import requests

from config import BOT_TOKEN,TMDB_ACCESS_TOKEN,TMDB_URL
from tmdb_header import headers

import requests

def make_request__to_tmdb (url,headers):
    for i in range(5):
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response
                else:
                    print(f"Attempt {i+1} failed: Status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Attempt {i+1} exception: {e}")



async def get_with_category(update: Update, context: ContextTypes.DEFAULT_TYPE, user_context,key:str):
    """Returns the movies currently playing in Indian theatres."""

    try:
        page = user_context.page_data.get("pageNo", 1)

        url = f"{TMDB_URL}/movie/{key}?language=en-US&page={page}&region=IN"

        # Retry up to 5 times
        response = make_request__to_tmdb(url,headers)
        
        if not response or response.status_code != 200:
            await update.callback_query.message.reply_text("Sorry, we couldn't fetch movie data. Please try again later.")
            return

        movies_list = response.json().get("results", [])

        if not movies_list:
            await update.callback_query.message.reply_text("No movies currently found.")
            return

        # Send top 5 movies only
        for movie in movies_list[:5]:
            poster_path = movie.get("poster_path")
            if not poster_path:
                continue  # skip if no image

            overview = movie.get("overview", "No description available.")
            if len(overview) > 800:
                overview = overview[:800] + "..."

            caption = f"""🎬 <b>{movie.get('title', 'No Title')}</b>
🗓️ Released: <i>{movie.get('release_date', 'N/A')}</i>
⭐ Rating: <b>{movie.get('vote_average', 'N/A')}</b>/10
🔥 Popularity: {movie.get('popularity', 'N/A')}
📝 {overview}"""

            await update.callback_query.message.reply_photo(
                photo=f"https://image.tmdb.org/t/p/w185{poster_path}",
                caption=caption,
                parse_mode='HTML'
            )
        
        await update.callback_query.message.reply_text(
            text=f"""To Know more about any of these reply that to me with the message more
            
            
            Choose an option:""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Get More", callback_data="get_more")],
                [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
            ])
)


    except Exception as e:
        print(f"Error in current_movies: {e}")
        await update.message.reply_text("Unexpected error occurred. Please try again.")
