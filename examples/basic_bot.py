import asyncio
import os

from botato.client import BotatoClient
from loguru import logger

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your token from env for safety
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("You must set the DISCORD_TOKEN environment variable.")

bot = BotatoClient(token=TOKEN)


@bot.event
async def on_ready(data):
    """
    Triggered when the bot is ready (GUILD_CREATE or READY event).
    """
    logger.info("Bot is now connected and ready!")
    
    
@bot.event
async def on_message_create(data):
    """
    Triggered when a message is sent in a text channel.
    """
    author = data["author"]["username"]
    content = data["content"]
    logger.info(f"Message from {author}: {content}")
    


async def main():
    try:
        await bot.connect()
    except KeyboardInterrupt:
        logger.info("Shutting down bot...")
        await bot.close()
        
if __name__ == "__main__":
    asyncio.run(main())