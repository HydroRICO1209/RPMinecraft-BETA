async def fetchvalue(item, tablename, userid):
    return (await self.bot.db.fetch('SELECT $1 FROM $2 WHERE userid = $3', item, tablename, userid))[0][item]