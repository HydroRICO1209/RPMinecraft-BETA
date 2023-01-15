class Stats():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.hp = await dbfunc.fetchValue('hp', 'stats', self.userid)
        self.highest_area = await dbfunc.fetchValue('highest_area', 'stats', self.userid)
        self.atk = await dbfunc.fetchValue('atk', 'stats', self.userid)
        self.defend = await dbfunc.fetchValue('defend', 'stats', self.userid)
        self.xp = await dbfunc.fetchValue('xp', 'stats', self.userid)
        self.level = await dbfunc.fetchValue('level', 'stats', self.userid)
        self.maxxp = self.level * 200
        self.area = await dbfunc.fetchValue('area', 'stats', self.userid)