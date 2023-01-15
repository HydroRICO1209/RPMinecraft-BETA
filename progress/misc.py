class Misc():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler
        
        self.userid = ctx.author.id
        self.emerald = await dbfunc.fetchValue('emerald', 'misc', self.userid)
        self.cobble = await dbfunc.fetchValue('cobble', 'misc', self.userid)
        self.coal = await dbfunc.fetchValue('coal', 'misc', self.userid)
        self.iron_ingot = await dbfunc.fetchValue('iron_ingot', 'misc', self.userid)
        self.diamond = await dbfunc.fetchValue('diamond', 'misc', self.userid)
        self.gold_ingot = await dbfunc.fetchValue('gold_ingot', 'misc', self.userid)
        self.netherite_scrap = await dbfunc.fetchValue('netherite_scrap', 'misc', self.userid)
        self.netherite_ingot = await dbfunc.fetchValue('netherite_ingot', 'misc', self.userid)
        self.redstone = await dbfunc.fetchValue('redstone', 'misc', self.userid)
        self.soul_sand = await dbfunc.fetchValue('soul_sand', 'misc', self.userid)
        self.wood = await dbfunc.fetchValue('wood', 'misc', self.userid)
        self.bed = await dbfunc.fetchValue('bed', 'misc', self.userid)
        self.common_chest = await dbfunc.fetchValue('common_chest', 'misc', self.userid)
        self.rare_chest = await dbfunc.fetchValue('rare_chest', 'misc', self.userid)
        self.super_rare_chest = await dbfunc.fetchValue('super_rare_chest', 'misc', self.userid)
        self.epic_chest = await dbfunc.fetchValue('epic_chest', 'misc', self.userid)
        self.mythic_chest = await dbfunc.fetchValue('mythic_chest', 'misc', self.userid)
        self.legendary_chest = await dbfunc.fetchValue('legendary_chest', 'misc', self.userid)