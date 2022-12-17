from discord.ext import commands
import discord
from progress.itemlist import itemss
from progress.itemlist import armors
from progress.itemlist import statss
from progress.my_emote import *
from replit import db

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases =['start'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def update(self, ctx):
        userid = str(ctx.author.id)
        my_emote = My_emote(ctx)
    
        for key, value in itemss.items():
            for item in value:
                if f'{userid}{item}' not in db:
                    db[f'{userid}{item}'] = 0
                else:
                    continue
                    
        for armor in armors:  
            if f'{userid}{armor}' not in db:
                db[f'{userid}{armor}'] = 0
            else:  
                continue
                
        for stats in statss:
            if f'{userid}{stats}' not in db:
                if stats == 'xp':
                    db[f'{userid}{stats}'] = 0
                elif stats == 'hp':
                    db[f'{userid}{stats}'] = 100
                else:
                    db[f'{userid}{stats}'] = 1
            else:
                continue

        db[f'{userid}farmlist'] = [[None,0],[]]
    
        embed = discord.Embed(
            title = f'**Welcome to RPMinecraft, {ctx.author.name}**',
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