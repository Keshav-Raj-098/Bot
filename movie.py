from typing import List, Dict, Any
from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,Application, filters,CallbackQueryHandler

import requests

from config import BOT_TOKEN,TMDB_ACCESS_TOKEN,TMDB_URL


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"
}
    
    
Genre = {
    "Horror": "genre_horror",
    "Action": "genre_action",
    "Comedy": "genre_comedy",
    "Drama": "genre_drama",
    "Romance": "genre_romance",
    "Sci-Fi": "genre_sci-fi",
    "Thriller": "genre_thriller",
    "Fantasy": "genre_fantasy",
    "Mystery": "genre_mystery",
    "Animation": "genre_animation",
    "Documentary": "genre_documentary",
    "Historical": "genre_historical",
    "Adventure": "genre_adventure",
    "Crime": "genre_crime",
}

genre_items = list(Genre.items())



async def choose_genre(update:Update, context:ContextTypes.DEFAULT_TYPE):
    """
    Handles the /search command to initiate hotel search.
    """
    
    genre_buttons = [
    [InlineKeyboardButton(text, callback_data=data)
     for text, data in genre_items[i:i+3]]
    for i in range(0, len(genre_items), 3)
]

    
    genre_buttons.append([
    InlineKeyboardButton("Cancel", callback_data='cancel_search'),
    InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')
    ])

    
    await update.callback_query.message.reply_text(
        "Please Choose the Genre you",
        reply_markup=InlineKeyboardMarkup(genre_buttons)
    )
    



async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE,genre:str):
    """
    Handles the callback query for genre selection.
    """
    
    
    
    
    if not genre:
        update.message.reply_text("Please provide a genre to search")
        return
    
    
    query = update.callback_query
    
    if genre == 'cancel_search':
        await query.message.reply_text("Search cancelled.")
        return
    
    if genre == 'main_menu':
        # await query.data = 'begin'
        await query.message.reply_text("Returning to main menu.")
        return
    
    resposne = requests.get(f"https://api.themoviedb.org/3/movie/changes?page=1",headers=headers) 
    
    
    print(resposne.text)
    
    





