from discord.ext import commands


class RoleManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cool")
    async def cool_bot(self, ctx):
        await ctx.send('Something')


# async def setup(bot: commands.Bot) -> None:
#     await bot.add_cog(RoleManager(bot))
