from discord.ext import commands
import discord
from progress.my_emote import *

class Trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def trade(self, ctx, *, arg):
        try:
            e = My_emote(ctx)
            arglists = arg.split(" ")
            arglen = len(arglists)
            if arglen == 1:
                arg1 = arglists[0]
                arg2 = 'nobody'
    
            elif arglen == 3:
                arg1 = arglists[0]
                arg2 = arglists[1]
                arg3 = arglists[2]
                arg4 = 1
    
            elif arglen == 4:
                arg1 = arglists[0]
                arg2 = arglists[1]
                arg3 = arglists[2]
                arg4 = int(arglists[3])

            if arg1 == 'sell':
        
                if arg2 == 'bob':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} wood for emerald')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} cobble for emerald')
            
                elif arg2 == 'wagner':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} iron_ingot for emerald')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} diamond for emerald')
    
                elif arg2 == 'sarth':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} pogchop for emerald')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} beef for emerald')
    
                elif arg2 == 'ashley':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} poisonous potato for emerald')
        
                elif arg2 == 'asher':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} potato for emerald')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} wheat_seeds for emerald')  
                    elif arg3 == 'c':
                        await ctx.send(f'traded {arg4} carrot for emerald')
                    elif arg3 == 'd':
                        await ctx.send(f'traded {arg4} wheat for emerald')
    
                elif arg2 == 'ryuga':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} wool for emerald')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} beetroot for emerald')
        
                elif arg2 == 'nobody': #sell
                    tradelist = f'''
    **__Bob, the Builder__**
    a) {e.wood}wood -> {e.emerald}emerald
    b) {e.cobble}cobble x10 -> {e.emerald}emerald x1
    
    **__Wagner, the Blacksmith__**
    a) {e.iron_ingot}iron_ingot -> {e.emerald}emerald
    b) {e.diamond}diamond -> {e.emerald}emerald
    
    **__Skev, the Lumberjack__**
    ~~None~~

    **__Sarth, the Butcher__**
    a) {e.pogchop}pogchop -> {e.emerald}emerald
    b) {e.beef}beef -> {e.emerald}emerald
    
    **__Ashley, the Cleric__**
    a) {e.poisonous_potato}poisonous_potato -> {e.emerald}emerald
    
    **__Asher, the Farmer__**
    a) {e.potato}potato -> {e.emerald}emerald
    b) {e.wheat_seeds}wheat_seeds -> {e.emerald}emerald
    c) {e.carrot}carrot -> {e.emerald}emerald
    d) {e.wheat}wheat -> {e.emerald}emerald
    
    **__Ryuga, the Shepherd__**
    1) {e.wool}wool -> {e.emerald}emerald
    2) {e.beetroot}beetroot -> {e.emerald}emerald
    '''
                    embed = discord.Embed(
                        description = tradelist, 
                        color = discord.Color.blue())
                    embed.set_author(name= f"{ctx.author.display_name}'s trade(Sell)", 
                    icon_url = ctx.author.avatar.url)
                    await ctx.send(embed=embed)

                else:
                    await ctx.send('''
correct format of trading
`rpm trade sell` -> to show tradelist
`rpm trade sell [who] [a,b,c,d] [amount(optional)]` -> to trade
''')
        
            elif arg1 == 'buy':
        
                if arg2 == 'skev':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} emerald for small_sapling')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} emerald for apple')
            
                elif arg2 == 'sarth':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} emerald for cooked_pogchop')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} emerald for steak')
    
                elif arg2 == 'ashley':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} emerald for cleansed_dirt')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} emerald for cleansed_water_bucket')
    
                elif arg2 == 'asher':
                    if arg3 == 'a':
                        await ctx.send(f'traded {arg4} emerald for potato')
                    elif arg3 == 'b':
                        await ctx.send(f'traded {arg4} emerald for wheat_seeds')
                    elif arg3 == 'c':
                        await ctx.send(f'traded {arg4} emerald for carrot')
                    elif arg3 == 'd':
                        await ctx.send(f'traded {arg4} emerald for beetroot_seeds')      
    
                elif arg2 == 'nobody': #buy
                    tradelist = f'''
**__Bob, the Builder__**
~~None~~

**__Wagner, the Blacksmith__**
a) {e.emerald}emerald -> R

**__Skev, the Lumberjack__**
a) {e.emerald}emerald -> {e.small_sapling}small_sapling
b) {e.emerald}emerald x20 -> {e.apple}apple x1

**__Sarth, the Butcher__**
a) {e.emerald}emerald x5 -> {e.cooked_pogchop}cooked_pogchop x1
b) {e.emerald}emerald x5 -> {e.steak}steak x1

**__Ashley, the Cleric__**
a) {e.emerald}emerald -> {e.cleansed_dirt}cleansed_dirt
b) {e.emerald}emerald -> {e.cleansed_water_bucket}cleansed_water_bucket

**__Asher, the Farmer__**
a) {e.emerald}emerald x25 -> {e.beetroot_seeds}beetroot_seeds x1
b) {e.emerald}emerald x50 -> {e.potato}potato x1
c) {e.emerald}emerald x75 -> {e.carrot}carrot x1
d) {e.emerald}emerald x100 -> {e.wheat_seeds}wheat_seeds x1

**__Ryuga, the Shepherd__**
~~None~~
    '''
                    embed = discord.Embed(
                        description = tradelist, 
                        color = discord.Color.blue())
                    embed.set_author(name= f"{ctx.author.display_name}'s trade(Buy)", 
                    icon_url = ctx.author.avatar.url)
                    await ctx.send(embed=embed)

        
                else:
                    await ctx.send('''
correct format of trading
`rpm trade buy` -> to show tradelist
`rpm trade buy [who] [a,b,c,d] [amount(optional)]` -> to trade
''')
            else:
                await ctx.send('''
correct format of trading
`rpm trade [buy/sell]` -> to show tradelist
`rpm trade [buy/sell] [who] [a,b,c,d] [amount(optional)]` -> to trade
''')
        except UnboundLocalError:
            await ctx.send('''
correct format of trading
`rpm trade [buy/sell]` -> to show tradelist
`rpm trade [buy/sell] [who] [a,b,c,d] [amount(optional)]` -> to trade
''')

async def setup(bot):
    await bot.add_cog(Trade(bot))