from discord.ext import commands
import discord
from progress.stats import *
from progress.atk_def import *

class Boss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def boss(self, ctx):
        try:
            stats = await Stats(ctx)
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name

            
            if stats['highest_area'] > stats['area']:
                await ctx.send('This area doesnt have any boss anymore')
            elif stats['highest_area'] == stats['area']:
                if stats['area'] == 1:
                    bossName = 'The Mutated Poggy'
                    mobdef = 50
                    mobatk = 15
                    newArea = 2
                elif stats['area'] == 2:
                    bossName = 'Giant Zompiggy'
                    mobdef = 100
                    mobatk = 25
                    newArea = 3
                elif stats['area'] == 3:
                    bossName = 'WOC ehT , enobrenniD'
                    mobdef = 200
                    mobatk = 35
                    newArea = 4
                elif stats['area'] == 4:
                    bossName = 'GIANT SPIDER'
                    mobdef = 500
                    mobatk = 45
                    newArea = 5
                elif stats['area'] == 5:    
                    bossName = 'Wooly Skeleton'
                    mobdef = 800
                    mobatk = 56
                    newArea = 6
                elif stats['area'] == 6:
                    bossName = 'Skeleton KING'
                    mobdef = 1000
                    mobatk = 70
                    newArea = 7
                elif stats['area'] == 7:
                    bossName = 'Johnny, THE RAIDER'
                    mobdef = 1500
                    mobatk = 135
                    newArea = 8
                elif stats['area'] == 8:
                    bossName = 'Elder Guardian'
                    mobdef = 2000
                    mobatk = 300
                    newArea = 8
                elif stats['area'] == 9:
                    bossName = 'Cheezy Blaze'
                    mobdef = 2000
                    mobatk = 145
                    newArea = 10
                elif stats['area'] == 10:
                    bossName = 'GIANT MAGMA CUBE'
                    mobdef = 2300
                    mobatk = 175
                    newArea = 11
                elif stats['area'] == 11:
                    bossName = 'small wither'
                    mobdef = 2500
                    mobatk = 200
                    newArea = 12
                elif stats['area'] == 13:
                    bossName = 'Silvered Enderman'
                    mobdef = 2800
                    mobatk = 380
                    newArea = 14
                
                mobatktotal = round(mobdef / stats['atk'])
                damage = (mobatk - stats['defend']) * mobatktotal
                if damage < 0: damage = 0
                newhp = stats['hp'] - damage
                
                if newhp > 0:
                    await dbfunc.setIntValue('hp', 'stats', userid, newhp)
                    await dbfunc.setIntValue('highest_area', 'stats', userid, newArea)
                    await dbfunc.setIntValue('area', 'stats', userid, newArea)
                    await ctx.send(f'''
    **{username}** went into a BIGGG cave to find the boss
    Looks like **{username}** found **{bossName}**
    Some serious fights are going on
    LOOKS LIKE **{username}** WINS
    Lost {damage} HP, remaining HP {newhp}/100
    **{username}** went to the NEXT AREA!!!
''')
                else:
                    await dbfunc.setIntValue('hp', 'stats', userid, 100)
                    if stats['level'] > 1:
                        await dbfunc.updateIntValue('level', 'stats', userid, -1)
                    await dbfunc.setIntValue('xp', 'stats', userid, 0)
                    await ctx.send(f'''
**{username}** went into a BIGGG cave to find the boss
Looks like **{username}** found **{bossName}**
Some serious fights are going on
THINGS DOESNT LOOKS GOOD
**{username}** lost fighting
**BETTER LUCK NEXT TIME!**
''')
                    atk_def(ctx)
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Boss(bot))