import random

class Character:
    def __init__(self, job, level, hp, mp, str, dex, luk, int, fresh_ap, stale_ap, int_from_items):
        self.job = job
        self.level = level
        self.hp = hp
        self.mp = mp
        self.str = str
        self.dex = dex
        self.luk = luk
        self.int = int
        self.fresh_ap = fresh_ap
        self.stale_ap = stale_ap
        self.resets_used = 0

        if self.job == "magician":
            self.lvl_up_hp_gain_limits = (10, 14)
            self.lvl_up_mp_gain_limits = (22, 24)
            self.fresh_ap_hp_gain_limits = (6, 10)
            self.fresh_ap_mp_gain = 18
            self.mp_lost_from_resetting = 30

        elif self.job == "spearman" or self.job == "figher" or self.job == "page":
            self.lvl_up_hp_gain_limits = (24, 28)
            self.lvl_up_mp_gain_limits = (4, 6)
            self.fresh_ap_hp_gain_limits = (20, 24)
            self.fresh_ap_mp_gain = 2
            self.mp_lost_from_resetting = 4

        elif self.job == "buccaneer":
            self.lvl_up_hp_gain_limits = (22, 28)
            self.lvl_up_mp_gain_limits = (18, 23)
            self.fresh_ap_hp_gain_limits = (16, 20)
            self.fresh_ap_mp_gain = 14
            self.mp_lost_from_resetting = 16

        self.minimum_mp = self.calculate_minimum_mp()

        self.int_from_items = int_from_items

    def __str__(self):
        ret = ''
        ret += '==============================================\n'
        ret += f"Level: {self.level}\n"
        ret += f"Fresh AP: {self.fresh_ap}\n"
        ret += f"Stale AP: {self.stale_ap}\n"
        ret += f"Resets used: {self.resets_used} ({self.resets_used * 3100} NX)\n"
        ret += f"{(self.resets_used * 3100)/5000} days of voting\n"
        ret += f"\n"
        ret += f"HP: {self.hp}\n"
        ret += f"MP: {self.mp}\n"
        ret += f"Excess MP: {self.mp - self.minimum_mp}\n"
        ret += f"Washes Possible: {int((self.mp - self.minimum_mp)/self.mp_lost_from_resetting)} -- yields approx. {int((self.fresh_ap_hp_gain_limits[0] + self.fresh_ap_hp_gain_limits[1])/2)*(int((self.mp - self.minimum_mp)/16))} HP\n"
        ret += f"\n"
        ret += f"STR: {self.str}\n"
        ret += f"DEX: {self.dex}\n"
        ret += f"INT: {self.int + self.int_from_items} ({self.int}+{self.int_from_items})\n"
        ret += f"LUK: {self.luk}\n"
        ret += '=============================================='
        return ret

    def level_up(self):
        if self.level >= 200:
            print('Max level')
            return

        self.level += 1
        self.fresh_ap += 5
        self.minimum_mp = self.calculate_minimum_mp()

        if self.job == "magician":
            # Job advancement Bonus
            if self.level == 30:
                self.mp += random.randint(100, 150)
            if self.level == 70:
                self.mp += random.randint(450, 500)

            # Improved MaxMP increase skill maxed
            if self.level >= 13:
                self.lvl_up_mp_gain_limits = (42, 44)

        if self.job == "spearman":
            # Job advancement Bonus
            if self.level == 30:
                self.hp += random.randint(200, 250)
            if self.level == 70:
                self.mp += random.randint(100, 150)

            # Improved MaxHP increase skill maxed
            if self.level >= 15:
                self.lvl_up_hp_gain_limits = (64, 68)
                self.fresh_ap_hp_gain_limits = (50, 54)

        if self.job == "fighter":
            # Job advancement Bonus
            if self.level == 30:
                self.hp += random.randint(200, 250)
            if self.level == 70:
                self.hp += random.randint(300, 350)

            # Improved MaxHP increase skill maxed
            if self.level >= 15:
                self.lvl_up_hp_gain_limits = (64, 68)
                self.fresh_ap_hp_gain_limits = (50, 54)

        if self.job == "page":
            # Job advancement Bonus
            if self.level == 30:
                self.hp += random.randint(200, 250)
            if self.level == 70:
                self.mp += random.randint(100, 150)

            # Improved MaxHP increase skill maxed
            if self.level >= 15:
                self.lvl_up_hp_gain_limits = (64, 68)
                self.fresh_ap_hp_gain_limits = (50, 54)

        if self.job == "buccaneer":
            # Job advancement Bonus
            if self.level == 30:
                self.hp += random.randint(100, 150) + random.randint(25, 50)
            if self.level == 70:
                self.hp += random.randint(200, 250)
                self.mp += random.randint(150, 175)

            # Improve MaxHP skill maxed
            if self.level >= 33:
                self.lvl_up_hp_gain_limits = (52, 58)
                self.fresh_ap_hp_gain_limits = (36, 40)

        self.hp += random.randint(self.lvl_up_hp_gain_limits[0], self.lvl_up_hp_gain_limits[1])
        self.mp += random.randint(self.lvl_up_mp_gain_limits[0], self.lvl_up_mp_gain_limits[1]) + int(self.calculate_total_int_with_mw(10) / 10)


    def add_fresh_ap(self, stat, val):
        for i in range(val):
            if self.fresh_ap <= 0:
                print('No fresh AP remaining')
                return

            if stat == 'str':
                self.str += 1
            elif stat == 'dex':
                self.dex += 1
            elif stat == 'luk':
                self.luk += 1
            elif stat == 'int':
                self.int += 1
            elif stat == 'hp':
                self.hp += random.randint(self.fresh_ap_hp_gain_limits[0], self.fresh_ap_hp_gain_limits[1])
            elif stat == 'mp':
                self.mp += self.fresh_ap_mp_gain + int(self.int / 10)

            self.fresh_ap -= 1

    def add_stale_ap(self, stat, val):
        for i in range(val):
            if self.stale_ap <= 0:
                print('No stale AP remaining')
                return

            if stat == 'str':
                self.str += 1
            elif stat == 'dex':
                self.dex += 1
            elif stat == 'luk':
                self.luk += 1
            elif stat == 'int':
                self.int += 1
            elif stat == 'hp':
                self.hp += 18
            elif stat == 'mp':
                self.mp += 14

            self.stale_ap -= 1

    def sim_ap_reset(self, stat, val):
        for i in range(val):
            if stat == 'str':
                if self.str <= 4:
                    print(f'AP reset #{i}: Already at minimum STR')
                    return
                self.str -= 1
            elif stat == 'dex':
                if self.dex <= 4:
                    print(f'AP reset #{i}: Already at minimum DEX')
                    return
                self.dex -= 1
            elif stat == 'luk':
                if self.luk <= 4:
                    print(f'AP reset #{i}: Already at minimum LUK')
                    return
                self.luk -= 1
            elif stat == 'int':
                if self.int <= 4:
                    print(f'AP reset #{i}: Already at minimum INT')
                    return
                self.int -= 1
            elif stat == 'mp':
                if self.mp - self.mp_lost_from_resetting < self.minimum_mp:
                    print(f'AP reset #{i}: Already at minimum MP')
                    return
                self.mp -= self.mp_lost_from_resetting

            self.stale_ap += 1
            self.resets_used += 1
    
    def set_int_from_items(self, val):
        self.int_from_items = val

    def calculate_minimum_mp(self):
        if self.job == "magician":
            if self.level < 30:
                return 22 * self.level - 1
            else:
                return 22 * self.level + 449
        
        elif self.job == "spearman":
            return 4 * self.level + 155
        elif self.job == "fighter":
            return 4 * self.level + 55
        elif self.job == "page":
            return 4 * self.level + 155

        elif self.job == "buccaneer":
            return 18 * self.level + 95 
        

    # set val to MW level (only supports 10 and 20)
    def calculate_total_int_with_mw(self, val):
        if val <= 10:
            return int(self.int + self.int_from_items + ((self.int + self.int_from_items)*0.05))

        elif val >= 20:
            return int(self.int + self.int_from_items + ((self.int + self.int_from_items)*0.10))



