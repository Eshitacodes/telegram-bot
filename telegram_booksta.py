import telegram.ext

Token="6093088014:AAEjQjURbXcEhCbkqJDnkexA0s6ZpXdrRMA"

updater=telegram.ext.updater("6093088014:AAEjQjURbXcEhCbkqJDnkexA0s6ZpXdrRMA",use_context="True")
dispatcher=updater.dispatcher

def start(update,context):
    update.message.reply_text("Welcome to the world of Books!! \n Welcome to BOOKISHTA!!")

def help(update,context):
    update.message.reply_text(
        """
         /start -> Welcome to the bot
          /help-> This Particular Message
          /about-> About the Bot
           /satire -> To recommend some Satire Books
            /romcom -> To recommend some Romantic Comedy Books
             /comic -> To recommend some Comic Books
              /spiritual -> To recommend some Spiritual Books """
    )
def about(update,context):
    update.message.reply_text("I am a book bot designed by Eshita Yadav\nI can help you get your hands on some really cool books :)")

def satire(update,context):
    update.message.reply_text("Here you GO all set! : https://www.google.com/search?q=best+english+satire+books&tbas=0&tbs=bkv:a,bkt:b&tbm=bks&source=lnt&sa=X&ved=2ahUKEwjWwt64q4L_AhUn2DgGHaZEDzcQpwV6BAgBEBs&biw=1280&bih=605&dpr=1.5")

def romcom(update,context):
    update.message.reply_text("Here you GO with some romcom by Indian Authors! : https://www.google.com/search?q=best+english+romcom+books+by+Indian+Authors&tbs=bkt:b,bkv:a,cdr:1,cd_min:2000,cd_max:2099&tbm=bks&source=lnt&sa=X&ved=2ahUKEwiZ78_grIL_AhVs_DgGHSIIBPgQpwV6BAgKECI&biw=1280&bih=605&dpr=1.5")

def comic(update,context):
    update.message.reply_text("Here you GO on to have some FuN! : https://www.google.com/search?q=best+english+comic+books&tbs=bkt:b,bkv:a&tbm=bks&tbas=0&source=lnt&sa=X&ved=2ahUKEwjUptCMrYL_AhX78DgGHWf9AIoQpwV6BAgKECE&biw=1280&bih=605&dpr=1.5")

def spiritual(update,context):
    update.message.reply_text("Here you GO with Peace ! : https://www.google.com/search?q=best+spiritual+books&biw=1280&bih=605&tbs=bkt%3Ab%2Cbkv%3Aa&tbm=bks&ei=pe1nZMOFKJzAjuMPjuO2aA&ved=0ahUKEwiD7NOPrYL_AhUcoGMGHY6xDQ0Q4dUDCAk&uact=5&oq=best+spiritual+books&gs_lcp=Cg1nd3Mtd2l6LWJvb2tzEAM6BAghEApQ7RtYsjJguDtoAHAAeACAAfgBiAHmD5IBBTAuOS4ymAEAoAEBwAEB&sclient=gws-wiz-books")

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
dispatcher.add_handler(telegram.ext.CommandHandler('about',about))
dispatcher.add_handler(telegram.ext.CommandHandler('satire',satire))
dispatcher.add_handler(telegram.ext.CommandHandler('romcom',romcom))
dispatcher.add_handler(telegram.ext.CommandHandler('comic',comic))
dispatcher.add_handler(telegram.ext.CommandHandler('spiritual',spiritual))

updater.start_polling()
updater.idle()