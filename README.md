# Fear and Greed Telegram Bot
This bot send you a message if the CNN fear and greed index is below 30 (fear).
## How to set up
1. Create a bot with the BotFather
2. Get your chat id by sending a message to the bot and then go to https://api.telegram.org/bot<yourtoken>/getUpdates
3. Add your bot token and your chat id to the github secrets
one with the name `TELEGRAM_BOT_TOKEN` and one with the name `TELEGRAM_CHAT_ID`