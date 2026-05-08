from telegram.ext import Updater, CommandHandler

TOKEN = "8775152874:AAHZrXjTMu-NHb-NsS_AYCugZw3ArbnDiQ4"

def start(update, context):
    update.message.reply_text("✅ Bot is working!")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()