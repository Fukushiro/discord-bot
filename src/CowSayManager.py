from discord.ext import commands
import cowsay
from controller.cowsay_controller import get_ascii_image_for_discord


class CowSayManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command('cowsay')
    async def cowsay(self, ctx, statement):
        await ctx.send(get_ascii_image_for_discord('cow', statement))
