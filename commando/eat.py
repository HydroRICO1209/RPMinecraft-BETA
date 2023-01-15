from discord.ext import commands
import discord
from progress.stats import *
from progress.mobdrop import *

class Eat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def eat(self, ctx, arg:str):
        try:
            mobdrop = await Mobdrop(ctx)
            stats = await Stats(ctx)
            dbfunc = self.bot.database_handler
            userid = ctx.author.id  
            username = ctx.author.name

            if stats.hp >= 100:
                await ctx.send(f'**{username}**, you want me to force feed you?')
            else:
                if arg == 'pogchop': #5hp
                    if mobdrop.pogchop == 0:
                        await ctx.send(f'**{username}**, you dont have a pogchop')
                    else:
                        await dbfunc.updateIntValue('pogchop', 'mobdrop', userid, -1)
                        await dbfunc.updateIntValue('hp', 'stats', userid, 5)
                        await ctx.send(f'**{username}** ate a pogchop and regen **5HP**')

                elif arg == 'cooked_pogchop': #15hp
                    if mobdrop.cooked_pogchop == 0: 
                        await ctx.send(f'**{username}**, you dont have a cooked_pogchop')
                    else:
                        await dbfunc.updateIntValue('cooked_pogchop', 'mobdrop', userid, -1)
                        await dbfunc.updateIntValue('hp', 'stats', userid, 15)
                        await ctx.send(f'**{username}** ate a cooked_pogchop and regen **15HP**')
                        
                elif arg == 'beef': #20hp
                    if mobdrop.beef == 0:
                        await ctx.send(f'**{username}**,you dont have a beef')
                    else:
                        await dbfunc.updateIntValue('beef', 'mobdrop', userid, -1)
                        await dbfunc.updateIntValue('hp', 'stats', userid, 20)
                        await ctx.send(f'**{username}** ate a beef and regen **20HP**')
                
                elif arg == 'steak': #40hp
                    if mobdrop.steak == 0:
                        await ctx.send(f'**{username}**,you dont have a steak')
                    else:
                        await dbfunc.updateIntValue('steak', 'mobdrop', userid, -1)
                        await dbfunc.updateIntValue('hp', 'stats', userid, 40)
                        await ctx.send(f'**{username}** ate a steak and regen **40HP**')
                        
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Eat(bot))