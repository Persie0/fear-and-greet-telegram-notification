import os
import telegram
import fear_and_greed

# Set up the Telegram bot
bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']

# Create a bot instance
bot = telegram.Bot(token=bot_token)

# Get the Fear and Greed Index value
value = fear_and_greed.get().value

if value < 30:
    # Send a notification if the value is below 30
    message = f"The Fear and Greed Index is {value}. Time to buy some crypto!"
    bot.send_message(chat_id=chat_id, text=message)
else:
    # Otherwise, just print the value to the console
    #print(f"The Fear and Greed Index is {value}.")
    message = f"The Fear and Greed Index is {value}."
    bot.send_message(chat_id=chat_id, text=message)