def buccTo30kPlan():
    c = Character("buccaneer", 62, 3071, 1674, 185, 26, 4, 110, 5, 0, 68)

    print("Phinkz currently:")
    print(str(c))
    print("Start with moving 20 STR to INT and HP wash our 5 fresh AP")

    start_val = 20
    c.sim_ap_reset("str", start_val)
    c.add_stale_ap("int", start_val)
    
    c.add_fresh_ap("hp", 5)
    c.sim_ap_reset("mp", 5)
    c.add_stale_ap("int", 5)
    print(str(c))

    print("For 5 levels HP wash moving points from MP to INT")
    for i in range(5):
        c.level_up()
        c.add_fresh_ap("hp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("int", 5)
    print(str(c))
        
    print("For 35 levels MP wash moving points from MP to INT")
    for i in range(35):
        c.level_up()
        c.add_fresh_ap("mp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("int", 5)
    print(str(c))

    print("From level 102 to level 150 standard HP wash moving points from MP to STR")
    while c.mp - 16 >= c.minimum_mp and c.level < 150:
        c.level_up()
        c.add_fresh_ap("hp", 5)
        # c.sim_ap_reset("mp", 5)
        # c.add_stale_ap("str", 5)
    print(str(c))
    
    print("At 150 we can start removing INT whenever")
    while(c.int > 4):
        c.sim_ap_reset("int", 1)
        c.add_stale_ap("str", 1)
    print(str(c))
    
    print("Continue HP washing until we run out of excess MP")
    while c.mp - 16 >= c.minimum_mp and c.level < 200:
        c.level_up()
        c.add_fresh_ap("hp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("str", 5)

        if c.level == 185:
            print("This is what our char will look like at 185")
            print(str(c))
    print(str(c))

    while c.level < 200:
        c.level_up()
        c.add_fresh_ap("str", 5)

    while c.mp - 16 >= c.minimum_mp:
        c.sim_ap_reset("mp", 1)
        c.add_stale_ap("str", 1)

    print(str(c))






def buccLessWork():
    c = Character("buccaneer", 62, 3071, 1674, 185, 26, 4, 110, 5, 0, 68)
    print(str(c))


    start_val = 20
    c.sim_ap_reset("str", start_val)
    c.add_stale_ap("int", start_val)

    for i in range(5):
        # c.level_up()
        c.add_fresh_ap("hp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("int", 5)
    print(str(c))

    for i in range(25):
        c.level_up()
        c.add_fresh_ap("mp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("int", 5)
    print(str(c))

    while c.mp - 16 >= c.minimum_mp and c.level < 200:
        c.level_up()
        c.add_fresh_ap("hp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("str", 5)
    print(str(c))

    while(c.int > 4):
        c.sim_ap_reset("int", 1)
        c.add_stale_ap("str", 1)
    print(str(c))

    while(c.level < 200):
        c.level_up()
    print(str(c))


def main():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    buccLessWork()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    buccTo30kPlan()

if __name__ == "__main__":
    main()
