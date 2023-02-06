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
            mobdrop_list = itemlist.mobdrop_list
            misc_list = itemlist.misc_list
            farm_list = itemlist.farm_list
            illegal_list = itemlist.illegal_list
            
            #mobdrop
            mobdrop_str = ''
            for mobdrop in itemlist['mobdrop_list']:
                e = discord.utils.get(self.bot.emojis, name = mobdrop)
                value = await dbfunc.fetchValue(mobdrop, 'mobdrop', userid)
                if value != 0:
                    mobdrop_str += f"{e}{mobdrop}: {value}\n"

            #misc
            misc_str = ''
            for misc in itemlist['misc_list']:
                e = discord.utils.get(self.bot.emojis, name = misc)
                value = await dbfunc.fetchValue(misc, 'misc', userid)
                if value != 0:
                    misc_str += f"{e}{misc}: {value}\n"

            #farm
            farm_str = ''
            for farm in itemlist['farm_list']:
                e = discord.utils.get(self.bot.emojis, name = farm)
                value = await dbfunc.fetchValue(farm, 'farm', userid)
                if value != 0:
                    farm_str += f"{e}{farm}: {value}\n"
                    
            #illegal
            illegal_str = ''
            for illegal in itemlist['illegal_list']:
                e = discord.utils.get(self.bot.emojis, name = items)
                value = await dbfunc.fetchValue(illegal, 'illegal', userid)
                if value != 0:
                    illegal_str += f"{e}{items}: {value}\n"

            #armors & sword
            armors_str = ''
            for armor in itemlist['armors']:
                value = await dbfunc.fetchValue(armors, 'armor', userid)
        
                if value == 0:
                    armors_str += f'No {armor}\n'
                if value == 1:
                    e = discord.utils.get(self.bot.emojis, name = f'pog_{armor}')
                    armors_str += f'{e}pog_{armor}\n'
                if value == 2:
                    e = discord.utils.get(self.bot.emojis, name = f'iron_{armor}')
                    armors_str += f'{e}iron_{armor}\n'
                if value == 3:
                    e = discord.utils.get(self.bot.emojis, name = f'diamond_{armor}')
                    armors_str += f'{e}diamond_{armor}\n'
                if value == 4:
                    e = discord.utils.get(self.bot.emojis, name = f'mw_diamond_{armor}')
                    armors_str += f'{e}meaty_wooly_diamond_{armor}\n'
                if value == 5:
                    e = discord.utils.get(self.bot.emojis, name = f'smw_diamond_{armor}')
                    armors_str += f'{e}shiny_meaty_wooly_diamond_{armor}\n'
                if value == 6:
                    e = discord.utils.get(self.bot.emojis, name = f'smw_netherite_{armor}')
                    armors_str += f'{e}shiny meaty wooly netherite {armor}\n'
                if value == 7:
                    e = discord.utils.get(self.bot.emojis, name = f'msmw_netherite_{armor}')
                    armors_str += f'{e}more shiny meaty wooly netherite {armor}\n'
                if value == 69:
                    armors_str += '<:beefy_sword:917410854209749023> beefy_sword'

            if mobdrop_str == '': mobdrop_str = 'None'
            if misc_str == '': misc_str = 'None'
            if farm_str == '': farm_str = 'None'
            if illegal_str == '': illegal_str = 'None'
            if armors_str == '': armors_str = 'None'
    
            embed = discord.Embed(
                color = discord.Color.blue())
            embed.add_field(name = 'Items',value = mobdrop_str, inline=True)
            embed.add_field(name = 'Misc',value = misc_str, inline=True)
            embed.add_field(name = 'Farm',value = farm_str, inline=True)
            embed.add_field(name = 'Illegal',value= illegal_str, inline=True)
            embed.add_field(name = 'Armors & Tools',value= armors_str, inline=True)
            embed.set_author(name= f"{username}'s profile",
            icon_url = ctx.author.avatar.url)
            await ctx.send(embed=embed)
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start`')

async def setup(bot):  
    await bot.add_cog(MyCog(bot))