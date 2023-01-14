class Armors():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.totalslot = await dbfunc.fetchValue('total_slot', 'armors', self.userid)
        self.slot1 = await dbfunc.fetchValue('slot1', 'armors', self.userid)
        self.slot1time = await dbfunc.fetchValue('slot1time', 'armors', self.userid)
        self.slot2 = await dbfunc.fetchValue('slot2', 'armors', self.userid)
        self.slot2time = await dbfunc.fetchValue('slot2time', 'armors', self.userid)
        self.slot3 = await dbfunc.fetchValue('slot3', 'armors', self.userid)
        self.slot3time = await dbfunc.fetchValue('slot3time', 'armors', self.userid)
