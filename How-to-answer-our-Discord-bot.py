import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if not message.author.bot:
        if "Hello" in message.content:
            await message.reply(f"Hi")

client.run("token")