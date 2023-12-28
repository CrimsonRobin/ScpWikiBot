import discord
import responses
from env import private_token


async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)
        await message.channel.send(f"Error: '{e}' has occurred.")


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    TOKEN = private_token()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        # general debugging, is useful
        print(f"{username} said: '{user_message}' in ({channel})")

        if user_message.startswith("!scp"):
            user_message = user_message[4:]
            await send_message(message, user_message)

    client.run(TOKEN)
