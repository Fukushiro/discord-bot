from cmath import log
from http import client
from xmlrpc.client import boolean
import discord
from discord.ext import commands
from globalValues import Singleton, owners, recover_messages, set_recover_manager


class RoleManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cool")
    async def cool_bot(self, ctx):
        await ctx.send('Something')

    @commands.command(name='set_recover')
    async def set_recover(self, ctx, newValue: boolean):
        if str(ctx.message.author) not in owners:
            return
        sing = Singleton()
        sing.recover_message = newValue
        await ctx.send("Valor alterado")

    @commands.command(name='Admin')
    async def add_role(self, ctx, role: discord.Role):
        user = ctx.message.author
        author = str(user)
        if author in owners:
            await user.add_roles(role)


# async def setup(bot: commands.Bot) -> None:
#     await bot.add_cog(RoleManager(bot))
