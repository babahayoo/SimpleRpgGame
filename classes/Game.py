import random

class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,hp,mp,atk,df,magic):
        self.maxhp = hp
        self.hp = hp

        self.maxmp = mp
        self.mp = mp

        self.atkl = atk - 10
        self.atkh = atk + 10

        self.df = df
        self.magic = magic
        self.actions = ["attack", "magic"]

    def generateDamage(self):
        return random.randrange(self.atkl,self.atkh)

    def generateSpellDamage(self,i):
        mgl = self.magic[i]["dmg"] - 5 #magic low damage
        mgh = self.magic[i]["dmg"] + 5 #magic high damage

        return random.randrange(mgl, mgh)

    def takeDamage(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.maxhp

    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.maxmp

    def reduceMp(self,cost):
        self.mp -= cost

    def getSpellName(self,i):
        return self.magic[i]["name"]

    def getSpellMpCost(self,i):
        return self.magic[i]["cost"]

    def chooseAction(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def chooseMagic(self):
        i = 1
        print(bColors.OKBLUE + bColors.BOLD + "Magic" + bColors.ENDC)
        for spell in self.magic:
            print(str(i)+":", spell["name"], "(cost:", str(spell["cost"])+")")
            i += 1

