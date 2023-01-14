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
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            highestArea = await dbfunc.fetchValue('highest_area', 'stats', userid)
            area = await dbfunc.fetchValue('area', 'stats', userid)
            atk = await dbfunc.fetchValue('atk', 'stats', userid)
            defend = await dbfunc.fetchValue('defend', 'stats', userid)
            hp = await dbfunc.fetchValue('hp', 'stats', userid)
            xp = await dbfunc.fetchValue('xp', 'stats', userid)
            level = await dbfunc.fetchValue('level', 'stats', userid)
            
            if higherArea > area:
                await ctx.send('This area doesnt have any boss anymore')
            elif highestArea == area:
                if area == 1:
                    bossName = 'The Mutated Poggy'
                    mobdef = 50
                    mobatk = 15
                    newArea = 2
                elif area == 2:
                    bossName = 'Giant Zompiggy'
                    mobdef = 100
                    mobatk = 25
                    newArea = 3
                elif area == 3:
                    bossName = 'woc eth , enobrennid'
                    mobdef = 200
                    mobatk = 35
                    newArea = 4
                elif area == 4:
                    bossName = 'GIANT SPIDER'
                    mobdef = 500
                    mobatk = 45
                    newArea = 5
                elif area == 5:
                    bossName = 'Wooly Skeleton'
                    mobdef = 800
                    mobatk = 56
                    newArea = 6
                elif area == 6:
                    bossName = 'Skeleton KING'
                    mobdef = 1000
                    mobatk = 70
                    newArea = 7
                elif area == 7:
                    bossName = 'Johnny, THE RAIDER'
                    mobdef = 1500
                    mobatk = 135
                    newArea = 8
                elif area == 8:
                    bossName = 'Elder Guardian'
                    mobdef = 2000
                    mobatk = 300
                    newArea = 8
                elif area == 9:
                    bossName = 'Cheezy Blaze'
                    mobdef = 2000
                    mobatk = 145
                    newArea = 10
                elif area == 10:
                    bossName = 'GIANT MAGMA CUBE'
                    mobdef = 2300
                    mobatk = 175
                    newArea = 11
                elif area == 11:
                    bossName = 'small wither'
                    mobdef = 2500
                    mobatk = 200
                    newArea = 12
                elif area == 13:
                    bossName = 'Silvered Enderman'
                    mobdef = 2800
                    mobatk = 380
                    newArea = 14
                
                mobatktotal = round(mobdef / atk)
                damage = (mobatk - defend) * mobatktotal
                if damage < 0: damage = 0
                newhp = stats.hp - damage
                
                if newhp > 0:
                    await dbfunc.setIntValue('hp', 'stats', userid, newhp)
                    await dbfunc.setIntValue('highest_area', 'stats', userid, newArea)
                    await dbfunc.setIntValue('area', 'stats', userid, newArea)
                    db[userid + 'hp'] = newhp
                    db[userid + 'highestArea'] = newArea
                    db[userid + 'area'] = newArea
                    await ctx.send(f'''
    **{ctx.author.name}** went into a BIGGG cave to find the boss
    Looks like **{ctx.author.name}** found **{bossName}**
    Some serious fights are going on
    LOOKS LIKE **{ctx.author.name}** WINS
    Lost {damage} HP, remaining HP {newhp}/100
    **{ctx.author.name}** went to the NEXT AREA!!!
''')
                else:
                    db[stats.userid + 'hp'] = 100
                    if stats.level > 1:
                        db[stats.userid + 'level'] = stats.level - 1
                        db[stats.userid + 'xp'] = 0
                    else:
                        db[stats.userid + 'xp'] = 0
                    await ctx.send(f'''
**{ctx.author.name}** went into a BIGGG cave to find the boss
Looks like **{ctx.author.name}** found **{bossName}**
Some serious fights are going on
THINGS DOESNT LOOKS GOOD
**{ctx.author.name}** lost fighting
**BETTER LUCK NEXT TIME!**
''')
                    atk_def(ctx)
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Boss(bot))