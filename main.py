from telethon import TelegramClient, events

# брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''

client = TelegramClient('mirror', api_id, api_hash)

client.start()

for dialog in client.iter_dialogs():
    print(dialog.title + " - " + str(dialog.id))