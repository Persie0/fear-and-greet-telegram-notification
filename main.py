import telegram
import fear_and_greed
import asyncio

# Set up the Telegram bot
bot_token = "6223994870:AAHX7P4Pk3VNc7rnqEBeOzes28fBmISlHBs"
chat_id = 576668948

async def notify(value:float):
    if value < 30:
        # Send a notification if the value is below 30
        message = f"The Fear and Greed Index is {format(round(value, 2))}" 
        await bot.send_message(chat_id=chat_id, text=message)

    print("Sent a notification")

if __name__ == "__main__":
    # Create a bot instance
    bot = telegram.Bot(token=bot_token)
    # Get the Fear and Greed Index value
    value = fear_and_greed.get().value
    asyncio.run(notify(value))