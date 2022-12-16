from aiogram import Dispatcher
from aiogram.utils.executor import start_webhook

from .TelegramBot import TelegramBot


class TelegramBotWebhook(TelegramBot):
    def __init__(self):
        super(TelegramBotWebhook, self).__init__()
        self.__url = f"https://{self.config.WEBHOOK_URL}/{self.config.TOKEN}"

    def certificate(self):
        if self.config.WEBHOOK_SSL_CERT:
            return open(self.config.WEBHOOK_SSL_CERT, 'rb')

    async def on_startup_webhook(self, dp: Dispatcher):
        webhook = await self.bot.get_webhook_info()

        if webhook.url != self.config.WEBHOOK_URL:
            if not webhook.url:
                await self.bot.delete_webhook()

            await self.bot.set_webhook(self.__url, certificate=self.certificate())
        await self.on_startup(self.dp)

    async def on_shutdown_webhook(self, dp: Dispatcher):
        await self.bot.delete_webhook()
        await self.dp.storage.close()
        await self.dp.storage.wait_closed()

    def start_webhook(self):
        start_webhook(
            dispatcher=self.dp,
            webhook_path=f'/{self.config.TOKEN}',
            on_startup=self.on_startup_webhook,
            on_shutdown=self.on_shutdown_webhook,
            skip_updates=self.config.SKIP_UPDATES,
            host='0.0.0.0',
            port='49151',
        )



