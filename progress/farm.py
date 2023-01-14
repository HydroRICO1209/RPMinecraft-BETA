class Farm():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.small_sapling = await dbfunc.fetchValue('small_sapling', 'armors', self.userid)
        self.medium_sapling = await dbfunc.fetchValue('medium_sapling', 'armors', self.userid)
        self.large_sapling = await dbfunc.fetchValue('large_sapling', 'armors', self.userid)
        self.apple = await dbfunc.fetchValue('apple', 'armors', self.userid)
        self.wheat_seeds = await dbfunc.fetchValue('wheat_seeds', 'armors', self.userid)
        self.wheat = await dbfunc.fetchValue('wheat', 'armors', self.userid)
        self.potato = await dbfunc.fetchValue('potato', 'armors', self.userid)
        self.poisonous_potato = await dbfunc.fetchValue('poisonous_potato', 'armors', self.userid)
        self.carrot = await dbfunc.fetchValue('carrot', 'armors', self.userid)
        self.beetroot_seeds = await dbfunc.fetchValue('beetroot_seeds', 'armors', self.userid)
        self.beetroot = await dbfunc.fetchValue('beetroot', 'armors', self.userid)
        self.cleansed_water_bucket = await dbfunc.fetchValue('cleansed_water_bucket', 'armors', self.userid)
        self.cleansed_dirt = await dbfunc.fetchValue('cleansed_dirt', 'armors', self.userid)