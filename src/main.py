from concurrent.futures import process
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from BlockManager import BlockManager
from PermissionManager import PermissionManager
from RoleManager import RoleManager
from CowSayManager import CowSayManager
from MathManager import MathManager
from globalValues import Singleton, black_list, owners, users_to_delete_message, recover_messages
from controller.cowsay_controller import get_ascii_image_for_discord
from utils.api import get_blocked_users
load_dotenv()
bot = commands.Bot(command_prefix='!')  # discord.bot()
token = os.getenv("TOKEN")

singleton = Singleton()
# events


@bot.event
async def on_ready():
    print(process.env.BASE_URL)
    print(get_blocked_users())
    print(f"Logged in as a bot {bot.user}")


@bot.event
async def on_message(message):
    author = str(message.author)
    users_to_delete = get_blocked_users()
    sin = Singleton()
    if author in users_to_delete:
        await message.delete()
        return
    if message.author == bot.user:
        return
    if message.content.startswith('fuku'):
        await message.channel.send('teste')
    if message.content.startswith('Ola') and author in owners:
        await message.channel.send('Oi')
    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    users_to_delete = get_blocked_users()
    print(recover_messages)
    # if str(message.author) in owners:
    #     return
    if not singleton.recover_message:
        await message.channel.send(get_ascii_image_for_discord('cow', "Recover desligado"))
        return

    if str(message.author) in users_to_delete:
        return
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
        await message.channel.send(get_ascii_image_for_discord('cow', send_message))


@bot.event
async def on_message_edit(message_before, message_after):
    if message_before.content == message_after.content:
        return
    print(message_before.content)
    send_message = f'Mensagem anterior : {message_before.content}, Nova mensagem : {message_after.content}, dono da mensagem: {message_after.author.name} '
    await message_before.channel.send(send_message)


# cogs

bot.add_cog(RoleManager(bot))
bot.add_cog(CowSayManager(bot))
bot.add_cog(MathManager(bot))
bot.add_cog(BlockManager(bot))
bot.add_cog(PermissionManager(bot))


# run bot
bot.run(token)
