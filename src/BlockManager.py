from ctypes import memset
from discord.ext import commands
import discord
from globalValues import PermissionSingleton, Singleton, owners
from utils.api import block_user, get_blocked_users
permissionSingleton = PermissionSingleton()
sing = Singleton()


class BlockManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='block')
    async def block_user(self, ctx, member: discord.Member):

        print('Aqui')
        # limita uso apenas por owners
        if str(ctx.message.author) not in owners and not permissionSingleton.all_can_block:
            return
        if str(member) in owners:  # bloqueia o block de owners
            return
        if str(member) == str(self.bot.user):
            return
        funcionou = block_user(str(member), 1)
        # sing.users_to_delete_message.append(str(member))
        usuarios_bloqueados = get_blocked_users()
        if not funcionou:
            return await ctx.send('Erro')
        await ctx.send('Usuario bloqueado ---->' + str(usuarios_bloqueados))

    @commands.command(name='unblock')
    async def unblock_user(self, ctx, member: discord.Member):
        # limita uso apenas por owners
        if str(ctx.message.author) not in owners and not permissionSingleton.all_can_unblock:
            return

        # if str(member) in sing.users_to_delete_message:
        #     sing.users_to_delete_message.remove(str(member))
        #     await ctx.send('Usuario desbloqueado')
        funcionou = block_user(str(member), 0)

        if not funcionou:
            return await ctx.send('Erro')

        await ctx.send('Usuario desbloqueado')

    @commands.command(name='unblockall')
    async def unlockall(self, ctx):
        if str(ctx.message.author) not in owners and not permissionSingleton.all_can_unblock:
            return
        sing.users_to_delete_message = []
        await ctx.send('Todos desbloqueados')
