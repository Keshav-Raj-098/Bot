from typing import Final
from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,Application, filters,CallbackQueryHandler

TOKEN:Final = '7607562374:AAEJuriLylwqM0_ll4jDsa7oKggVN5Ny2t0'
BOT_USERNAME:Final = '@hoottell_bot'
API_URL:Final = f'https://api.telegram.org/bot{TOKEN}/'



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [InlineKeyboardButton("Let's Begin", callback_data='begin')]
        
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text( f'Hello {update.effective_user.first_name}, I am here to help you with finding and booking the best hotels for your stay.', reply_markup=reply_markup)

async def begin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Search Hotels", callback_data='search')],
        [InlineKeyboardButton("Book Hotel", callback_data='book')],
        [InlineKeyboardButton("Cancel Booking", callback_data='cancel')]
    ])
    
    await update.message.reply_text(
        'What would you like to do?',
        reply_markup=reply_markup
    )

# callback handler for button presses
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # acknowledge the callback
    await query.edit_message_text(text=f"You selected: {query.data}")
    
async def search_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # acknowledge the callback
    await query.edit_message_text(text=f"You selected: {query.data}")
    
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'I can help you with the following commands:\n'
        '/start - Start the bot\n'
        '/help - Show this help message\n'
        '/search - Search for hotels\n'
        '/book - Book a hotel\n'
        '/cancel - Cancel a booking\n'
    )
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'This is a custom command. You can add your own functionality here.'
    )
    
#handle responses

def handle_response(text:str)-> str:
    if 'hello' in text.lower():
        return 'Hello! How can I help you today?'
    elif 'book' in text.lower():
        return 'Sure! I can help you with booking a hotel. Please provide the details.'
    elif 'cancel' in text.lower():
        return 'I can help you with canceling a booking. Please provide the details.'
    else:
        return 'I am not sure how to respond to that. Please try again.'
    
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messgae_type : str = update.message.chat.type
    text : str = update.message.text
    
    print(f"User ({update.message.chat.id}) sent a message in {messgae_type} chat: {text}")
    
    
    if messgae_type == 'group':
        if BOT_USERNAME in text:
            new_text :str = text.replace(BOT_USERNAME, '').strip()
            response :str = handle_response(new_text)
        else:
            return
        
    else:
        response : str = handle_response(text)
        
    print(f"Response to user ({update.message.chat.id}): {response}")
    await update.message.reply_text(response)
    

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    await update.message.reply_text('An error occurred. Please try again later.')
    
    
if __name__ == '__main__':
    print('Bot is running...')
    app = ApplicationBuilder().token(TOKEN).build()
    
    
    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    app.add_handler(CallbackQueryHandler(button),handler='button')
    app.add_handler(CallbackQueryHandler(search_button),handler='search')
    
    
    
    #message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    
    #error handler
    app.add_error_handler(error_handler)
    
    
    print('Polling...')
    app.run_polling(poll_interval=5)
