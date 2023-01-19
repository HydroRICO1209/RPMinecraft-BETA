async def Misc(ctx):
    intents = discord.Intents.all()
    intents.members = True
    prefixxx  = ['rpm ', 'Rpm ', 'RPM ', 'RPm ']
    bot = commands.Bot(command_prefix = prefixxx, case_insensitive=True, activity=discord.Game(name="rpm start"),intents=intents)
    dbfunc = bot.database_handler
    
    userid = ctx.author.id
    emerald = await dbfunc.fetchValue('emerald', 'misc', userid)
    cobble = await dbfunc.fetchValue('cobble', 'misc', userid)
    coal = await dbfunc.fetchValue('coal', 'misc', userid)
    iron_ingot = await dbfunc.fetchValue('iron_ingot', 'misc', userid)
    diamond = await dbfunc.fetchValue('diamond', 'misc', userid)
    gold_ingot = await dbfunc.fetchValue('gold_ingot', 'misc', userid)
    netherite_scrap = await dbfunc.fetchValue('netherite_scrap', 'misc', userid)
    netherite_ingot = await dbfunc.fetchValue('netherite_ingot', 'misc', userid)
    redstone = await dbfunc.fetchValue('redstone', 'misc', userid)
    soul_sand = await dbfunc.fetchValue('soul_sand', 'misc', userid)
    wood = await dbfunc.fetchValue('wood', 'misc', userid)
    bed = await dbfunc.fetchValue('bed', 'misc', userid)
    common_chest = await dbfunc.fetchValue('common_chest', 'misc', userid)
    rare_chest = await dbfunc.fetchValue('rare_chest', 'misc', userid)
    super_rare_chest = await dbfunc.fetchValue('super_rare_chest', 'misc', userid)
    epic_chest = await dbfunc.fetchValue('epic_chest', 'misc', userid)
    mythic_chest = await dbfunc.fetchValue('mythic_chest', 'misc', userid)
    legendary_chest = await dbfunc.fetchValue('legendary_chest', 'misc', userid)