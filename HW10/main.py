import requests
import random
from bs4 import BeautifulSoup as b
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


URL='https://www.anekdot.ru/last/good/'

#URL = 'https://www.newkaliningrad.ru/horoscope/'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div',class_ = 'text')
    #goroscops = soup.find_all('div', class_ = "col-sm-12 col-md-6"){p}
    return [c.text for c in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)
print(list_of_jokes)
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, чтобы посмеятся введите команду /whaha')

async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(list_of_jokes)<1:
        list_of_jokes.append('Анекдотики закончились')
        await update.message.reply_text(f'{list_of_jokes[0]}')
    else:
        await update.message.reply_text(f'{list_of_jokes[0]}')
        del list_of_jokes[0]



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/whaha\n/help')




app = ApplicationBuilder().token("6012121848:AAHJQ5OPOEv4kL6XQigN0Hy_S2-F1qrBc1s").build()


app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler('whaha', jokes))
app.add_handler(CommandHandler("help", help))
app.run_polling()



