from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Welcome to MonarChain, Play to climb the Leaderboard in our MMORPG 3D!")

updater = Updater("7951802603:AAF8YPBMj9pPfRGa7H_JeyVJCK1WD0mrV0A")
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
