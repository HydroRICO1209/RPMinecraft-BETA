from discord.ext import commands
import discord
from progress.my_emote import *
from progress.misc import *
from progress.stats import *


class Trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def trade(self, ctx, *, arg):
        try:
            e = My_emote(ctx)
            misc = await Misc(ctx)
            stats = await Stats(ctx)
            
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            
            if stats.area in [7, 8]:
                arglists = arg.split(" ")
                arglen = len(arglists)
                if arglen == 1:
                    action = arglists[0]
                    trader_wanted = 'nobody'
        
                elif arglen == 3:
                    action = arglists[0]
                    trader_wanted = arglists[1]
                    trade_option = arglists[2]
                    number = 1
        
                elif arglen == 4:
                    action = arglists[0]
                    trader_wanted = arglists[1]
                    trade_option = arglists[2]
                    number = int(arglists[3])

                if action == 'sell':
            
                    if trader_wanted == 'bob':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} wood for emerald')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} cobble for emerald')
                
                    elif trader_wanted == 'wagner':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} iron_ingot for emerald')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} diamond for emerald')
        
                    elif trader_wanted == 'sarth':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} pogchop for emerald')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} beef for emerald')
        
                    elif trader_wanted == 'ashley':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} poisonous potato for emerald')
            
                    elif trader_wanted == 'asher':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} potato for emerald')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} wheat_seeds for emerald')  
                        elif trade_option == 'c':
                            await ctx.send(f'traded {number} carrot for emerald')
                        elif trade_option == 'd':
                            await ctx.send(f'traded {number} wheat for emerald')
        
                    elif trader_wanted == 'ryuga':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} wool for emerald')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} beetroot for emerald')
            
                    elif trader_wanted == 'nobody': #sell
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
`rpm trade sell [trader] [a,b,c,d] [amount(optional)]` -> to trade
''')
            
                elif action == 'buy':
            
                    if trader_wanted == 'skev':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} emerald for small_sapling')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} emerald for apple')
                
                    elif trader_wanted == 'sarth':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} emerald for cooked_pogchop')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} emerald for steak')
        
                    elif trader_wanted == 'ashley':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} emerald for cleansed_dirt')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} emerald for cleansed_water_bucket')
        
                    elif trader_wanted == 'asher':
                        if trade_option == 'a':
                            await ctx.send(f'traded {number} emerald for potato')
                        elif trade_option == 'b':
                            await ctx.send(f'traded {number} emerald for wheat_seeds')
                        elif trade_option == 'c':
                            await ctx.send(f'traded {number} emerald for carrot')
                        elif trade_option == 'd':
                            await ctx.send(f'traded {number} emerald for beetroot_seeds')      
        
                    elif trader_wanted == 'nobody': #buy
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
`rpm trade buy [trader] [a,b,c,d] [amount(optional)]` -> to trade
''')
            elif stats.area not in [7, 8]:
                await ctx.send(f'**{username}**, you need to be in village in order to trade')
            else:
                await ctx.send('''
correct format of trading
`rpm trade [buy/sell]` -> to show tradelist
`rpm trade [buy/sell] [trader] [a,b,c,d] [amount(optional)]` -> to trade
''')
            
        except UnboundLocalError:
            await ctx.send('''
correct format of trading
`rpm trade [buy/sell]` -> to show tradelist
`rpm trade [buy/sell] [trader] [a,b,c,d] [amount(optional)]` -> to trade
''')

async def setup(bot):
    await bot.add_cog(Trade(bot))