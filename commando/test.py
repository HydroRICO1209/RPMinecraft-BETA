from discord.ext import commands
import discord
from progress.item import cursed

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test(self, ctx):
        var = cursed('name', 'user', 1234)
        print(var)
    
async def setup(bot):
    await bot.add_cog(Test(bot))