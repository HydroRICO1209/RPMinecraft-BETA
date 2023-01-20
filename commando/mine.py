from discord.ext import commands
import discord, random
from progress.stats import *
from progress.misc import *
from progress.my_emote import *

class Mine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def mine(self, ctx):
        try:
            misc = await Misc(self.bot, ctx)
            stats = await Stats(self.bot, ctx)
            e = My_emote(ctx)
            
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.id
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
    
            if stats.area in [1, 2, 3]:
                if num1 <= 80: #80%
                    loottype = 'coal'
                    emotechosen = e.coal
                elif num1 <= 100: #20%
                    loottype = 'cobble'
                    emotechosen = e.cobble
            
            elif stats.area in [4, 5, 6]:
                if num1 <= 10: #10%
                    loottype = 'coal'
                    emotechosen = e.coal
                elif num1 <= 80: #70%
                    loottype = 'iron_ingot'
                    emotechosen = e.iron_ingot
                elif num1 <= 100: #20%
                    loottype = 'cobble'
                    emotechosen = e.cobble

            elif stats.area in [7, 8]:
                if num1 <= 10: #10%
                    loottype = 'coal'
                    emotechosen = e.coal
                elif num1 <= 30: #20%
                    loottype = 'iron_ingot'
                    emotechosen = e.iron_ingot
                elif num1 <= 90: #60%
                    loottype = 'diamond'
                    emotechosen = e.diamond
                elif num1 <= 100: #10%
                    loottype = 'cobble'
                    emotechosen = e.cobble
    
            elif stats.area in [9, 10, 11, 12]:
                if num1 <= 40: #40%
                    loottype = 'gold_ingot'
                    emotechosen = e.gold_ingot
                elif num1 == 41: #1%
                    loottype = 'netherite_scrap'
                    emotechosen = e.netherite_scrap
                elif num1 <= 100: #59%
                    loottype = 'cobble'
                    emotechosen = e.cobble
    
            elif stats.area in [13, 14]:
                if num1 <= 10: #10%
                    loottype = 'coal'
                    emotechosen = e.coal
                elif num1 <= 20: #10%
                    loottype = 'iron_ingot'
                    emotechosen = e.iron_ingot
                elif num1 <= 40: #20%
                    loottype = 'diamond'
                    emotechosen = e.diamond
                elif num1 <= 80: #40%
                    loottype = 'redstone'
                    emotechosen = e.redstone
                elif num1 <= 100: #20%
                    loottype = 'cobble'
                    emotechosen = e.cobble
    
            if loottype == 'netherite_scrap':
                if num2 <= 69: #69%
                    lootcount = 1
                elif num2 <= 89: #20%
                    lootcount = 2
                elif num2 <= 89: #10%
                    lootcount = 3
                elif num2 <= 100:#1%
                    lootcount = 4
                await dbfunc.updateIntValue(loottype, 'misc', userid, lootcount)

            else:
                if num2 <= 45: #45%
                    lootcount = 1
                elif num2 <= 75: #30%
                    lootcount = 2
                elif num2 <= 85: #10%
                    lootcount = 3
                elif num2 <= 95: #10%
                    lootcount = 5
                elif num2 <= 100: #5%
                    lootcount = 10
                await dbfunc.updateIntValue(loottype, 'misc', userid, lootcount)
    
            if lootcount == 1:
                await ctx.send(f'**{username}** found and mined **{lootcount} {loottype}** {emotechosen}')
            else:
                await ctx.send(f'**{username}** found and mined **{lootcount} {loottype}s** {emotechosen}')
        
            num1 = random.randint(0,10000) 
            if num1 == 69: #bedrock 0.1%
                await ctx.send(f'HOLEY POGEY, **{username}** GOT A **BEDROCK** {e.ebedrock}. SOMEONE CLIP THAT!')
                await dbfunc.updateIntValue('bedrock', 'illegal', userid, 1)
                
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Mine(bot))