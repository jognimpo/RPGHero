import random
from Armor import *

class Hero(object):
    RACELIST = ["Human", "Elf", "Goblin"]
    CLASSLIST = ["Warrior", "Mage", "Hunter"]

    def __init__(self):
        self.is_alive = True
        self.level = 1
        self.race = self.pick_race()
        self.player_class = self.pick_class()
        self.name = input("What is your heroes name?")
        self.xp = 0
        self.xp_to_levelup = 90 + (self.level * 10)
        #health
        self.healthmod = 100
        self.max_health = self.level * self.healthmod
        self.hp = self.max_health
        #mana
        self.manamod = 100
        self.max_mana = self.level * self.manamod
        self.mana = self.max_mana

        #base stats
        self.deff = 0
        self.atk = 10
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0
        self.setMods()
        self.atk_list = []

        #setup hero inventories
        self.inventory = []
        self.invmax = 10
        self.helmeq = []
        self.chesteq = []
        self.legeq = []
        self.gloveq = []
        self.bootseq = []
        self.righthandweq = []
        self.lefthandweq = []
        self.pop_inv()

    def pop_inv(self):
        #give some random potions
        x = random.randint(0, 4)
        for i in range(x):
            y = random.randint(0, 1)
            if y == 1:
                self.add_to_inv("Health potion")
            else:
                self.add_to_inv("Mana potion")
        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()
        x = random.randint(0, 3)
        if x == 0:
            weapon = Sword()
        elif x == 1:
            weapon = Staff()
        else:
            weapon = Bow()
        self.add_to_inv(helm)
        self.add_to_inv(chest)
        self.add_to_inv(legs)
        self.add_to_inv(boots)
        self.add_to_inv(gloves)
        self.add_to_inv(weapon)

    def add_to_inv(self, item):
        if len(self.inventory) < self.invmax:
            self.inventory.append(item)
            print("picked up", item)
        else:
            print("not enough inventory space")
            return

    def setMods(self):
        if self.player_class == "Warrior":
            self.deff = random.randint(5, 20)
            self.atk = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.max_mana = 0

        if self.player_class == "Mage":
            self.deff = random.randint(5, 10)
            self.atk = random.randint(5, 20)
            self.luck - random.randint(1, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 20)
            self.agi = random.randint(1, 5)
            self.manamod = random.randint(15, 20)

        if self.player_class == "Hunter":
            self.deff = random.randint(5, 15)
            self.atk = random.randint(8, 18)
            self.luck = random.randint(5, 10)
            self.stamina = random.randint(15, 20)
            self.iq = random.randint(5, 12)
            self.agi = random.randint(5, 15)

        if self.race == "Elf":
            self.stamina -= 2
            self.iq += 2

        if self.race == "Goblin":
            self.deff +=1
            self.agi +=1

    def __str__(self):
        return """
                Name:{}\t Race:{}\t Class:{}\t Level:{}
                Health:{}\t Mana:{}\t          Xp:{} 
                Attack:{}\t  Defence:{}
                Luck:{} \t     Stamina:{} 
                iq:{}\t     Agility:{}""".format(self.name, self.race, self.player_class, self.level, self.hp, self.mana, self.xp, self.atk,
                                                 self.deff, self.luck, self.stamina, self.iq, self.agi)

    def pick_race(self):
        while True:
            try:
                print(Hero.RACELIST)
                x = input("Pick your Race")
                if x in Hero.RACELIST:
                    return x
            except:
                print("Not a good option")

    def pick_class(self):
        while True:
            try:
                print(Hero.CLASSLIST)
                x = input("Pick your Class")
                if x in Hero.CLASSLIST:
                    return x
            except:
                print("Not a good option")

    def die(self):
        if self.hp <= 0:
            self.unequip_all()
            drop_xp = 20*self.level
            drop_item = random.choice(self.inventory)
            return drop_xp, drop_item
        else:
            return "",""

    def levelup(self):
        if self.xp >= self.xp_to_levelup:
            print("LEVEL UP!")
            print(self)
            remxp = self.xp - self.xp_to_levelup
            self.level += 1
            self.xp_to_levelup = 90 + (self.level * 10)
            self.xp = remxp
            self.healthmod = self.healthmod + self.level
            self.max_health = self.level * self.healthmod
            self.hp = self.max_health
            if self.player_class != "Warrior":
                self.manamod = self.manamod + self.level
                self.max_mana = self.level * self.manamod
                self.mana = self.max_mana
            self.level_mod()

    def level_mod(self):
        points = random.randint(1, self.level+1)
        while points > 0:
            print(
                """
                
                Luck:{}
                Stamina:{}
                iq: {}
                Agility:{}""".format(self.luck, self.stamina, self.iq, self.agi))
            x = input("What stat would you like to add to")
            y = int(input("you have " + str(points)+ " point(s) to spend how many would you like to put in " + x))
            if x == "stamina":
                self.stamina += y
                points -= y
            elif x == "luck":
                self.luck += y
                points -= y
            elif x == "iq":
                self.iq += y
                points -= y
            elif x == "agility":
                self.agi += y
                points -= y
            else:
                print("not a good option")

        else:
            return

    def add_xp(self, xp):
        print("You picked up " + str(xp) +" xp!")
        self.xp += xp
        self.levelup()

    def equip_gloves(self):
        for i in self.inventory:
            x = type(i)
            if "Gloves" in str(x):
                if len(self.gloveq) < 1:
                    print("you equiped a set of gloves")
                    print(i)
                    self.gloveq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.gloveq[0].armor
                    self.luck += self.gloveq[0].luck
                    self.stamina += self.gloveq[0].stamina
                    self.iq += self.gloveq[0].iq
                    self.agi += self.gloveq[0].agi
                else:
                    print("you are wearing a pair of gloves")
                    print(self.gloveq[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your gloves")
                            self.deff -= self.gloveq[0].armor
                            self.luck -= self.gloveq[0].luck
                            self.stamina -= self.gloveq[0].stamina
                            self.iq -= self.gloveq[0].iq
                            self.agi -= self.gloveq[0].agi
                            self.gloveq.remove(self.gloveq[0])
                            self.gloveq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.gloveq[0].armor
                            self.luck += self.gloveq[0].luck
                            self.stamina += self.gloveq[0].stamina
                            self.iq += self.gloveq[0].iq
                            self.agi += self.gloveq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_helm(self):
        for i in self.inventory:
            x = type(i)
            if "Helm" in str(x):
                if len(self.helmeq) < 1:
                    print("you equiped a Helmet")
                    print(i)
                    self.helmeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.helmeq[0].armor
                    self.luck += self.helmeq[0].luck
                    self.stamina += self.helmeq[0].stamina
                    self.iq += self.helmeq[0].iq
                    self.agi += self.helmeq[0].agi
                else:
                    print("you are wearing a helmet")
                    print(self.helmeq[0])
                    print("would you like to replace it with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your helmet")
                            self.deff -= self.helmeq[0].armor
                            self.luck -= self.helmeq[0].luck
                            self.stamina -= self.helmeq[0].stamina
                            self.iq -= self.helmeq[0].iq
                            self.agi -= self.helmeq[0].agi
                            self.helmeq.remove(self.helmeq[0])
                            self.helmeq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.helmeq[0].armor
                            self.luck += self.helmeq[0].luck
                            self.stamina += self.helmeq[0].stamina
                            self.iq += self.helmeq[0].iq
                            self.agi += self.helmeq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_chest(self):
        for i in self.inventory:
            x = type(i)
            if "Chest" in str(x):
                if len(self.chesteq) < 1:
                    print("you equiped a chest")
                    print(i)
                    self.chesteq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.chesteq[0].armor
                    self.luck += self.chesteq[0].luck
                    self.stamina += self.chesteq[0].stamina
                    self.iq += self.chesteq[0].iq
                    self.agi += self.chesteq[0].agi
                else:
                    print("you are wearing a chest")
                    print(self.chesteq[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your chest")
                            self.deff -= self.chesteq[0].armor
                            self.luck -= self.chesteq[0].luck
                            self.stamina -= self.chesteq[0].stamina
                            self.iq -= self.chesteq[0].iq
                            self.agi -= self.chesteq[0].agi
                            self.chseteq.remove(self.chesteq[0])
                            self.chesteq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.chesteq[0].armor
                            self.luck += self.chesteq[0].luck
                            self.stamina += self.chesteq[0].stamina
                            self.iq += self.chesteq[0].iq
                            self.agi += self.chesteq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_legs(self):
        for i in self.inventory:
            x = type(i)
            if "Legs" in str(x):
                if len(self.legeq) < 1:
                    print("you equiped a set of legs")
                    print(i)
                    self.legeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.legeq[0].armor
                    self.luck += self.legeq[0].luck
                    self.stamina += self.legeq[0].stamina
                    self.iq += self.legeq[0].iq
                    self.agi += self.legeq[0].agi
                else:
                    print("you are wearing legs")
                    print(self.legeq[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your legs")
                            self.deff -= self.legeq[0].armor
                            self.luck -= self.legeq[0].luck
                            self.stamina -= self.legeq[0].stamina
                            self.iq -= self.legeq[0].iq
                            self.agi -= self.legeq[0].agi
                            self.legeq.remove(self.legeq[0])
                            self.legeq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.legeq[0].armor
                            self.luck += self.legeq[0].luck
                            self.stamina += self.legeq[0].stamina
                            self.iq += self.legeq[0].iq
                            self.agi += self.legeq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_boots(self):
        for i in self.inventory:
            x = type(i)
            if "Boots" in str(x):
                if len(self.bootseq) < 1:
                    print("you equiped a set of boots")
                    print(i)
                    self.bootseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.bootseq[0].armor
                    self.luck += self.bootseq[0].luck
                    self.stamina += self.bootseq[0].stamina
                    self.iq += self.bootseq[0].iq
                    self.agi += self.bootseq[0].agi
                else:
                    print("you are wearing a pair of boots")
                    print(self.bootseq[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your boots")
                            self.deff -= self.bootseq[0].armor
                            self.luck -= self.bootseq[0].luck
                            self.stamina -= self.bootseq[0].stamina
                            self.iq -= self.bootseq[0].iq
                            self.agi -= self.bootseq[0].agi
                            self.bootseq.remove(self.bootseq[0])
                            self.bootseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.bootseq[0].armor
                            self.luck += self.bootseq[0].luck
                            self.stamina += self.bootseq[0].stamina
                            self.iq += self.bootseq[0].iq
                            self.agi += self.bootseq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equip_weapon(self):
        for i in self.inventory:
            try:
                if i.eq_type == "Weapon":
                    while True:
                        x = input("would you like to equip the weapon in your right or left hand")
                        if x == "right":
                            if len(self.righthandweq) < 1:
                                print("you equiped a weapon in your right hand")
                                print(i)
                                self.righthandweq.append(i)
                                self.inventory.remove(i)
                                self.atk += self.righthandweq[0].atk
                                self.luck += self.righthandweq[0].luck
                                self.stamina += self.righthandweq[0].stamina
                                self.iq += self.righthandweq[0].iq
                                self.agi += self.righthandweq[0].agi
                                break
                            else:
                                print("you already have a weapon in that hand")
                                print(self.righthandweq[0])
                                print("would you like to replace it with")
                                print(i)
                                while True:
                                    x = input("yes or no")
                                    if x == "yes":
                                        self.atk -= self.righthandweq[0].damage
                                        self.luck -= self.righthandweq[0].luck
                                        self.stamina -= self.righthandweq[0].stamina
                                        self.iq -= self.righthandweq[0].iq
                                        self.agi -= self.righthandweq[0].agi
                                        self.righthandweq.append(i)
                                        self.inventory.remove(i)
                                        self.atk += self.righthandweq[0].damage
                                        self.luck += self.righthandweq[0].luck
                                        self.stamina += self.righthandweq[0].stamina
                                        self.iq += self.righthandweq[0].iq
                                        self.agi += self.righthandweq[0].agi
                                        break
                                    elif x == "no":
                                        break
                                    break

                        elif x == "left":
                                if len(self.lefthandweq) < 1:
                                    print("you equiped a weapon in your left hand")
                                    print(i)
                                    self.lefthandweq.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.lefthandweq[0].damage
                                    self.luck += self.lefthandweq[0].luck
                                    self.stamina += self.lefthandweq[0].stamina
                                    self.iq += self.lefthandweq[0].iq
                                    self.agi += self.lefthandweq[0].agi
                                    break
                                else:
                                    print("you already have a weapon in that hand")
                                    print(self.lefthandweq[0])
                                    print("would you like to replace it with")
                                    print(i)
                                    while True:
                                        x = input("yes or no")
                                        if x == "yes":
                                            self.atk -= self.lefthandweq[0].damage
                                            self.luck -= self.lefthandweq[0].luck
                                            self.stamina -= self.lefthandweq[0].stamina
                                            self.iq -= self.lefthandweq[0].iq
                                            self.agi -= self.lefthandweq[0].agi
                                            self.lefthandweq.append(i)
                                            self.inventory.remove(i)
                                            self.atk += self.lefthandweq[0].damage
                                            self.luck += self.lefthandweq[0].luck
                                            self.stamina += self.lefthandweq[0].stamina
                                            self.iq += self.lefthandweq[0].iq
                                            self.agi += self.lefthandweq[0].agi
                                            break
                                        elif x == "no":
                                            break
                                        break

            except:
                pass

    def equip_all(self):
        self.equip_helm()
        self.equip_legs()
        self.equip_chest()
        self.equip_boots()
        self.equip_gloves()
        self.equip_weapon()

    def unequip_all(self):
        try:
            self.add_to_inv(self.helmeq.pop(0))
            self.add_to_inv(self.chesteq.pop(0))
            self.add_to_inv(self.legeq.pop(0))
            self.add_to_inv(self.bootseq.pop(0))
            self.add_to_inv(self.gloveq.pop(0))
            self.add_to_inv(self.righthandweq.pop(0))
            self.add_to_inv(self.lefthandweq.pop(0))
        except:
            pass

    def attack(self):
        roll1 = random.randint(1,6)
        if roll1 == 1:
            print("miss")
            return 0
        else:
            crit_chance = 10000%(2500-self.luck)
            roll2 = random.randint(0,crit_chance)
            print(1/crit_chance)
            x = input("what do you want to do 1 attack 2 health potion or 3 for a mana potion")
            if int(x) == 1:
                if self.player_class == "Warrior":
                    attk = (((self.atk + self.stamina) * roll1) * .1)
                    if roll2 == 1:
                        attk = attk * 2
                elif self.player_class == "Mage" and mana > 0:
                    attk = (((self.atk + self.iq) * roll1) * .1)
                    self.mana -= 5
                    if roll2 == 1:
                        attk = attk * 2
                elif self.player_class == "Hunter":
                    attk = (((self.atk + self.agi) * roll1) *.1)
                    if roll2 == 1:
                        attk = attk * 2
            elif x == 2:
                self.use_hp_potion()
                attk = 0
            elif x == 3:
                self.use_mana_potion()
                attk = 0
        print(self.name, "did", attk, "damage")
        return attk

    def defend(self, damage):
        dmg = damage
        roll = random.randint(1,6)
        if roll == 7:
            print("blocked")
            dmg = 0
        roll = random.randint(1,6)
        if self.player_class == "Warrior":
            block = ((self.deff + self.agi) * roll) * .1

        elif self.player_class == "Mage":
            block = ((self.deff + self.luck)* roll) * .1
        elif self.player_class == "Hunter":
            block = ((self.deff + self.stamina) * roll) * .1

        else:
            block = ((self.deff + self.iq) * roll) * .1
        print(self.name, "blocked", block, "damage")
        dmgdelt = dmg - block
        if dmgdelt >= 0:
            self.hp = self.hp - dmgdelt
        if self.hp <= 0:
            self.is_alive = False

    def use_hp_potion(self):
        for i in self.inventory:
            if i == "Health potion":
                print("you healed", str(self.max_health - self.hp), "hp")
                self.hp = self.max_health
                self.inventory.remove(i)
                return

    def use_mana_potion(self):
        for i in self.inventory:
            if i == "Mana potion":
                print("you recovered", str(self.max_mana - self.mana), "mana")
                self.mana = self.max_mana
                self.inventory.remove(i)
                return