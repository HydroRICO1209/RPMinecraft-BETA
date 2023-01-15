from discord.ext import commands
import discord
from progress.stats import *
from progress.my_emote import *

class Profile(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases =['p'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def profile(self, ctx): 
        try:
            stats = await Stats(ctx)
            my_emote = My_emote(ctx)
            
            embed = discord.Embed(
                description = f'''
    **PROGRESS**
    **LEVEL**: **{stats.level}**({stats.xp}/{stats.maxxp})
    **AREA**: **{stats.area}** (Max: **{stats.highestArea}**)
    **STATS**
    {my_emote.earmorfull}**DEF**: {stats.defend}
    <:iron_sword:917408207213821972>**ATK**: {stats.atk}
    {my_emote.eheartfull}**HP**: {stats.hp}/100
    ''', 
                color = discord.Color.blue())
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.set_author(name= f"{ctx.author.display_name}'s profile", 
            icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Profile(bot))