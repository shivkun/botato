import asyncio
import os

from botato.client import BotatoClient
from botato.intents import Intents
from botato.models.message import Message
from loguru import logger

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your token from env for safety
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("You must set the DISCORD_TOKEN environment variable.")

# Setup intents
intents = Intents.default()
logger.info(f"Using intents: {intents.describe()}")

bot = BotatoClient(token=TOKEN, intents=intents)


@bot.event
async def on_ready(data):
    """
    Triggered when the bot is ready (GUILD_CREATE or READY event).
    """
    logger.info("Bot is now connected and ready!")
    
    
@bot.event
async def on_message_create(message: Message):
    """
    Triggered when a message is sent in a text channel.
    """
    logger.info(f"Message from {message.author.username}: {message.content}")
    

async def main():
    try:
        await bot.connect()
    except KeyboardInterrupt:
        logger.info("Shutting down bot...")
        await bot.close()
        
if __name__ == "__main__":
    asyncio.run(main())