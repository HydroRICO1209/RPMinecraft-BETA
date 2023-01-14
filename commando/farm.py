from discord.ext import commands
import discord
from progress.farm import *
from progress.farmlist import *

class farm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def farm(self, ctx, *, arg):
        try:
            item = Item(ctx)
            arglists = arg.split(" ")
            arglen = len(arglists)
            await ctx.send(f'arglen: {arglen}')
            def findspace():                 
                for farmland in item.farmlist: #[[n,n],[n,n]]
                    if farmland[1] == None:       #^^^^^
                        pass
                        #plant here
            
            #arg1: plant/harvest
            #arg2: croptype
            #arg3: location
    
            if arglen == 1: #error
                pass
                
            elif arglen == 2: #rpm farm plant potato 
                arg1 = arglists[0]
                await ctx.send(f'arg1: {arg1}')
                arg2 = arglists[1]
                await ctx.send(f'arg2: {arg2}')
                arg3 = 1 #findspace()
                await ctx.send(f'arg3: {arg3}')

            elif arglen == 3: #rpm farm harvest potato 3
                arg1 = arglists[0]
                await ctx.send(f'arg1: {arg1}')
                arg2 = arglists[1]
                await ctx.send(f'arg2: {arg2}')
                arg3 = arglists[2]
                await ctx.send(f'arg3: {arg3}')
        
            if arg1 == 'plant':
                if arg2 == 'potato':
                    if arg3 == False and item.potato > 1:
                        await ctx.send(f'planted potato in {arg3}')
                    elif arg3 == False:
                        await ctx.send('This place is already planted')
            
                elif arg2 == 'wheat_seeds':
                    if arg3 == False:
                        await ctx.send(f'planted wheat_seeds in {arg3}')
                    else:
                        await ctx.send('This place is already planted')
            
                elif arg2 == 'carrot':
                    if arg3 == False:
                        await ctx.send(f'carrot in {arg3}')
                    else:
                        await ctx.send('This place is already planted')
            
                elif arg2 == 'beetroot_seeds':
                    if arg3 == False:
                        await ctx.send(f'planted beetroot_seeds in {arg3}')
                    else:
                        await ctx.send('This place is already planted')
            
            elif arg1 == 'harvest':
                await ctx.send(f'harvested {arg2} in {arg3}')
        
        except Exception:
            raise Exception

async def setup(bot):
    await bot.add_cog(farm(bot))

#rpm farm plant potato 1
#rpm farm harvest 1