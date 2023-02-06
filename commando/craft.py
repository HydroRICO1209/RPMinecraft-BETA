from discord.ext import commands
import discord
from progress.stats import *
from progress.misc import *
from progress.mobdrop import *
from progress.my_emote import *
from progress.atk_def import *

class Craft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def craft(self, ctx, *, arg: str):
        try:
            stats = await Stats(ctx)
            misc = await Misc(ctx)
            mobdrop = await Mobdrop(ctx)
            e = My_emote(ctx)
            dbfunc = self.bot.database_handler
            userid = ctx.author.id
            username = ctx.author.name
            
            if arg == '1':
                embed = discord.Embed(
                    description= f'''
    {e.eph} `pog helmet` ↦ 50 {e.epogchop} + 50 {e.ecoal}
    {e.epc} `pog chestplate` ↦ 80 {e.epogchop} + 80 {e.ecoal}
    {e.epl} `pog leggings` ↦ 70 {e.epogchop} + 70 {e.ecoal}
    {e.epb} `pog boots` ↦ 40 {e.epogchop} + 40 {e.ecoal}
    {e.eps} `pog sword` ↦ 20 {e.epogchop} + 20 {e.ecoal}
    {e.ebs} `beefy sword` ↦ 20 {e.ebeef}
    
    {e.eih} `iron helmet` ↦ 50 {e.eiron_ingot}
    {e.eic} `iron chestplate` ↦ 80 {e.eiron_ingot}
    {e.eil} `iron leggings` ↦ 70 {e.eiron_ingot}
    {e.eib} `iron boots` ↦ 40 {e.eiron_ingot}
    {e.eis} `iron sword` ↦ 20 {e.eiron_ingot}
    
    {e.edh} `diamond helmet` ↦ 50 {e.ediamond}
    {e.edc} `diamond chestplate` ↦ 80 {e.ediamond}
    {e.edl} `diamond leggings` ↦ 70 {e.ediamond}
    {e.edb} `diamond boots` ↦  40 {e.ediamond}
    {e.eds} `diamond sword` ↦ 20 {e.ediamond}
''',
                    color = discord.Color.blue())
                embed.set_author(name= 'Recipes(Page 1)',
                icon_url = ctx.author.avatar.url)
                embed.set_footer(text = 'imagine forgetting recipes')
                await ctx.send(embed=embed)
    
            elif arg == '2':
                embed = discord.Embed(
                    description= f'''
    {e.emwdh} `meaty wooly diamond helmet` ↦ 1 {e.edh} + 50 {e.epogchop} + 50 {e.ebeef} + 50 {e.ewool}
    {e.emwdc} `meaty wooly diamond chestplate` ↦ 1 {e.edc} + 80 {e.epogchop} + 80 {e.ebeef} + 80 {e.ewool}
    {e.emwdl} `meaty wooly diamond leggings` ↦ 1 {e.edl} + 70 {e.epogchop} + 70 {e.ebeef} + 70 {e.ewool}
    {e.emwdb} `meaty wooly diamond boots` ↦ 1 {e.edb} + 40 {e.epogchop} + 40 {e.ebeef} + 40 {e.ewool}
    {e.emwds} `meaty wooly diamond sword` ↦ 1 {e.eds} + 20 {e.epogchop} + 20 {e.ebeef} + 20 {e.ewool}
    
    {e.esmwdh} `shiny meaty wooly diamond helmet` ↦ 1 {e.emwdh} 50 + {e.egold_ingot}
    {e.esmwdc} `shiny meaty wooly diamond chestplate` ↦ 1 {e.emwdc} +  80 {e.egold_ingot}
    {e.esmwdl} `shiny meaty wooly diamond leggings` ↦ 1 {e.emwdl} + 70 {e.egold_ingot}
    {e.esmwdb} `shiny meaty wooly diamond boots` ↦ 1 {e.emwdb} + 40 {e.egold_ingot}
    {e.esmwds} `shiny meaty wooly diamond sword` ↦ 1 {e.emwds} + 20 {e.egold_ingot}
    
    {e.esmwnh} `shiny meaty wooly netherite helmet` ↦ 1 {e.esmwdh} + 1 {e.enetherite_ingot}
    {e.esmwnc} `shiny meaty wooly netherite chestplate` ↦ 1 {e.esmwdc} + 1 {e.enetherite_ingot}
    {e.esmwnl} `shiny meaty wooly netherite leggings` ↦ 1 {e.esmwdl} + 1 {e.enetherite_ingot}
    {e.esmwnb} `shiny meaty wooly netherite boots` ↦ 1 {e.esmwdb} + 1 {e.enetherite_ingot}
    {e.esmwns} `shiny meaty wooly netherite sword` ↦ 1 {e.esmwds} + 1 {e.enetherite_ingot}
    
    {e.emsmwnh} `more shiny meaty wooly netherite helmet` ↦ 1 {e.esmwnh} + 50 {e.eredstone}
    {e.emsmwnc} `more shiny meaty wooly netherite chestplate` ↦ 1 {e.esmwnc} + 80 {e.eredstone}
    {e.emsmwnl} `more shiny meaty wooly netherite leggings` ↦ 1 {e.esmwnl} + 70 {e.eredstone}
    {e.emsmwnb} `more shiny meaty wooly netherite boots` ↦ 1 {e.esmwnb} + 40 {e.eredstone}
    {e.emsmwns} `more shiny meaty wooly netherite sword` ↦ 1 {e.esmwns} + 20 {e.eredstone}
''',
                    color = discord.Color.blue())
                embed.set_author(name= 'Recipes(Page 2)',
                icon_url = ctx.author.avatar.url)
                embed.set_footer(text = 'imagine forgetting recipes')
                await ctx.send(embed=embed)
    
            elif arg == '3':
                embed = discord.Embed(
                    description= f'''
    {e.ecooked_pogchop} `cooked_pogchop` ↦ 8 {e.epogchop} + 1 {e.ecoal}
    {e.esteak} `steak` ↦ 8 {e.ebeef} + 1 {e.ecoal}
    {e.ebed} `bed` ↦ 3 {e.ewood} + 3 {e.ewool}
    {e.eblaze_powder} `blaze_powder`x2 ↦ 1 {e.eblaze_rod}
    {e.emap} `map` ↦ 5 {e.emap_scrap}
    {e.eeoe} `eye_of_ender` ↦ 1 {e.eender_pearl} + 1 {e.eblaze_powder}
''',
                    color = discord.Color.blue())
                embed.set_author(name= 'Recipes(Page 3)',
                icon_url = ctx.author.avatar.url)
                embed.set_footer(text = 'imagine forgetting recipes')
                await ctx.send(embed=embed)
    
            elif arg == 'pog helmet':
                if stats.helmet == 1:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 50 and misc.coal >= 50:
                    await dbfunc.updateIntValue('pogchop', 'mobdrop', userid, -50)
                    await dbfunc.updateIntValue('coal', 'misc', userid, -50)
                    await dbfunc.setIntValue('helmet', 'armor', userid, 1)
                    await ctx.send(f'**{username}**, poghelmet is crafted')
                else:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchops** and **{misc.coal} coals**')
                atk_def(ctx)
    
            elif arg == 'pog chestplate':
                if stats.chestplate == 1:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 80 and misc.coal >= 80:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 80
                    db[stats.userid + 'coal'] = misc.coal - 80
                    db[stats.userid + 'chestplate'] = 1
                    await ctx.send(f'**{username}**, pog chestplate is crafted')
                else:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchops** and **{misc.coal} coals**')
                atk_def(ctx)
    
            elif arg == 'pog leggings':
                if stats.leggings == 1:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 70 and misc.coal >= 70:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 70
                    db[stats.userid + 'coal'] = misc.coal - 70
                    db[stats.userid + 'leggings'] = 1
                    await ctx.send(f'**{username}**, pog leggings is crafted')
                else:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchops** and **{misc.coal} coals**')
                atk_def(ctx)
    
            elif arg == 'pog boots':
                if stats.boots == 1:
                    await ctx.send('You will regret, check your inv :D')
                if mobdrop.pogchop >= 40 and misc.coal >= 40:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 40
                    db[stats.userid + 'coal'] = misc.coal - 40
                    db[stats.userid + 'boots'] = 1
                    await ctx.send(f'**{username}**, pog boots is crafted')
                else:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchops** and **{misc.coal} coals**')
                atk_def(ctx)
    
            elif arg == 'pog sword':
                if stats.sword == 1:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 20 and misc.coal >= 20:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 20
                    db[stats.userid + 'coal'] = misc.coal - 20
                    db[stats.userid + 'sword'] = 1
                    await ctx.send(f'**{username}**, pog sword is crafted')
                else:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchops** and **{misc.coal} coals**')
                atk_def(ctx)
    
            elif arg == 'beefy sword':
                if stats.sword == 69:
                    await ctx.send('You will regret, check your inv :D')
                elif item.beef >= 20:
                    db[stats.userid + 'beef'] = db[stats.userid + 'beef'] - 20
                    db[stats.userid + 'sword'] = 69
                    await ctx.send(f'**{username}**, beefy sword is crafted')
                else:
                    await ctx.send(f'You only have **{item.beef} beefs**')
                atk_def(ctx)
    
            elif arg == 'iron helmet':
                if stats.helmet == 2:
                    await ctx.send('You will regret, check your inv :D')
                elif item.iron_ingot >= 50:
                    db[stats.userid + 'iron_ingot'] = item.iron_ingot - 50
                    db[stats.userid + 'helmet'] = 2
                    await ctx.send(f'**{username}**, iron helmet is crafted')
                elif item.iron_ingot < 50:
                    await ctx.send(f'You only have **{item.iron_ingot} iron_ingot**')
                atk_def(ctx)
    
            elif arg == 'iron chestplate':
                if stats.chestplate == 2:
                    await ctx.send('You will regret, check your inv :D')
                elif item.iron_ingot >= 80:
                    db[stats.userid + 'iron_ingot'] = item.iron_ingot - 80
                    db[stats.userid + 'chestplate'] = 2
                    await ctx.send(f'**{username}**,iron chestplate is crafted')
                elif item.iron_ingot < 80:
                    await ctx.send(f'You only have **{item.iron_ingot} iron_ingot**')
                atk_def(ctx)
    
            elif arg == 'iron leggings':
                if stats.leggings == 2:
                    await ctx.send('You will regret, check your inv :D')
                elif item.iron_ingot >= 70:
                    db[stats.userid + 'iron_ingot'] = item.iron_ingot - 70
                    db[stats.userid + 'leggings'] = 2
                    await ctx.send(f'**{username}**, iron leggings is crafted')
                elif item.iron_ingot < 70:
                    await ctx.send(f'You only have **{item.iron_ingot} iron_ingot**')
                atk_def(ctx)
    
            elif arg == 'iron boots':
                if stats.boots == 2:
                    await ctx.send('You will regret, check your inv :D')
                elif item.iron_ingot >= 40:
                    db[stats.userid + 'iron_ingot'] = item.iron_ingot - 40
                    db[stats.userid + 'boots'] = 2
                    await ctx.send(f'**{username}**, iron boots is crafted')
                elif item.iron_ingot < 40:
                    await ctx.send(f'You only have **{item.iron_ingot} iron_ingot**')
                atk_def(ctx)
    
            elif arg == 'iron sword':
                if stats.sword == 2:
                    await ctx.send('You will regret, check your inv :D')
                elif item.iron_ingot >= 20:
                    db[stats.userid + 'iron_ingot'] = item.iron_ingot - 20
                    db[stats.userid + 'sword'] = 2
                    await ctx.send(f'**{username}**, iron sword is crafted')
                elif item.iron_ingot < 20:
                    await ctx.send(f'You only have **{item.iron_ingot} iron_ingot**')
                atk_def(ctx)
    
            elif arg == 'diamond helmet':
                if stats.helmet == 3:
                    await ctx.send('You will regret, check your inv :D')
                elif item.diamond >= 50:
                    db[stats.userid + 'diamond'] = item.diamond - 50
                    db[stats.userid + 'helmet'] = 3
                    await ctx.send(f'**{username}**, diamond helmet is crafted')
                elif item.diamond < 50:
                    await ctx.send(f'You only have **{item.diamond} diamond**')
                atk_def(ctx)
    
            elif arg == 'diamond chestplate':
                if stats.chestplate == 3:
                    await ctx.send('You will regret, check your inv :D')
                elif item.diamond >= 80:
                    db[stats.userid + 'diamond'] = item.diamond - 80
                    db[stats.userid + 'chestplate'] = 3
                    await ctx.send(f'**{username}**, diamond chestplate is crafted')
                elif item.diamond < 80:
                    await ctx.send(f'You only have **{item.diamond} diamond**')
                atk_def(ctx)
    
            elif arg == 'diamond leggings':
                if stats.leggings == 3:
                    await ctx.send('You will regret, check your inv :D')
                elif item.diamond >= 70:
                    db[stats.userid + 'diamond'] = item.diamond - 70
                    db[stats.userid + 'leggings'] = 3
                    await ctx.send(f'**{username}**, diamond leggings is crafted')
                elif item.diamond < 70:
                    await ctx.send(f'You only have **{item.diamond} diamond**')
                atk_def(ctx)
            
            elif arg == 'diamond boots':
                if stats.boots == 3:
                    await ctx.send('You will regret, check your inv :D')
                elif item.diamond >= 40:
                    db[stats.userid + 'diamond'] = item.diamond - 40
                    db[stats.userid + 'boots'] = 3
                    await ctx.send(f'**{username}**, diamond boots is crafted')
                elif item.diamond < 40:
                    await ctx.send(f'You only have **{item.diamond} diamond**')
                atk_def(ctx)
    
            elif arg == 'diamond sword':
                if stats.sword == 3:
                    await ctx.send('You will regret, check your inv :D')
                elif item.diamond >= 20:
                    db[stats.userid + 'diamond'] = item.diamond - 20
                    db[stats.userid + 'sword'] = 3
                    await ctx.send(f'**{username}**, diamond sword is crafted')
                elif item.diamond < 20:
                    await ctx.send(f'You only have **{item.diamond} diamond**')
                atk_def(ctx)
    
            elif arg == 'meaty wooly diamond helmet':
                if stats.helmet == 4:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 40 and item.beef >= 40 and item.wool >= 40 and stats.helmet == 3:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 40
                    db[stats.userid + 'beef'] = item.beef - 40
                    db[stats.userid + 'wool'] = item.wool - 40
                    db[stats.userid + 'helmet'] = 4
                    await ctx.send(f'**{username}**, meaty wooly diamond helmet is crafted')
                elif mobdrop.pogchop < 40:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchop**')
                elif item.beef < 40:
                    await ctx.send(f'You only have **{item.beef} beef**')
                elif item.wool < 40:
                    await ctx.send(f'You only have **{item.wool} wool**')
                elif stats.helmet != 3:
                    await ctx.send(f'You dont have a **diamond helmet**')
                atk_def(ctx)
    
            elif arg == 'meaty wooly diamond chestplate':
                if stats.chestplate == 4:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 80 and item.beef >= 80 and item.wool >= 80 and stats.chestplate == 3:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 80
                    db[stats.userid + 'beef'] = item.beef - 80
                    db[stats.userid + 'wool'] = item.wool - 80
                    db[stats.userid + 'chestplate'] = 4
                    await ctx.send(f'**{username}**, meaty wooly diamond chestplate is crafted')
                elif mobdrop.pogchop < 80:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchop**')
                elif item.beef < 80:
                    await ctx.send(f'You only have **{item.beef} beef**')
                elif item.wool < 80:
                    await ctx.send(f'You only have **{item.wool} wool**')
                elif stats.chestplate != 3:
                    await ctx.send(f'You dont have a **diamond chestplate**')
                atk_def(ctx)
    
            elif arg == 'meaty wooly diamond leggings':
                if stats.leggings == 4:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 70 and item.beef >= 70 and item.wool >= 70 and stats.leggings == 3:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 70
                    db[stats.userid + 'beef'] = item.beef - 70
                    db[stats.userid + 'wool'] = item.wool - 70
                    db[stats.userid + 'leggings'] = 4
                    await ctx.send(f'**{username}**, meaty wooly diamond leggings is crafted')
                elif mobdrop.pogchop < 70:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchop**')
                elif item.beef < 70:
                    await ctx.send(f'You only have **{item.beef} beef**')
                elif item.wool < 70:
                    await ctx.send(f'You only have **{item.wool} wool**')
                elif stats.leggings != 3:
                    await ctx.send(f'You dont have a **diamond leggings**')
                atk_def(ctx)
    
            elif arg == 'meaty wooly diamond boots':
                if stats.boots == 4:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 40 and item.beef >= 40 and item.wool >= 40 and stats.boots == 3:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 40
                    db[stats.userid + 'beef'] = item.beef - 40
                    db[stats.userid + 'wool'] = item.wool - 40
                    db[stats.userid + 'boots'] = 4
                    await ctx.send(f'**{username}**, meaty wooly diamond boots is crafted')
                elif mobdrop.pogchop < 40:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchop**')
                elif item.beef < 40:
                    await ctx.send(f'You only have **{item.beef} beef**')
                elif item.wool < 40:
                    await ctx.send(f'You only have **{item.wool} wool**')
                elif stats.boots != 4:
                    await ctx.send(f'You dont have a **diamond boots**')
                atk_def(ctx)
    
            elif arg == 'meaty wooly diamond sword':
                if stats.sword == 4:
                    await ctx.send('You will regret, check your inv :D')
                elif mobdrop.pogchop >= 20 and item.beef >= 20 and item.wool >= 20 and stats.sword == 3:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 20
                    db[stats.userid + 'beef'] = item.beef - 20
                    db[stats.userid + 'wool'] = item.wool - 20
                    db[stats.userid + 'sword'] = 4
                    await ctx.send(f'**{username}**, meaty wooly diamond sword is crafted')
                elif mobdrop.pogchop < 20:
                    await ctx.send(f'You only have **{mobdrop.pogchop} pogchop**')
                elif item.beef < 20:
                    await ctx.send(f'You only have **{item.beef} beef**')
                elif item.wool < 20:
                    await ctx.send(f'You only have **{item.wool} wool**')
                elif stats.sword != 3:
                    await ctx.send(f'You dont have a **diamond sword**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly diamond helmet':
                if stats.helmet == 5:
                    await ctx.send('You will regret, check your inv :D')
                elif item.gold_ingot >= 50 and stats.helmet == 4:
                    db[stats.userid + 'gold_ingot'] = item.gold_ingot - 50
                    db[stats.userid + 'helmet'] = 5
                    await ctx.send(f'**{username}**, shiny meaty wooly diamond helmet is crafted')
                elif item.gold_ingot < 50:
                    await ctx.send(f'You only have **{item.gold_ingot} gold_ingot**')
                elif stats.helmet != 4:
                    await ctx.send(f'You dont have a  **meaty wooly diamond helmet**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly diamond chestplate':
                if stats.chestplate == 5:
                    await ctx.send('You will regret, check your inv :D')
                elif item.gold_ingot >= 80 and stats.chestplate == 4:
                    db[stats.userid + 'gold_ingot'] = item.gold_ingot - 80
                    db[stats.userid + 'chestplate'] = 5
                    await ctx.send(f'**{username}**, shiny meaty wooly diamond chestplate is crafted')
                elif item.gold_ingot < 80:
                    await ctx.send(f'You only have **{item.gold_ingot} gold_ingot**')
                elif stats.chestplate != 4:
                    await ctx.send(f'You dont have a **meaty wooly diamond chestplate**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly diamond leggings':
                if stats.leggings == 5:
                    await ctx.send('You will regret, check your inv :D')
                elif item.gold_ingot >= 70 and stats.leggings == 4:
                    db[stats.userid + 'gold_ingot'] = item.gold_ingot - 70
                    db[stats.userid + 'leggings'] = 5
                    await ctx.send(f'**{username}**, shiny meaty wooly diamond leggings is crafted')
                elif item.gold_ingot < 70:
                    await ctx.send(f'You only have **{item.gold_ingot} gold_ingot**')
                elif stats.leggings != 4:
                    await ctx.send(f'You dont have a **meaty wooly diamond leggings**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly diamond boots':
                if stats.boots == 5:
                    await ctx.send('You will regret, check your inv :D')
                elif item.gold_ingot >= 40 and stats.boots == 4:
                    db[stats.userid + 'gold_ingot'] = item.gold_ingot - 40
                    db[stats.userid + 'boots'] = 5
                    await ctx.send(f'**{username}**, shiny meaty wooly diamond boots is crafted')
                elif item.gold_ingot < 40:
                    await ctx.send(f'You only have **{item.gold_ingot} gold_ingot**')
                elif stats.boots != 4:
                    await ctx.send(f'You dont have a **meaty wooly diamond boots**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly diamond sword':
                if stats.sword == 5:
                    await ctx.send('You will regret, check your inv :D')
                elif item.gold_ingot >= 20 and stats.sword == 4:
                    db[stats.userid + 'gold_ingot'] = item.gold_ingot - 20
                    db[stats.userid + 'sword'] = 5
                    await ctx.send(f'**{username}**, shiny meaty wooly diamond sword is crafted')
                elif item.gold_ingot < 20:
                    await ctx.send(f'You only have **{item.gold_ingot} gold_ingot**')
                elif stats.sword != 4:
                    await ctx.send(f'You dont have a **meaty wooly diamond sword**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly netherite helmet':
                if stats.helmet == 6:
                    await ctx.send('You will regret, check your inv :D')
                elif item.netherite_ingot >= 1 and stats.helmet == 5:
                    db[stats.userid + 'netherite_ingot'] = item.netherite_ingot - 1
                    db[stats.userid + 'helmet'] = 6
                    await ctx.send(f'**{username}**, shiny meaty wooly netherite helmet is crafted')
                elif item.netherite_ingot < 1:
                    await ctx.send(f'You dont have a **netherite_ingot**')
                elif stats.helmet != 5:
                    await ctx.send(f'You dont have a **shiny meaty wooly diamond helmet**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly netherite chestplate':
                if stats.chestplate == 6:
                    await ctx.send('You will regret, check your inv :D')
                elif item.netherite_ingot >= 1 and stats.chestplate == 5:
                    db[stats.userid + 'netherite_ingot'] = item.netherite_ingot - 1
                    db[stats.userid + 'chestplate'] = 6
                    await ctx.send(f'**{username}**,shiny meaty wooly netherite chestplate is crafted')
                elif item.netherite_ingot < 1:
                    await ctx.send(f'You only have **{item.netherite_ingot} netherite_ingot**')
                elif stats.chestplate != 5:
                    await ctx.send(f'You dont have a **shiny meaty wooly diamond chestplate**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly netherite leggings':
                if stats.leggings == 6:
                    await ctx.send('You will regret, check your inv :D')
                elif item.netherite_ingot >= 1 and stats.leggings == 5:
                    db[stats.userid + 'netherite_ingot'] = item.netherite_ingot - 1
                    db[stats.userid + 'shiny meaty wooly netherite leggings'] = True
                    db[stats.userid + 'shiny_meaty_wooly_diamond_leggings'] = False
                    await ctx.send(f'**{username}**, shiny meaty wooly netherite leggings is crafted')
                elif item.netherite_ingot < 1:
                    await ctx.send('You dont have a ** netherite_ingot**')
                elif stats.leggings != 5:
                    await ctx.send(f'You dont have a **shiny meaty wooly diamond leggings**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly netherite boots':
                if stats.boots == 6:
                    await ctx.send('You will regret, check your inv :D')
                elif item.netherite_ingot >= 1 and stats.boots == 5:
                    db[stats.userid + 'netherite_ingot'] = item.netherite_ingot - 1
                    db[stats.userid + 'boots'] = 6
                    await ctx.send(f'**{username}**, shiny meaty wooly netherite boots is crafted')
                elif item.netherite_ingot < 1:
                    await ctx.send('You dont have a ** netherite_ingot**')
                elif stats.boots != 5:
                    await ctx.send(f'You dont have a **shiny meaty wooly diamond boots**')
                atk_def(ctx)
    
            elif arg == 'shiny meaty wooly netherite sword':
                if stats.sword == 6:
                    await ctx.send('You will regret, check your inv :D')
                elif item.netherite_ingot >= 1 and stats.sword == 5:
                    db[stats.userid + 'netherite_ingot'] = item.netherite_ingot - 1
                    db[stats.userid + 'sword'] = 6
                    await ctx.send(f'**{username}**, shiny meaty wooly netherite sword is crafted')
                elif item.netherite_ingot < 1:
                    await ctx.send('You dont have a ** netherite_ingot**')
                elif stats.sword != 5:
                    await ctx.send('You dont have a **shiny meaty wooly diamond sword**')
                atk_def(ctx)
    
            elif arg == 'more shiny meaty wooly netherite helmet':
                if stats.helmet == 7:
                    await ctx.send('You will regret, check your inv :D')
                elif item.redstone >= 50 and stats.thelmet == 6:
                    db[stats.userid + 'redstone'] = item.redstone - 50
                    db[stats.userid + 'helmet'] = 7
                    await ctx.send(f'**{username}**, more shiny meaty wooly netherite helmet is crafted')
                elif item.redstone < 50:
                    await ctx.send(f'You only have **{item.redstone} redstone**')
                elif stats.helmet != 6:
                    await ctx.send(f'You dont have a **shiny meaty wooly netherite helmet**')
                atk_def(ctx)
    
            elif arg == 'more shiny meaty wooly netherite chestplate':
                if stats.chestplate == 7:
                    await ctx.send('You will regret, check your inv :D')
                elif item.redstone >= 80 and stats.chestplate == 6:
                    db[stats.userid + 'redstone'] = item.redstone - 80
                    db[stats.userid + 'chestplate'] = 7
                    await ctx.send(f'**{username}**, more shiny meaty wooly netherite helmet is crafted')
                elif item.redstone < 80:
                    await ctx.send(f'You only have **{item.redstone} redstone**')
                elif stats.chestplate != 6:
                    await ctx.send(f'You dont have a **shiny meaty wooly netherite chestplate**')
                atk_def(ctx)
    
            elif arg == 'more shiny meaty wooly netherite leggings':
                if stats.leggings == 7:
                    await ctx.send('You will regret, check your inv :D')
                elif item.redstone >= 70 and stats.leggings == 6:
                    db[stats.userid + 'redstone'] = item.redstone - 70
                    db[stats.userid + 'leggings'] = 7
                    await ctx.send(f'**{username}**, more shiny meaty wooly netherite leggings is crafted')
                elif item.redstone < 70:
                    await ctx.send(f'You only have **{item.redstone} redstone**')
                elif stats.leggings != 6:
                    await ctx.send(f'You dont have a **shiny meaty wooly netherite leggings**')
                atk_def(ctx)
    
            elif arg == 'more shiny meaty wooly netherite boots':
                if stats.boots == 7:
                    await ctx.send('You will regret, check your inv :D')
                elif item.redstone >= 40 and stats. boots == 6:
                    db[stats.userid + 'redstone'] = item.redstone - 40
                    db[stats.userid + 'boots'] = 7
                    await ctx.send(f'**{username}**, more shiny meaty wooly netherite boots is crafted')
                elif item.redstone < 40:
                    await ctx.send(f'You only have **{item.redstone} redstone**')
                elif stats.boots != 6:
                    await ctx.send(f'You dont have a **shiny meaty wooly netherite boots**')
                atk_def(ctx)
    
            elif arg == 'more shiny meaty wooly netherite sword':
                if stats.sword == 7:
                    await ctx.send('You will regret, check your inv :D')
                elif item.redstone >= 20 and stats.sword == 6:
                    db[stats.userid + 'redstone'] = item.redstone - 20
                    db[stats.userid + 'sword'] = 7
                    await ctx.send(f'**{username}**, more shiny meaty wooly netherite sword is crafted')
                elif item.redstone < 20:
                    await ctx.send(f'You only have **{item.redstone} redstone**')
                elif stats.sword != 6:
                    await ctx.send(f'You dont have a **shiny meaty wooly netherite sword**')
                atk_def(ctx)
    
            elif arg == 'cooked pogchop':
                if mobdrop.pogchop >= 8 and misc.coal >= 1:
                    db[stats.userid + 'pogchop'] = mobdrop.pogchop - 8
                    db[stats.userid + 'coal'] = misc.coal - 1
                    db[stats.userid + 'cooked_pogchop'] = db[stats.userid + 'cooked_pogchop'] + 8
                    await ctx.send(f'**{username}**cooked 8 pogchop')
                elif mobdrop.pogchop < 8:
                    await ctx.send(f'**{username}**, how do you cook pogchop without pogchop???**')
                elif misc.coal < 1:
                    await ctx.send(f'**{username}**, no fire :(**')
    
            elif arg == 'steak':
                if item.beef >= 8 and misc.coal >= 1:
                    db[stats.userid + 'beef'] = item.beef - 8
                    db[stats.userid + 'coal'] = misc.coal - 1
                    db[stats.userid + 'steak'] = db[stats.userid + 'steak'] + 8
                    await ctx.send(f'**{username}**cooked 8 steak')
                elif item.beef < 8:
                    await ctx.send(f'**{username}**, how do you cook steak without beef???**')
                elif misc.coal < 1:
                    await ctx.send(f'**{username}**, no fire :(**')
                
            elif arg == 'bed':
                if item.wool >= 3 and item.wood >= 3:
                    db[stats.userid + 'wool'] -= 3
                    db[stats.userid + 'wood'] -= 3
                    db[stats.userid + 'bed'] += 1
                    await ctx.send(f'**{username}**, bed is crafted')
                elif item.wool < 3:
                    await ctx.send(f'You only have **{item.wool} wool**')
                elif item.wood < 3:
                    await ctx.send(f'You only have **{item.wood} wood**')
    
            elif arg == 'blaze powder':
                if item.blaze_rod >= 1:
                    db[stats.userid + 'blaze_rod'] -= 1
                    db[stats.userid + 'blaze_powder'] += 2
                    await ctx.send(f'**{username}** powdered a blaze_rod')
                else:
                    await ctx.send(f'You dont have any **blaze_rod**')
            
            elif arg == 'eye of ender':
                if item.blaze_powder >= 1 and item.ender_pearl >= 1:
                    db[stats.userid + 'blaze_powder'] -= 1
                    db[stats.userid + 'ender_pearl'] -= 1
                    db[stats.userid + 'eye_of_ender'] += 1
                    await ctx.send(f'**{username}**crafted an eye_of_ender')
                elif item.blaze_powder == 0:
                    await ctx.send(f'You dont have any **blaze_powder**')
                elif item.ender_pearl == 0:
                    await ctx.send(f'You dont have any **ender_peark**')
            
            elif arg == 'map':
                if item.map_scrap >= 5:
                    db[stats.userid + 'map_scrap'] -= 5
                    db[stats.userid + 'map'] += 1
                    await ctx.send(f'**{username}** has finished  **sea monument map**')
                else:
                    await ctx.send(f'You dont have enough **map scrap**')
    
            elif arg == 'netherite ingot':
                if item.netherite_scrap >= 4 and item.gold_ingot >= 4:
                    db[stats.userid + 'netherite_scrap'] -= 4
                    db[stats.userid + 'gold_ingot'] -= 4
                    db[stats.userid + 'netherite_ingot'] += 1
                    await ctx.send(f'**{username}** crafted a **netherite ingot**')
                elif item.netherite_scrap < 4:
                    await ctx.send(f'You dont have enough **netherite scrap**')
                else:
                    await ctx.send(f'You dont have enough **gold_ingot**')
        except KeyError: #error handler
            await ctx.send(f'**{username}**, your account is either not created yet or not at the latest version. Try using `rpm start`')
            
async def setup(bot):
    await bot.add_cog(Craft(bot))