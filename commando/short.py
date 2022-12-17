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
    async def hydrorico(self, ctx, arg: int): #delete account
        userid = str(ctx.author.id)
        if userid != '757508305256972338':
            await ctx.send('**ACCESS DENIED**')
        else:
            matches = db.prefix(arg)
            for match in matches:
                del db[match]
            await ctx.send(f'**{matches}** deleted from db')
    
    @commands.command()
    async def debug(self, ctx, arg:str): #check database value
        try:
            userid = str(ctx.author.id)
            if userid != '757508305256972338':
                await ctx.send('**ACCESS DENIED**')
            else:
                value = db[arg]
                await ctx.send(f'**{arg}** = **{value}**')
        except KeyError:
            await ctx.send(f'**{arg}** is not in database')
    
    @commands.command()
    async def server(self, ctx): #number of server
        number = 0
        msg = '```'
        msg2 = '```'
        userid = str(ctx.author.id)
        if userid != '757508305256972338':
            await ctx.send('**ACCESS DENIED**')
        else:
            for gu in bot.guilds:
                if len(msg) < 1950:
                    number += 1
                    msg += f'{number}) {gu.name}: {gu.owner}\n'
        
        msg += '```'
        await ctx.send(msg)

    @commands.command
    async def hack(self, ctx, arg:str): #hack item
        try:
            userid = str(ctx.author.id)
            if userid != '757508305256972338':
                await ctx.send('**ACCESS DENIED**')
            else:
                db[arg] += 1
                value = db[arg]
                await ctx.send(f'**{arg}** = {value}')
        except KeyError:
            await ctx.send(f'**{arg}** is not in database')

async def setup(bot):
    await bot.add_cog(Others(bot))