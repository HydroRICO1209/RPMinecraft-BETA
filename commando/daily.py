from discord.ext import commands
import discord
from replit import db

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        try:
            userid = str(ctx.author.id)
            db[userid + 'cooked_pogchop'] += 5
            db[userid + 'steak'] += 5
            await ctx.send(f'**{ctx.author.name}** has claimed daily kit')
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):
    await bot.add_cog(Daily(bot))