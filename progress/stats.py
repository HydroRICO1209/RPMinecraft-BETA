from discord.ext import commands
import discord

async def Stats(ctx):
    intents = discord.Intents.all()
    intents.members = True
    prefixxx  = ['rpm ', 'Rpm ', 'RPM ', 'RPm ']
    bot = commands.Bot(command_prefix = prefixxx, case_insensitive=True, activity=discord.Game(name="rpm start"),intents=intents)

    dbfunc = bot.database_handler

    userid = ctx.author.id
    hp = await dbfunc.fetchValue('hp', 'stats', userid)
    highest_area = await dbfunc.fetchValue('highest_area', 'stats', userid)
    atk = await dbfunc.fetchValue('atk', 'stats', userid)
    defend = await dbfunc.fetchValue('defend', 'stats', userid)
    xp = await dbfunc.fetchValue('xp', 'stats', userid)
    level = await dbfunc.fetchValue('level', 'stats', userid)
    maxxp = level * 200
    area = await dbfunc.fetchValue('area', 'stats', userid)