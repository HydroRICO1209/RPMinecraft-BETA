class mobdr():
    async def __init__(self, ctx):
        dbfunc = self.bot.database_handler

        self.userid = ctx.author.id
        self.pogchop = await dbfunc.fetchValue('pogchop', 'mobdrop', self.userid)
        self.cooked_pogchop = await dbfunc.fetchValue('cooked_pogchop', 'mobdrop', self.userid)
        self.beef = await dbfunc.fetchValue('beef', 'mobdrop', self.userid)
        self.steak = await dbfunc.fetchValue('steak', 'mobdrop', self.userid)
        self.wool = await dbfunc.fetchValue('wool', 'mobdrop', self.userid)
        self.map_scrap = await dbfunc.fetchValue('map_scrap', 'mobdrop', self.userid)
        self.map = await dbfunc.fetchValue('map', 'mobdrop', self.userid)
        self.wither_skull = await dbfunc.fetchValue('wither_skull', 'mobdrop', self.userid)
        self.blaze_rod = await dbfunc.fetchValue('blaze_rod', 'mobdrop', self.userid)
        self.blaze_powder = await dbfunc.fetchValue('blaze_powder', 'mobdrop', self.userid)
        self.ender_pearl = await dbfunc.fetchValue('ender_pearl', 'mobdrop', self.userid)
        self.eye_of_ender = await dbfunc.fetchValue('eye_of_ender', 'mobdrop', self.userid)