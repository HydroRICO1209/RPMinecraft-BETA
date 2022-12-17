from discord.ext import commands
import discord

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def cursed(self, attribute, tablename, userid):
        return (await self.bot.db.fetch('SELECT $1 FROM $2 WHERE userid = $3',attribute, tablename, userid))[0]["name"]
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test(self, ctx):
        var = cursed('name', 'user', 1234)
    
async def setup(bot):
    await bot.add_cog(Test(bot))