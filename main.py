import discord
from dotenv import load_dotenv
import os

load_dotenv()
client = discord.Client()
token = os.getenv("TOKEN")
print(token)

# user events


@client.event
async def on_ready():
    print(f"Logged in as a bot {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # await message.channel.send(message.content)


@client.event
async def on_message_delete(message):
    print("Apagada")
    deleter = None
    async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
        deleter = entry.user
    print(deleter)
    if deleter is not None:
        print(f"{deleter.name} deleted message by {message.author.name}")
        await message.channel.send(f'Cara que deleto: {deleter.name},  Dono da mensagem: {message.author.name}, Mensagem: {message.content}')

# run client
client.run(token)
