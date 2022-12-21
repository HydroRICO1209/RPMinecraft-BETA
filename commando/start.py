from discord.ext import commands
import discord
from progress.my_emote import *

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases =['start'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def update(self, ctx):
        username = ctx.author.name
        userid = ctx.author.id
        my_emote = My_emote(ctx)
        created = await self.bot.db.fetch('SELECT * FROM stats WHERE playerid = $1', userid)
        
        if created == []:
            #armors
            await self.bot.db.execute('''
INSERT INTO armors (playerid, helmet, chestplate, leggings, boots, sword)
VALUES ($1, 0, 0, 0, 0, 0)
''', userid)
            
            #farm
            await self.bot.db.execute('''
INSERT INTO farm (playerid, small_sapling, medium_sapling, large_sapling, apple, wheat_seeds, wheat, potato, poisonous_potato, carrot, beetroot_seeds, beetroot, cleansed_water_bucket. cleansed_dirt)
VALUES ($1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
''', userid)
            
            #farmlist
            await self.bot.db.execute('''
INSERT INTO farmlist (playerid, slot1, slot1time, slot2, slot2time, slot3, slot3time)
VALUES ($1, 'locked', 999999, 'locked', 999999, 'locked', 999999)
''', userid)
            
            #misc
            await self.bot.db.execute('''
INSERT INTO misc (playerid, emerald, cobble, coal, iron_ingot, diamond, gold_ingot, netherite_scrap, netherite_ingot, redstone, soul_sand, wood, bed, common_chest, rare_chest	super_rare_chest, epic_chest, mythic_chest, legendary_chest)
VALUES ($1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
''', userid)
            
            #mobdrop
            await self.bot.db.execute('''
INSERT INTO mobdrop (playerid, pogchop, cooked_pogchop, beef, steak, wool, map_scrap, map, wither_skull, blaze_rod, blaze_powder, ender_pearl, eye_of_ender)
VALUES ($1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
''', userid)

            #stats
            await self.bot.db.execute('''
INSERT INTO stats (playerid, hp, level, highest_area, atk, defend, xp, area, vote_count)
VALUES ($1, 100, 1, 1, 1, 1, 1, 0, 1, 0)
''', userid)
    
        embed = discord.Embed(
            title = f'**Welcome to RPMinecraft, {username}**',
            description = f'''
    This is a minecraft based rpg bot. You need to **hunt for mobdrops**, **defeat bosses** to get to **higher areas**. There is **14 areas** in total.
    
    ***__HOW TO PLAY???__***

    Gains **XP & mobdrops** through {my_emote.eis} **hunting**, but make sure to {my_emote.esteak}** consume food** when your {my_emote.eheartfull} **remaining HP is low**, you will lose **levels** if you die.  
    
    ***__BOSSES & AREAS???__***

    **Craft {my_emote.eic} armors & {my_emote.eis} sword** and you are ready to go (*hopefully*)!
    You will find **new mobs** if and only if you **defeated the boss**.

    __**MORE**__

    **Explore more commands** with **`help`**! There is always more to do than just hunting!
    Make sure to vote for this bot every 12 hours with `vote` to get more rewards
    ''',
            color = discord.Color.blue())
        embed.set_author(name= 'Commands', 
            icon_url = ctx.author.avatar.url)
        embed.set_footer(text = 'HAVE FUN! -HydroRICO1209')
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Start(bot))