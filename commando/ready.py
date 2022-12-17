from discord.ext import commands
import discord

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['ready'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def rd(self, ctx):
        names = ['hunt', 'mine', 'boss', 'daily']
        res = ''
        for name in names:
            name = self.bot.get_command(name)
            cd = round(name.get_cooldown_retry_after(ctx))
            if cd == 0:
                res += f'<:white_check_mark:918492637428850689> {name}\n'
        if res == '':
            res = 'You must be really active huh'
    
        embed = discord.Embed(
            description= res,
            color = discord.Color.blue())
        embed.set_author(name= f"{ctx.author.display_name}'s ready", 
        icon_url = ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ready(bot))