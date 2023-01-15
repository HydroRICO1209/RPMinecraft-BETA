class Stats():
    async def __init__(self, bot):
        self.bot = bot

    async def value(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.hp = await dbfunc.fetchValue('hp', 'misc', self.userid)
        self.highest_area = await dbfunc.fetchValue('highest_area', 'armors', self.userid)
        self.atk = await dbfunc.fetchValue('atk', 'armors', self.userid)
        self.defend = await dbfunc.fetchValue('defend', 'armors', self.userid)
        self.xp = await dbfunc.fetchValue('xp', 'armors', self.userid)
        self.maxxp = self.level * 200
        self.area = await dbfunc.fetchValue('area', 'armors', self.userid)