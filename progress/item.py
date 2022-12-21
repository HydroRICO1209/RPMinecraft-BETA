class Item():
    def __init__(self, ctx):  
        self.userid = str(ctx.author.id)
    
    async def fetchvalue(self, item, tablename):
        return (await self.bot.db.fetch('SELECT $1 FROM $2 WHERE userid = $3', item, tablename, self.userid))[0][item]