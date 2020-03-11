import random


class Equipment(object):
    RARITY = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]

    def __init__(self,eq_type):
        self.rarity_level, self.rare_mod = self.pick_rare()
        self.eq_type = eq_type

    def pick_rare(self):
        x = random.randint(1, 10)
        if x >=1 and x  <= 2:
            return Equipment.RARITY[0],2
        elif x > 2 and x  <= 5:
            return Equipment.RARITY[1],4
        elif x > 5 and x  <= 8:
            return Equipment.RARITY[2],8
        elif x >= 8 and x  <= 9:
            return Equipment.RARITY[3],16
        elif x == 10:
            return Equipment.RARITY[4],32

class Armor(Equipment):
    ARMORTYPE = ["Helmet", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self,aType):
        super(Armor, self).__init__("Armor")
        self.aType = aType
        self.armor = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
                armor Type: {}
                Rarity Level: {}
                Armor: {}
                Luck: {}
                Stamina: {}
                IQ: {}
                Agility: {}
            """.format(self.aType, self.rarity_level, self.armor, self.luck, self.stamina, self.iq, self.agi)

class Helm(Armor):
    def __init__(self):
        super(Helm, self).__init__(Armor.ARMORTYPE[0])
        self.armor = random.randint(5, 10) * self.rare_mod
        self.stamina = random.randint(0, 8) + self.rare_mod
        self.agi = random.randint(0, 8) + self.rare_mod
        self.iq = random.randint(0, 8) + self.rare_mod
        self.luck = random.randint(0, 8) + self.rare_mod

class Chest(Armor):
    def __init__(self):
        super(Chest, self).__init__(Armor.ARMORTYPE[1])
        self.armor = random.randint(5, 25) * self.rare_mod
        self.stamina = random.randint(0, 25) + self.rare_mod
        self.agi = random.randint(0, 25) + self.rare_mod
        self.iq = random.randint(0, 25) + self.rare_mod
        self.luck = random.randint(0, 25) + self.rare_mod

class Legs(Armor):
    def __init__(self):
        super(Legs, self).__init__(Armor.ARMORTYPE[2])
        self.armor = random.randint(5, 15) * self.rare_mod
        self.stamina = random.randint(0, 15) + self.rare_mod
        self.agi = random.randint(0, 15) + self.rare_mod
        self.iq = random.randint(0, 15) + self.rare_mod
        self.luck = random.randint(0, 15) + self.rare_mod

class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__(Armor.ARMORTYPE[3])
        self.armor = random.randint(5, 10) * self.rare_mod
        self.stamina = random.randint(0, 8) + self.rare_mod
        self.agi = random.randint(0, 8) + self.rare_mod
        self.iq = random.randint(0, 8) + self.rare_mod
        self.luck = random.randint(0, 8) + self.rare_mod

class Gloves(Armor):
    def __init__(self):
        super(Gloves, self).__init__(Armor.ARMORTYPE[4])
        self.armor = random.randint(5, 8) * self.rare_mod
        self.stamina = random.randint(0, 5) + self.rare_mod
        self.agi = random.randint(0, 5) + self.rare_mod
        self.iq = random.randint(0, 5) + self.rare_mod
        self.luck = random.randint(0, 5) + self.rare_mod

class Weapon(Equipment):
    WEAPONTYPE = ["Sword", "Staff", "Bow"]

    def __init__(self, wType):
        super(Weapon, self).__init__("Weapon")
        self.wType = wType
        self.atk = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return"""
                Weapon Type: {}
                Rarity Level: {}
                Luck: {}
                Stamina: {}
                IQ: {}
                Agility: {}
            """.format(self.wType, self.rarity_level, self.luck, self.stamina, self.iq, self.agi)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(Weapon.WEAPONTYPE[0])
        self.atk = random.randint(8, 12) * self.rare_mod
        self.stamina = random.randint(8, 12) * self.rare_mod
        self.agi = random.randint(0, 8) * self.rare_mod
        self.luck = random.randint(5, 10) *self.rare_mod

class Staff(Weapon):
    def __init__(self):
        super(Staff, self).__init__(Weapon.WEAPONTYPE[1])
        self.atk = random.randint(10, 15)
        self.iq = random.randint(10, 20) * self.rare_mod
        self.agi = random.randint(0, 3) * self.rare_mod
        self.luck = random.randint(0, 5) *self.rare_mod

class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__(Weapon.WEAPONTYPE[2])
        self.atk = random.randint(5, 10)
        self.stamina = random.randint(5, 10) * self.rare_mod
        self.agi = random.randint(0, 15) * self.rare_mod
        self.luck = random.randint(5, 15) *self.rare_mod





