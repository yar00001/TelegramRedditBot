from reddit_bot.util import log
from reddit_bot.reddit import reddit_handler
import configparser
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

logger = log.get_configured_logger()

telegram_config = configparser.ConfigParser()
telegram_config.read('config/telegram.properties')

updater = Updater(token=telegram_config.get('BOT', 'Token'), use_context=True)
dispatcher = updater.dispatcher


def subreddit_command(update, context):
    """
    Return top 5 topics in the subreddit
    """
    sub = ' '.join(context.args).upper()
    logger.info('subreddit passed after /sub: {}'.format(sub))

    title_list = reddit_handler.get_n_hot_submissions(sub, 5)

    context.bot.send_message(chat_id=update.message.chat_id, text=output_list(title_list))

def output_list(list):
    res = ''
    for line in list:
        res = res + line + '\n'
    return res

subreddit_handler = CommandHandler('sub', subreddit_command)
dispatcher.add_handler(subreddit_handler)

# Start polling
updater.start_polling()
