from discord.ext import commands
import discord
import progress.database

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test1(self, ctx, *, arg):
        dbfunc = self.bot.database_handler
        arglists = arg.split(" ")
        arglen = len(arglists)
        if arglen == 3:
            #item, tablename, userid
            value = await dbfunc.fetchvalue(arglists[0], arglists[1], arglists[2])
            await ctx.send(value)
        else:
            await ctx.send(f'arglen is only {arglen}, it should be 3 dumb')
            
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def test2(self, ctx, *, arg):
        dbfunc = self.bot.database_handler
        arglists = arg.split(" ")
        arglen = len(arglists)
        if arglen == 4:
            #item, tablename, userid, newvalue
            value = await dbfunc.updatevalue(arglists[0], arglists[1], arglists[2], arglists[3])
            await ctx.send(value)
        else:
            await ctx.send(f'arglen is only {arglen}, it should be 4 dumb')
            
async def setup(bot):
    await bot.add_cog(Test(bot))