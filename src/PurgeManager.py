from tabnanny import check
from discord.ext import commands


class PuergeManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="delete")
    async def delete(self, ctx, number):
        await ctx.message.channel.purge(limit=int(number))
