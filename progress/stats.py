class Stats():
    def __init__(self, ctx):
        self.userid = str(ctx.author.id)
        self.helmet = db[self.userid  +'helmet']
        self.chestplate = db[self.userid + 'chestplate' ]
        self.leggings = db[self.userid + 'leggings']
        self.boots = db[self.userid + 'boots']
        self.sword = db[self.userid + 'sword']  
        self.hp = db[self.userid + 'hp']  
        self.level = db[self.userid + 'level']
        self.highestArea = db[self.userid + 'highestArea']
        self.atk = db[self.userid + 'atk']
        self.defend = db[self.userid + 'defend']
        self.xp = db[self.userid + 'xp']
        self.maxxp = self.level * 200
        self.area = db[self.userid + 'area']