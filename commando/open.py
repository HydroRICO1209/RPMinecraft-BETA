from discord.ext import commands
import discord, random
from progress.misc import *
from progress.mobdrop import *

class Open(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def open(self, ctx, *, arg: str):
        try:
            misc = await Misc(ctx)
            mobdrop = await Mobdrop(ctx)
            
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            num1 = random.randint(0, 100) #loottype
            num2 = random.randint(0, 100) #lootnum
            
            if arg in ['c', 'common chest', 'common']:
                lootlist = f'**{username}** opened a common chest and got:'
                if misc['common_chest'] > 0: #have the chest
                    await dbfunc.updateIntValue('common_chest', 'misc', userid, -1)
                    common = ['pogchop', 'coal']
                    for loot in common:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        num3 = random.randint(0, 1000)
                        
                        if num1 <= 80: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 1
                            elif num2 <= 90: #20%
                                lootnum = 3
                            elif num2 <= 100: #10%
                                lootnum = 5
                                
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    rare = ['beef', 'iron_ingot', 'emerald']
                    for loot in rare:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #50% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 1
                            elif num2 <= 90: #20%
                                lootnum = 2
                            elif num2 <= 100: #10%
                                lootnum = 3
                                
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                            
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'
    
                    super_rare = ['legendary_chest']
                    for loot in super_rare:
                        if num3 == 69: #1% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            await dbfunc.updateIntValue(loot, 'misc', userid, 1)
                            lootlist += f'\n{my_emote}{loot} x1'

                    await ctx.send(lootlist)
                else:
                    await ctx.send(f'**{username}**, check your inventory maybe???')

            elif arg in ['r', 'rare chest']:
                lootlist = f'**{username}** opened a rare chest and got:'
                if misc['rare_chest'] > 0: #have the chest
                    await dbfunc.updateIntValue('rare_chest', 'misc', userid, -1)
                    common = ['pogchop', 'beef', 'wool', 'coal']
                    for loot in common:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 80: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 3
                            elif num2 <= 90: #20%
                                lootnum = 5
                            elif num2 <= 100: #10%
                                lootnum = 7
                                
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)

                            lootlist += f'\n{my_emote}{loot} x{lootnum}'
            
                    rare = ['emerald', 'iron_ingot', 'common_chest']
                    for loot in rare:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if loot == 'common_chest':
                                lootnum = 1
                            else:
                                if num2 <= 70: #70%
                                    lootnum = 2
                                elif num2 <= 90: #20%
                                    lootnum = 3
                                elif num2 <= 100: #10%
                                    lootnum = 4
                            await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'
    
                    await ctx.send(lootlist)
                else:
                    await ctx.send(f'**{username}**, check your inventory maybe???')
                    
            elif arg in ['s',  'super rare chest']:
                lootlist = f'**{username}** opened a super rare chest and got:'
                if misc['super_rare_chest'] > 0: #have the chest
                    await dbfunc.updateIntValue('super_rare_chest', 'misc', userid, -1)
                    common = ['pogchop', 'beef', 'wool', 'coal', 'iron_ingot']
                    for loot in common:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 5
                            elif num2 <= 90: #20%
                                lootnum = 7
                            elif num2 <= 100: #10%
                                lootnum = 9
                            
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    rare = ['diamond', 'emerald', 'rare_chest']
                    for loot in rare:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if loot == 'rare_chest':
                                lootnum = 1
                            else:
                                if num2 <= 70: #70%
                                    lootnum = 3
                                elif num2 <= 90: #20%
                                    lootnum = 4
                                elif num2 <= 100: #10%
                                    lootnum = 5
                            await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'
                    await ctx.send(lootlist)

                else:
                    await ctx.send(f'**{username}**, check your inventory maybe???')
            
            elif arg in ['e', 'epic chest']:
                lootlist = f'**{username}** opened an epic chest and got:'
                if misc['epic_chest'] > 0: #have the chest
                    await dbfunc.updateIntValue('epic_chest', 'misc', userid, -1)

                    common = ['beef', 'wool', 'coal', 'iron_ingot', 'diamond']
                    for loot in common:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 6
                            elif num2 <= 90: #20%
                                lootnum = 8
                            elif num2 <= 100: #10%
                                lootnum = 10
                            
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    rare = ['blaze_rod', 'emerald', 'netherite_scrap', 'rare_chest']
                    for loot in rare:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 5
                            elif num2 <= 90: #20%
                                lootnum = 7
                            elif num2 <= 100: #10%
                                lootnum = 9
                            
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    super_rare = ['wither_skull']
                    for loot in super_rare:
                        num1 = random.randint(0, 100)
                        if num1 <= 10: #10% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            await dbfunc.updateIntValue(loot, 'mobdrop', userid, 1)
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'
                    await ctx.send(lootlist)

                else:
                    await ctx.send(f'**{username}**, check your inventory maybe???')
                    
            elif arg in ['m', 'mythic chest']:
                if misc['mythic_chest'] > 0: #have the chest
                    lootlist = f'**{username}** opened a mythic chest and got:'
                    await dbfunc.updateIntValue('mythic_chest', 'misc', userid, -1)
                    common = ['beef', 'wool', 'blaze_rod', 'diamond']
                    for loot in common:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 80: #80%
                                lootnum = 10
                            elif num2 <= 95: #15%
                                lootnum = 15
                            elif num2 <= 100: #5%
                                lootnum = 20
                            
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    rare = ['ender_pearl', 'gold', 'wood']
                    for loot in rare:
                        num1 = random.randint(0, 100)
                        num2 = random.randint(0, 100)
                        if num1 <= 50: #80% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            if num2 <= 70: #70%
                                lootnum = 6
                            elif num2 <= 90: #20%
                                lootnum = 8
                            elif num2 <= 100: #10%
                                lootnum = 10
                            
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, lootnum)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, lootnum)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    super_rare = ['wither_skull', 'netherite_scrap']
                    for loot in super_rare:
                        num1 = random.randint(0, 100)
                        if num1 <= 20: #20% drop rate
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            
                            if loot in mobdrop_list:
                                await dbfunc.updateIntValue(loot, 'mobdrop', userid, 1)
                            elif loot in misc_list:
                                await dbfunc.updateIntValue(loot, 'misc', userid, 1)
                                
                            lootlist += f'\n{my_emote}{loot} x{lootnum}'

                    await ctx.send(lootlist)
                else:
                    await ctx.send(f'**{username}**, check your inventory maybe???')
                    
            elif arg in ['l', 'legendary chest']:
                lootlist = f'**{username}** opened a legendary chest and got:'
                if misc['legendary_chest'] > 0: #have the chest
                    await dbfunc.updateIntValue('legendary_chest', 'misc', userid, -1)
                    mobdrop = ['pogchop', 'beef', 'wool', 'map_scrap', 'wither_skull', 'blaze_rod', 'ender_pearl'] #3 random mobdrop x20
                    for _ in range(3):
                        num1 = random.randint(0, 6)
                        loot = mobdrop[num1]
                        my_emote = discord.utils.get(self.bot.emojis, name = loot)
                        if loot in ['map_scrap', 'wither_skull', 'ender_pearl']:
                            await dbfunc.updateIntValue(loot, 'mobdrop', userid, 2)
                            lootlist += f'\n{my_emote}{loot} x2'
                        else:
                            await dbfunc.updateIntValue(loot, 'mobdrop', userid, 20)
                            lootlist += f'\n{my_emote}{loot} x20'
                        
                    ore = ['coal', 'iron_ingot', 'diamond', 'gold_ingot', 'netherite_scrap', 'redstone', 'soul_sand'] #3 random ore x20
                    for _ in range(3):
                        num1 = random.randint(0, 6)
                        loot = ore[num1]
                        my_emote = discord.utils.get(self.bot.emojis, name = loot)
                        if loot in ['netherite_scrap', 'soul_sand']:
                            await dbfunc.updateIntValue(loot, 'misc', userid, 2)
                            lootlist += f'\n{my_emote}{loot} x2'
                        else:
                            await dbfunc.updateIntValue(loot, 'misc', userid, 20)
                            lootlist += f'\n{my_emote}{loot} x20'

                    rare = ['legendary_chest']
                    for loot in rare:
                        num1 = random.randint(0, 100)
                        if num1 <= 69: #69%
                            my_emote = discord.utils.get(self.bot.emojis, name = loot)
                            await dbfunc.updateIntValue('legendary_chest', 'misc', userid, 1)
                            lootlist += f'\n{my_emote}{loot} x1'

                    await ctx.send(lootlist)

                else:
                    await ctx.send(f"**{username}**, the only chest you have is yaw chern's father chest")
            else:
                await ctx.send(f'**{username}**, correct syntax to open common chest -> `rpm open common/c`')
        
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start')

async def setup(bot):
    await bot.add_cog(Open(bot))