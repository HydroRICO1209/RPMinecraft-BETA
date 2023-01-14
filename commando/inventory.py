from discord.ext import commands
import discord
from progress.itemlist import *
from progress.my_emote import *

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['i', 'inv'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def inventory(self,ctx):
        try:
            e = My_emote(ctx)
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            

            mobdrop_str = ''
            for mobdrop in itemlist.mobdrop_list:
                e = discord.utils.get(self.bot.emojis, name = mobdrop)
                value = db[userid + items]
                if value > 0:
                    mobdrop_str += f"{e}{items}: {value}\n"

            res2 = ''
            for items in itemss['misc']:
                e = discord.utils.get(self.bot.emojis, name = items)
                value = db[userid + items]
                if value > 0:
                    res2 += f"{e}{items}: {value}\n"

            res3 = ''
            for items in itemss['illegal']:
                e = discord.utils.get(self.bot.emojis, name = items)
                value = db[userid + items]
                if value > 0:
                    res3 += f"{e}{items}: {value}\n"
        
            res4 = ''
            for armor in armors:
                value = db[userid + armor]
        
                if value == 0:
                    res4 += f'No {armor}\n'
                if value == 1:
                    e = discord.utils.get(self.bot.emojis, name = f'pog_{armor}')
                    res4 += f'{e}pog_{armor}\n'
                if value == 2:
                    e = discord.utils.get(self.bot.emojis, name = f'iron_{armor}')
                    res4 += f'{e}iron_{armor}\n'
                if value == 3:
                    e = discord.utils.get(self.bot.emojis, name = f'diamond_{armor}')
                    res4 += f'{e}diamond_{armor}\n'
                if value == 4:
                    e = discord.utils.get(self.bot.emojis, name = f'mw_diamond_{armor}')
                    res4 += f'{e}meaty_wooly_diamond_{armor}\n'
                if value == 5:
                    e = discord.utils.get(self.bot.emojis, name = f'smw_diamond_{armor}')
                    res4 += f'{e}shiny_meaty_wooly_diamond_{armor}\n'
                if value == 6:
                    e = discord.utils.get(self.bot.emojis, name = f'smw_netherite_{armor}')
                    res4 += f'{e}shiny meaty wooly netherite {armor}\n'
                if value == 7:
                    e = discord.utils.get(self.bot.emojis, name = f'msmw_netherite_{armor}')
                    res4 += f'{e}more shiny meaty wooly netherite {armor}\n'
                if value == 69:
                    res4 += '<:beefy_sword:917410854209749023> beefy_sword'

            if res1 == '': res1 = 'None'
            if res2 == '': res2 = 'None'
            if res3 == '': res3 = 'None'
            if res4 == '': res4 = 'None'
    
            embed = discord.Embed(
                color = discord.Color.blue())
            embed.add_field(name = 'Items',value = res1, inline=True)
            embed.add_field(name = 'Misc',value = res2, inline=True)
            embed.add_field(name = 'Illegal',value= res3, inline=True)
            embed.add_field(name = 'Armors & Tools',value= res4, inline=True)
            embed.set_author(name= f"{ctx.author.display_name}'s profile",
            icon_url = ctx.author.avatar.url)
            await ctx.send(embed=embed)
        except KeyError: #error handler
            await ctx.send(f'**{ctx.author.name}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):  
    await bot.add_cog(MyCog(bot))