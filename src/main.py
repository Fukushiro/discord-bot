import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from RoleManager import RoleManager
from globalValues import black_list, owners
load_dotenv()
bot = commands.Bot(command_prefix='!')  # discord.bot()
token = os.getenv("TOKEN")


# events


@bot.event
async def on_ready():
    print(f"Logged in as a bot {bot.user}")


@bot.event
async def on_message(message):
    author = str(message.author)
    if message.author == bot.user:
        return
    if message.content.startswith('fuku'):
        await message.channel.send('teste')
    if message.content.startswith('Ola') and author in owners:
        await message.channel.send('Oi')
    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    print("Apagada")

    deleter = None
    async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
        deleter = entry.user
    print(deleter)
    if deleter is not None:
        print(f"{deleter.name} deleted message by {message.author.name}")
        send_message = f'Cara que deleto: {deleter.name},  Dono da mensagem: {message.author.name}, Mensagem: {message.content}'
        if len(message.attachments) > 0:
            send_message += f', attach: {message.attachments[0].url}'
        await message.channel.send(send_message)


# cogs

bot.add_cog(RoleManager(bot))

# run bot
bot.run(token)
