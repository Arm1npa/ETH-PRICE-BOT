import requests
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.filters import Command
import asyncio

# Replace with your API keys
COINMARKETCAP_API_KEY = 'YOUR_API_KEY'
TELEGRAM_BOT_TOKEN = 'YOUR_API_KEY'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Function to get cryptocurrency price from CoinMarketCap API


def get_crypto_price(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol, 'convert': 'USD'}
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    # Extract the price in USD
    price = data['data'][symbol]['quote']['USD']['price']
    return price

# Set bot description


async def set_bot_description():
    description = "I can fetch the latest cryptocurrency prices for you. Use the buttons below!"
    await bot.set_my_description(description)

# Handler for /start command, sends a custom reply keyboard for different coins


@dp.message(Command("start"))
async def send_welcome(message: Message):
    # Create reply buttons for different cryptocurrencies
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Get ETH Price")],
            [KeyboardButton(text="Get BNB Price")],
            [KeyboardButton(text="Get BTC Price")],
            [KeyboardButton(text="Get POL Price")],
            [KeyboardButton(text="Get TON Price")]
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )
    await message.answer("Welcome! Select a cryptocurrency to get the latest price.", reply_markup=keyboard)

# Handler for text messages that match button labels


@dp.message(lambda message: message.text in ["Get ETH Price", "Get BNB Price", "Get BTC Price", "Get POL Price", "Get TON Price"])
async def handle_crypto_message(message: Message):
    # Map text to cryptocurrency symbols
    symbol_mapping = {
        "Get ETH Price": "ETH",
        "Get BNB Price": "BNB",
        "Get BTC Price": "BTC",
        "Get POL Price": "POL",
        "Get TON Price": "TON"
    }

    symbol = symbol_mapping.get(message.text)

    if symbol:
        # Send loading message
        loading_message = await message.answer(f"Loading {symbol} price...")

        try:
            # Fetch cryptocurrency price
            price = get_crypto_price(symbol)

            # Edit loading message to display the actual price
            await loading_message.edit_text(f"The current price of {symbol} is ${price:.2f}")
        except Exception as e:
            # Edit the message to show error if API call fails
            await loading_message.edit_text(f"Error fetching {symbol} price: {str(e)}")

# Function to start the bot


async def main():
    # Set bot description
    await set_bot_description()

    # Start the bot
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.info("Starting the bot...")
    asyncio.run(main())
