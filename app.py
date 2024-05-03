from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from erdem_bot.credentials import bot_token

cp = {494938886: 1160289394,
      1160289394: 494938886}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=cp[update.effective_chat.id], text=update.effective_message.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(bot_token).build()
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler("hello", hello)
    forward_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), forward)
    app.add_handlers([start_handler, hello_handler, forward_handler])
    app.run_polling()
