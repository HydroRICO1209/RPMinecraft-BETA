from discord.ext import commands
import discord

class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['cooldown'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def cd(self, ctx):
        names = ['hunt', 'mine', 'boss','daily']
        res = ''
        for name in names:
            name = self.bot.get_command(name)
            seccd = round(name.get_cooldown_retry_after(ctx))
            mincd = 0
            hrcd = 0
            rseccd = 0
            rmincd = 0

            if seccd > 59:  
                rseccd = int(seccd % 60)
                mincd = int((seccd - rseccd) / 60)
                if mincd > 59:
                    rmincd = int(mincd % 60)
                    hrcd = int((mincd - rmincd) / 60)
            else:
                rseccd = seccd

            if seccd == 0 and rseccd == 0 and mincd == 0 and rmincd == 0 and hrcd == 0:
                res += f':white_check_mark: {name}\n' 
            else:
                res += f'<a:spinning_clock:923476086493429760> {name}: **{hrcd}h {rmincd}m {rseccd}s**\n'

        embed = discord.Embed(
            description= res,
            color = discord.Color.blue())
        embed.set_author(name= f"{ctx.author.display_name}'s cooldown", 
        icon_url = ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Cooldown(bot))