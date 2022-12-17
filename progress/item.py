from replit import db

class Item():  
    def __init__(self, ctx):  
        self.userid = str(ctx.author.id)

        #item
        self.pogchop = db[self.userid + 'pogchop']
        self.cooked_pogchop =  db[self.userid + 'cooked_pogchop']
        self.beef =  db[self.userid + 'beef']
        self.steak =  db[self.userid + 'steak']
        self.wool =  db[self.userid + 'wool']
        self.map_scrap =  db[self.userid + 'map_scrap']
        self.map =  db[self.userid + 'map']
        self.wither_skull =  db[self.userid + 'wither_skull']
        self.blaze_rod =  db[self.userid + 'blaze_rod']
        self.blaze_powder =  db[self.userid + 'blaze_powder']
        self.ender_pearl =  db[self.userid + 'ender_pearl']
        self.eye_of_ender =  db[self.userid + 'eye_of_ender']

        #misc
        self.cobble =  db[self.userid + 'cobble']
        self.coal =  db[self.userid + 'coal']
        self.iron_ingot =  db[self.userid + 'iron_ingot']
        self.diamond =  db[self.userid + 'diamond'] 
        self.gold_ingot =  db[self.userid + 'gold_ingot']
        self.netherite_scrap =  db[self.userid + 'netherite_scrap']
        self.netherite_ingot =  db[self.userid + 'netherite_ingot']
        self.redstone =  db[self.userid + 'redstone']
        self.soul_sand =  db[self.userid + 'soul_sand']
        self.wood =  db[self.userid + 'wood']
        self.bed =  db[self.userid + 'bed']
        self.common_chest = db[self.userid + 'common_chest']
        self.rare_chest = db[self.userid + 'rare_chest']
        self.super_rare_chest = db[self.userid + 'super_rare_chest']
        self.epic_chest = db[self.userid + 'epic_chest']
        self.mythic_chest = db[self.userid + 'mythic_chest']
        self.legendary_chest = db[self.userid + 'legendary_chest']

        #illegal
        self.bedrock =  db[self.userid + 'bedrock']
        self.bedrock_trophy =  db[self.userid + 'bedrock_trophy']
        self.pog_champ =  db[self.userid + 'pog_champ']

        #farm
        self.small_sapling = db[self.userid + 'small_sapling']
        self.medium_sapling = db[self.userid + 'medium_sapling']
        self.large_sapling = db[self.userid + 'large_sapling']
        self.apple = db[self.userid + 'apple']
        self.wheat_seeds = db[self.userid + 'wheat_seeds']
        self.wheat = db[self.userid + 'wheat']
        self.potato = db[self.userid + 'potato']
        self.poisonous_potato = db[self.userid + 'poisonous_potato']
        self.carrot = db[self.userid + 'carrot']
        self.beetroot_seeds = db[self.userid + 'beetroot_seeds']
        self.beetroot = db[self.userid + 'beetroot']
        self.cleansed_water_bucket = db[self.userid + 'cleansed_water_bucket']
        self.cleansed_dirt = db[self.userid + 'cleansed_dirt']
        self.farmlist = db[self.userid + 'farmlist']