import sys
import asyncio
import logging

from classes.TelegramBotWebhook import TelegramBotWebhook
from database.base import async_session_maker, engine

logging.getLogger(__name__)


async def check_db():
    try:
        async with async_session_maker() as session:
            pass
        await engine.dispose()
    except Exception as e:
        logging.warning(e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[0] == 'check_db':
            asyncio.run(check_db())
    else:
        telebot = TelegramBotWebhook()
        telebot.start_webhook()
