
from telethon.sync import TelegramClient
from telethon.tl.types import Channel
import json, os
from datetime import datetime

async def get_tikvah_entity():
    await client.start()
    async for dialog in client.iter_dialogs():
        if "tikvah" in dialog.name.lower():
            print(f"✅ Found Tikvah Entity: {dialog.name}")
            await client.disconnect()
            return dialog.entity
    await client.disconnect()
    return None

async def scrape_by_entity(entity):
    await client.start()
    messages = []
    async for msg in client.iter_messages(entity, limit=100):
        messages.append(msg.to_dict())

    today = datetime.today().strftime('%Y-%m-%d')
    os.makedirs(f"data/raw/telegram_messages/{today}", exist_ok=True)
    with open(f"data/raw/telegram_messages/{today}/tikvah.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4, default=str)

    print(f"✅ Scraped {{len(messages)}} messages from Tikvah | Pharma")
    await client.disconnect()
