import telegram.ext
from telegram.ext import *


Token = "5756838887:AAHoqs4A6ctHVcVxxllqHl-7ECbuJ6g1g2E"

updater = telegram.ext.Updater("5756838887:AAHoqs4A6ctHVcVxxllqHl-7ECbuJ6g1g2E", use_context=True) 
dispatcher = updater.dispatcher



def Start(update,context):
    update.message.reply_text("Hello! welcome to crioalertsBot click '/Sports' to get information")

def Sports(update,context):
    update.message.reply_text("click on these you get links to view  1./Livescore 2./Upcoming 3./Results")

def Livescore(update,context):
    update.message.reply_text("Tutorial link:  https://www.espncricinfo.com/live-cricket-score")

def Upcoming(update,context):
    update.message.reply_text("Tutorial link:  https://www.espncricinfo.com/live-cricket-match-schedule-fixtures")

def Results(update,context):
    update.message.reply_text("Tutorial link:  https://www.espncricinfo.com/live-cricket-match-results")

dispatcher.add_handler(telegram.ext.CommandHandler('start',Start))
dispatcher.add_handler(telegram.ext.CommandHandler('sports',Sports))
dispatcher.add_handler(telegram.ext.CommandHandler('Livescore',Livescore))
dispatcher.add_handler(telegram.ext.CommandHandler('Upcoming',Upcoming))
dispatcher.add_handler(telegram.ext.CommandHandler('Results',Results))




updater.start_polling()
updater.idle()
