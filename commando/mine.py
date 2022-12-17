from discord.ext import commands
import discord, random
from progress.stats import *
from progress.my_emote import *

class Mine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def mine(self, ctx):
        try:
            stats = Stats(ctx)
            e = My_emote(ctx)
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
                    db[stats.userid + loottype] += 1
                elif num2 <= 89: #20%
                    lootcount = 2
                    db[stats.userid + loottype] += 2
                elif num2 <= 89: #10%
                    lootcount = 3
                    db[stats.userid + loottype] += 3
                elif num2 <= 100:#1%
                    lootcount = 4
                    db[stats.userid + loottype] += 4

            else:
                if num2 <= 45: #45%
                    lootcount = 1
                    db[stats.userid + loottype] += 1
                elif num2 <= 75: #30%
                    lootcount = 2
                    db[stats.userid + loottype] += 2
                elif num2 <= 85: #10%
                    lootcount = 3
                    db[stats.userid + loottype] += 3
                elif num2 <= 95: #10%
                    lootcount = 5
                    db[stats.userid + loottype] += 5
                elif num2 <= 100: #5%
                    lootcount = 10
                    db[stats.userid + loottype] += 10
    
            if lootcount == 1:
                await ctx.send(f'**{ctx.author.name}** found and mined **{lootcount} {loottype}** {emotechosen}')
            else:
                await ctx.send(f'**{ctx.author.name}** found and mined **{lootcount} {loottype}s** {emotechosen}')
        
            num1 = random.randint(0,10000) 
            if num1 == 69: #bedrock 0.1%
                await ctx.send(f'HOLEY POGEY, **{ctx.author.name}** GOT A **BEDROCK** {e.ebedrock}. SOMEONE CLIP THAT!')
                db[stats.userid + 'bedrock'] += 1
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Mine(bot))