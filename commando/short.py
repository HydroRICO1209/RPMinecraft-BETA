from discord.ext import commands
import discord

class Others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

######   ######   ##    ##   ######
##  ##     ##     ####  ##   ##
######     ##     ##  ####   ##  ##
##       ######   ##    ##   ######
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

##  ##   ######   ########   ######
##  ##   ##  ##      ##      ##
##  ##   ##  ##      ##      ####
##  ##   ##  ##      ##      ##
  ##     ######      ##      ######
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def vote(self, ctx):
        embed=discord.Embed(
            title="**Vote for RPMinecraft**", 
            url = 'https://top.gg/bot/905427623780442142/vote',
            description="""
You can vote for RPMinecraft and get the following rewards (you can vote every 12h)

**Vote Rewards**
5 steak <:steak:917408224913797140>
1 rare chest <:rare_chest:971653832411066378>
""", 
            color = discord.Color.blue())
        await ctx.send(embed=embed)
    
    @commands.command()
    async def hydrorico_check(self, ctx, arg:str): #check database value
        try:
            userid = ctx.author.id
            if userid != 757508305256972338:
                await ctx.send('**ACCESS DENIED**')
            else:
                dbfunc = self.bot.database_handler
                arglists = arg.split(" ")
                arglen = len(arglists)
                if arglen is 3:
                    #item, tablename, userid
                    value = await dbfunc.fetchValue(arglists[0], arglists[1], arglists[2])
                    await ctx.send(value)
                else:
                    await ctx.send(f'arglen is only {arglen}, it should be 3 dumb')
        except KeyError:
            await ctx.send(f'**{arg}** is not in database')
    
    @commands.command()
    async def hydrorico_server_list(self, ctx): #number of server
        userid = ctx.author.id
        if userid != 757508305256972338:
            await ctx.send('**ACCESS DENIED**')
        else:
            for gu in bot.guilds:
                print(f'{number}) {gu.name}: {gu.owner}')

    @commands.command
    async def hack(self, ctx, arg:str): #hack item
        try:
            dbfunc = self.bot.database_handler
            arglists = arg.split(" ")
            arglen = len(arglists)
            if arglen is 4:
                #item, tablename, userid, newvalue
                await dbfunc.setIntValue(arglists[0], arglists[1], arglists[2], arglists[3])
                await ctx.send(f'{arglists[0]} is now {arglists[3]}')
        except KeyError:
            await ctx.send(f'**{arglists[0]}** is not in database')

async def setup(bot):
    await bot.add_cog(Others(bot))