import configurator
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import PeerChannel, MessageMediaPhoto
from telethon.tl.functions.messages import GetHistoryRequest
import asyncio
import constants
import json
import os

class SignalClient:
    '''Klasse die den Client enthält und Signale in die Gruppe postet'''
    def __init__(self):
        # Liest Konfigurationsdatei aus und speichert Werte wie api_id in self.config_data.api_id
        self.config_data = configurator.ConfigData(constants.CONFIG)
        self.client      = TelegramClient(self.config_data.username, self.config_data.api_id, self.config_data.api_hash)

    async def get_signal(self):
        # Wandle .json-Datei am angegebenen Pfad in Signal für Telegram um
        await self.client.start()
        print('Client erfolgreich gestartet...')
        # Authorisierung gewährleisten
        if await self.client.is_user_authorized() == False:
            await self.client.send_code_request(self.config_data.phone)
            try:
                await self.client.sign_in(self.config_data.phone, input('Bitte den Code von Telegram eingeben: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('Passwort: '))
        channel = await self.client.get_entity(PeerChannel(self.config_data.channel_id))
        history = await self.client(GetHistoryRequest(
            peer        = channel,
            offset_id   = 0,
            offset_date = None,
            add_offset  = 0,
            limit       = 1,
            max_id      = 0,
            min_id      = 0,
            hash        = 0
        ))
        # Lade einen Dateianhang herunter
        message  = history.messages[0]
        # Für den Fall, dass keine Datei im Anhang ist
        if not message.media:
            return
        else:
            if message.media.document.mime_type == constants.TELEGRAM_JSON:
                filepath = os.path.join(os.getcwd(), constants.SIGNALS, message.media.document.attributes[0].file_name)
                if not os.path.isfile(filepath):
                    await self.client.download_media(message, filepath)
                    return filepath
                else:
                    return
            else:
                return

    def send_message(self, message):
        with self.client:
            self.client.loop.run_until_complete(await self.client.send_message('me', message))

    def run_get_signal(self):
        with self.client:
            self.client.loop.run_until_complete(self.get_signal())
