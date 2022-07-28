from discord.ext import commands
from discord import app_commands
from globalValues import PermissionSingleton
permissionSingleton = PermissionSingleton()


class PermissionManager(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command('set_can_block')
    async def set_can_block(self, ctx, val: bool):
        permissionSingleton.all_can_block = val
        await ctx.send('Permissão alterada')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PermissionManager(bot))
