from discord.ext import commands


class MathManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calculate")
    async def calculate(self, ctx, *, expression):
        print(expression)
        result = eval(expression)
        await ctx.send(result)
