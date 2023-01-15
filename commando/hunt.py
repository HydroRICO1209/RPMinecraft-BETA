from discord.ext import commands
import discord, random
from progress.my_emote import *
from progress.stats import *
from progress.mobdrop import *

class Hunt(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def hunt(self, ctx):
        try:
            emote = My_emote(ctx)
            stats = await Stats(ctx)
            mobdrop = await Mobdrop(ctx)
            
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            num1 = random.randint(0, 100) #mob type
            num2 = random.randint(0, 100) #drop rate
            num3 = random.randint(0, 100) #chest drop rate
            num4 = random.randint(0, 1000) #chest type
            loot = 'nothing'
            chesttype = None
    
            if stats.area == 1:
                mobxp = 5
                if num1 <= 50:
                    mobselected = 'pig'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'angrypig'
                    mobdef = 10
                    mobatk = 1
                elif num1 <= 100:
                    mobselected = 'zombie'
                    mobdef = 15
                    mobatk = 2
    
            elif stats.area == 2:
                mobxp = 10
                if num1 <= 50:
                    mobselected = 'pig'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'angrypig'
                    mobdef = 25
                    mobatk = 7
                elif num1 <= 100:
                    mobselected = 'zombie'
                    mobdef = 50
                    mobatk = 10
    
            elif stats.area == 3:
                mobxp = 15
                if num1 <= 50:
                    mobselected = 'cow'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'angrycow'
                    mobdef = 60
                    mobatk = 30
                elif num1 <= 100:
                    mobselected = 'spider'
                    mobdef = 30
                    mobatk = 40
    
            elif stats.area == 4:
                mobxp = 20
                if num1 <= 50:
                    mobselected = 'cow'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'angrycow'
                    mobdef = 30
                    mobatk = 40
                elif num1 <= 100:
                    mobselected = 'spider'
                    mobdef = 37
                    mobatk = 45
    
            elif stats.area == 5:
                mobxp = 25
                if num1 <= 50:
                    mobselected = 'sheep'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'angrysheep'
                    mobdef = 50
                    mobatk = 55
                elif num1 <= 100:
                    mobselected = 'skeleton'
                    mobdef = 53
                    mobatk = 60
    
            elif stats.area == 6:
                mobxp = 30
                if num1 <= 50:
                    mobselected = 'sheep'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'angrysheep'
                    mobdef = 170
                    mobatk = 69
                elif num1 <= 100:
                    mobselected = 'skeleton'
                    mobdef = 200
                    mobatk = 73
    
            elif stats.area == 7:
                mobxp = 35
                if num1 <= 50:
                    mobselected = 'broke zombie villager'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'pillager'
                    mobdef = 110
                    mobatk = 80
                elif num1 <= 100:
                    mobselected = 'vindicator'
                    mobdef = 120
                    mobatk = 130

            elif stats.area == 8:
                mobxp = 40
                if num1 <= 50:
                    mobselected = 'broke zombie villager'
                    mobdef = 1
                    mobatk = 0
                elif num1 <= 75:
                    mobselected = 'pillager'
                    mobdef = 125
                    mobatk = 160
                elif num1 <= 100:
                    mobselected = 'vindicator'
                    mobdef = 130
                    mobatk = 175
            
            elif stats.area == 9:
                mobxp = 45
                if num1 <= 50:
                    mobselected = 'witherskeleton'
                    mobdef = 1240
                    mobatk = 190
                elif num1 <= 75:
                    mobselected = 'magma'
                    mobdef = 240
                    mobatk = 195
                elif num1 <= 100:
                    mobselected = 'blaze'
                    mobdef = 210
                    mobatk = 175
    
            elif stats.area == 10:
                mobxp = 50
                if num1 <= 50:
                    mobselected = 'witherskeleton'
                    mobdef = 240
                    mobatk = 215
                elif num1 <= 75:
                    mobselected = 'magma'
                    mobdef = 240
                    mobatk = 230
                elif num1 <= 100:
                    mobselected = 'blaze'
                    mobdef = 210
                    mobatk = 190
                
            elif stats.area == 11:
                mobxp = 55
                if num1 <= 50:
                    mobselected = 'ghast'
                    mobdef = 290
                    mobatk = 237
                elif num1 <= 75:
                    mobselected = 'zombiepiglin'
                    mobdef = 330
                    mobatk = 250
                elif num1 <= 100:
                    mobselected = 'iron armored skeleton'
                    mobdef = 300
                    mobatk = 270
    
            elif stats.area == 12:
                mobxp = 60
                if num1 <= 50:
                    mobselected = 'ghast'
                    mobdef = 330
                    mobatk = 310
                elif num1 <= 75:
                    mobselected = 'zombiepiglin'
                    mobdef = 300
                    mobatk = 321
                elif num1 <= 100:
                    mobselected = 'iron armored skeleton'
                    mobdef = 300
                    mobatk = 333
            
            elif stats.area == 13:
                mobxp = 65
                if num1 <= 50:
                    mobselected = 'enderman'
                    mobdef = 370
                    mobatk = 310
                elif num1 <= 75:
                    mobselected = 'silverfish'
                    mobdef = 350
                    mobatk = 340
                elif num1 <= 100:
                    mobselected = 'endermite'
                    mobdef = 340
                    mobatk = 290
        
            elif stats.area == 14:
                mobxp = 70
                if num1 <= 50:
                    mobselected = 'enderman'
                    mobdef = 390
                    mobatk = 350
                elif num1 <= 75:
                    mobselected = 'silverfish'
                    mobdef = 380
                    mobatk = 345
                elif num1 <= 100:
                    mobselected = 'endermite'
                    mobdef = 370
                    mobatk = 320
    
            if mobselected in ['pig', 'angrypig']:
                if num2 <= 25:
                    loot = 'nothing'
                elif num2 <= 75:
                    loot = '5 pogchops'
                    await dbfunc.updateIntValue('pogchop', 'mobdrop', userid, 5)
                    
                elif num2 <= 100:
                    loot = '10 pogchops'
                    await dbfunc.updateIntValue('pogchop', 'mobdrop', userid, 10)
    
            elif mobselected in ['cow', 'angrycow']:
                if num2 <= 25:
                    loot = 'nothing'
                elif num2 <= 75:
                    loot = '5 beefs'
                    await dbfunc.updateIntValue('beef', 'mobdrop', userid, 5)
                elif num2 <= 100:
                    loot = '10 beefs'
                    await dbfunc.updateIntValue('beef', 'mobdrop', userid, 10)
                
            elif mobselected in ['sheep', 'angrysheep']:
                if num2 <= 75:
                    loot = 'nothing'
                elif num2 <= 95:
                    loot = '1 wool'
                    await dbfunc.updateIntValue('wool', 'mobdrop', userid, 1)
                elif num2 <= 100:
                    loot = '2 wools'
                    await dbfunc.updateIntValue('wool', 'mobdrop', userid, 2)
    
            elif mobselected == 'broke zombie villager':
                if num2 <= 95:
                    loot = 'nothing'
                elif num2 <= 100:
                    loot = '1 map scrap'
                    await dbfunc.updateIntValue('map_scrap', 'mobdrop', userid, 1)
            
            elif mobselected == 'witherskeleton':
                if num2 <= 50:
                    loot = 'nothing'
                elif num2 <= 75:
                    loot = '1 coal'
                    await dbfunc.updateIntValue('coal', 'misc', userid, 1)
                elif num2 <= 100:
                    loot = '1 wither skull'
                    await dbfunc.updateIntValue('wither_skull', 'mobdrop', userid, 11)
    
            elif mobselected == 'blaze':
                if num2 <= 75:
                    loot = 'nothing'
                elif num2 <= 100:
                    loot = '1 blaze rod' 
                    await dbfunc.updateIntValue('blaze_rod', 'mobdrop', userid, 1)
            
            elif mobselected == 'ghast':
                if num2 <= 95:
                    loot = 'nothing'
                elif num2 <= 100:
                    loot = '1 soul sand'
                    await dbfunc.updateIntValue('soul_sand', 'misc', userid, 1)
                    
            elif mobselected == 'enderman':
                if num2 <= 75:
                    loot = 'nothing'
                elif num2 <= 100:
                    loot = '1 ender pearl' 
                    await dbfunc.updateIntValue('ender_pearl', 'mobdrop', userid, 10)
    
            #calculate damage
            mobatktotal = mobdef / stats.atk
            damage = (mobatk - stats.defend) * round(mobatktotal)
            if damage < 0: damage = 0
            newhp = stats.hp - damage
            await dbfunc.setIntValue('hp', 'stats', userid, newhp)
    
            #chestdrop
            if num3 <= 10:
                if num4 <= 750: 
                    chesttype = 'common_chest' #75%
                    echest = emote.ecommon_chest
                elif num4 <= 900: 
                    chesttype = 'rare_chest' #15%
                    echest = emote.erare_chest
                elif num4 <= 955: 
                    chesttype = 'super_rare_chest' #5.5%
                    echest = emote.esuper_rare_chest
                elif num4 <= 975:
                    chesttype = 'epic_chest' #2%
                    echest = emote.eepic_chest
                elif num4 <= 990:
                    chesttype = 'mythic_chest' #1.5%
                    echest = emote.emythic_chest
                elif num4 <= 1000:
                    chesttype = 'legendary_chest' #1%
                    echest = emote.elegendary_chest
    
            if newhp > 0: #successfully killed mob
                await ctx.send(f'''
    **{username}** found and killed **{mobselected}**
    Lost {damage} HP, remaining HP is {newhp}/100
    Earned {mobxp} XP and got **{loot}**''')
                newxp = mobxp + stats.xp
                maxxp = stats.level * 200
                if newxp > maxxp: #upgradable
                    newxp = newxp - maxxp
                    await dbfunc.updateIntValue('level', 'stats', userid, 1)
                    await dbfunc.setIntValue('xp', 'stats', userid, newxp)
                    atk_def(ctx)
                    await ctx.send(f'**{username}** just up a level!')
                else: 
                    await dbfunc.setIntValue('xp', 'stats', userid, newxp)
    
                if chesttype is not None: #chest
                    await dbfunc.updateIntValue(chesttype, 'misc', userid, 1)
                    await ctx.send(f'**{username}** got 1 {chesttype} {echest}')

            else:
                await dbfunc.updateIntValue('hp', 'stats', userid, 100)
                await ctx.send(f'**{username}** died found a **{mobselected}**, but lost fighting\nRoses are red and violets are blue, you just died and lost some levels too')
                await dbfunc.updateIntValue('level', 'stats', userid, -1)
                await dbfunc.setIntValue('xp', 'stats', userid, 0)
    
            return damage, loot
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Hunt(bot))