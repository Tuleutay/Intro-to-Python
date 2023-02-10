from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Salamaleysum {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text(f'/hello\n/sum\n/help')
async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = str(update.message.text)
    print(msg)
    list=msg.split()
    a = int(list[1])
    b = int(list[2])
    sum = a + b

    await update.message.reply_text(f'{a} + {b} = {sum}')

app = ApplicationBuilder().token("6056180153:AAHOxL3310Crw00kESSKYbpXtF-KDjQsU6s").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("sum", sum))
print('server start')
app.run_polling()