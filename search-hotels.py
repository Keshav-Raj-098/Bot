from typing import List, Dict, Any
from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,Application, filters,CallbackQueryHandler

from dotenv import load_dotenv
import os

load_dotenv()  # load from .env

AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")



async def search_hotels(update:Update, context:ContextTypes.DEFAULT_TYPE):
    """
    Handles the /search command to initiate hotel search.
    """
    
    await update.message.reply_text(
        "Please provide the city you want to search for hotels in.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Cancel", callback_data='cancel_search')]
            [InlineKeyboardButton("Back to Main Menu", callback_data='main_menu')]
        ])
    )
    