# Creating a README.md file with the provided content for the ETH Price Checker Telegram Bot
readme_content = """# ETH Price Checker Telegram Bot

This is a simple Telegram bot that provides real-time price information for Ethereum (ETH) using the CoinMarketCap API. Built with Python and Aiogram, this bot allows users to query the current price of ETH in various currencies.

## Features

- Get the current price of Ethereum (ETH) in different currencies.
- User-friendly interaction through Telegram.
- Fast response times and reliable price data.

## Technologies Used

- Python
- Aiogram (for Telegram Bot API)
- CoinMarketCap API

## Requirements

- Python 3.7 or higher
- Aiogram library
- Requests library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Arm1npa/ETH-PRICE-BOT.git
   cd ETH-PRICE-BOT
Install the required packages:

bash
Always show details

Copy code
pip install -r requirements.txt
Set up your environment variables. Create a .env file in the root directory of your project and add your CoinMarketCap API key and Telegram Bot token:

plaintext
Always show details

Copy code
COINMARKETCAP_API_KEY=your_coinmarketcap_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
Usage
Start the bot by running:

bash
Always show details

Copy code
python bot.py
Open Telegram and search for your bot. Start a conversation and use the command /price to get the current price of Ethereum.

Commands
/price - Get the current price of Ethereum in your preferred currency.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- CoinMarketCap for providing cryptocurrency market data.
- Aiogram for making it easy to build Telegram bots with Python. """
