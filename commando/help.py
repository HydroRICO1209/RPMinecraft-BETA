from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def help(self, ctx):
        embed = discord.Embed(
            description= '''
add `rpm` before any command

:medal:**Statistic Commands**:medal:
`profile`,`inventory`

<:iron_sword:917408207213821972>**Fighting Commands**<:iron_sword:917408207213821972>
`hunt`,`mine`,`boss`

:tools:**Working Commands**:tools:
`craft 1/2`,`eat`,`area`,`cooldown`,`ready`

:hammer_pick:**Under Contrustion Commands(use at your own risk)**:hammer_pick:
`open`

:arrow_right:**Other Commands**:arrow_left:
`ping`
''',
            color = discord.Color.blue())
        embed.set_author(name= 'Commands', 
            icon_url = ctx.author.avatar_url)
        embed.add_field(name='**Link**' ,value='[Offcial server](https://discord.gg/uVJrchkCeA)')
        embed.set_footer(text = 'imagine forgetting command')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))