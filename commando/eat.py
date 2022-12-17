from discord.ext import commands
import discord
from progress.item import *
from progress.stats import *

class Eat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def eat(self, ctx, arg:str):
        try:
            item = Item(ctx)
            stats = Stats(ctx)
            if stats.hp >= 100:
                await ctx.send(f'**{ctx.author.name}**, you want me to force feed you?')
            else:
                if arg == 'pogchop': #5hp
                    if item.pogchop == 0:
                        await ctx.send(f'**{ctx.author.name}**, you dont have a pogchop')
                    else:
                        db[stats.userid + 'pogchop'] = item.pogchop - 1
                        db[stats.userid + 'hp'] = stats.hp + 5
                        await ctx.send(f'**{ctx.author.name}** ate a pogchop and regen **5HP**')
        
                elif arg == 'cooked_pogchop': #15hp
                    if item.cooked_pogchop == 0: 
                        await ctx.send(f'**{ctx.author.name}**, you dont have a cooked_pogchop')
                    else:
                        db[stats.userid + 'cooked_pogchop'] = item.cooked_pogchop - 1
                        db[stats.userid + 'hp'] = stats.hp + 15
                        await ctx.send(f'**{ctx.author.name}** ate a cooked_pogchop and regen **15HP**')
                        
                elif arg == 'beef': #20hp
                    if item.beef == 0:
                        await ctx.send(f'**{ctx.author.name}**,you dont have a beef')
                    else:
                        db[stats.userid + 'beef'] = item.beef - 1
                        db[stats.userid + 'hp'] = stats.hp + 20
                        await ctx.send(f'**{ctx.author.name}** ate a beef and regen **20HP**')

                elif arg == 'steak': #40hp
                    if item.steak == 0:
                        await ctx.send(f'**{ctx.author.name}**,you dont have a steak')
                    else:
                        db[stats.userid + 'steak'] = item.steak - 1
                        db[stats.userid + 'hp'] = stats.hp + 40
                        await ctx.send(f'**{ctx.author.name}** ate a steak and regen **40HP**')
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Eat(bot))