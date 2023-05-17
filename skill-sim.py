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

        self.minimum_mp = self.calculate_minimum_mp()


        self.int_from_items = int_from_items

    def __str__(self):
        ret = ''
        ret += '==============================================\n'
        ret += f"Level: {self.level}\n"
        ret += f"Fresh AP: {self.fresh_ap}\n"
        ret += f"Stale AP: {self.stale_ap}\n"
        ret += f"Resets used: {self.resets_used}\n"
        ret += f"\n"
        ret += f"HP: {self.hp}\n"
        ret += f"MP: {self.mp}\n"
        ret += f"Excess MP: {self.mp - self.minimum_mp}\n"
        ret += f"Washes Possible: {int((self.mp - self.minimum_mp)/16)} -- yields approx. {38*(int((self.mp - self.minimum_mp)/16))} HP\n"
        ret += f"\n"
        ret += f"STR: {self.str}\n"
        ret += f"DEX: {self.dex}\n"
        ret += f"INT: {self.int + self.int_from_items} ({self.int}+{self.int_from_items})\n"
        ret += f"LUK: {self.luk}\n"
        ret += '=============================================='
        # return f"\nLevel: {self.level}\nFresh AP: {self.fresh_ap}\nStale AP: {self.stale_ap}\n\nHP: {self.hp}\nMP: {self.mp}\n\nSTR: {self.str}\nDEX: {self.dex}\nINT: {self.int + self.int_from_items} ({self.int}+{self.int_from_items})\nLUK: {self.luk}"
        return ret

    def level_up(self):
        if self.level >= 200:
            print('Max level')
            return

        self.level += 1
        self.fresh_ap += 5
        self.minimum_mp = self.calculate_minimum_mp()

        # Not accounting for job
        # Not accounting for skills (eg: brawler assumes MaxHp skill leveled)

        self.hp += random.randint(22, 28)
        self.mp += random.randint(18, 23) + int((self.int+self.int_from_items) / 10)

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
                self.hp += random.randint(36, 40)
            elif stat == 'mp':
                self.mp += 14 + int(self.int / 10)

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
                if self.mp - 16 < self.minimum_mp:
                    print(f'AP reset #{i}: Already at minimum MP')
                    return
                self.mp -= 16

            self.stale_ap += 1
            self.resets_used += 1
    
    def set_int_from_items(self, val):
        self.int_from_items = val

    def calculate_minimum_mp(self):
        if self.job == "buccaneer":
            return 18 * self.level + 95 



def main():
    c = Character("buccaneer", 62, 3071, 1674, 185, 26, 4, 110, 5, 0, 68)
    print(str(c))
    # c.add_fresh_ap("hp", 5)
    # c.sim_ap_reset("mp", 5)
    # c.add_stale_ap("int", 5)

    for i in range(10):
        c.level_up()
        c.add_fresh_ap("int", 5)

    for i in range(20):
        c.level_up()
        c.add_fresh_ap("mp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("int", 5)

    for i in range(30):
        c.level_up()
        c.add_fresh_ap("mp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("str", 5)

    # print(str(c))

    # for i in range(50):
    #     c.level_up()
    #     c.add_fresh_ap("hp", 5)
    #     c.sim_ap_reset("mp", 5)
    #     c.add_stale_ap("str", 5)

    while c.level < 185:
        c.level_up()

    print(str(c))

    # # Add base int to level 80


    # for i in range(18):
    #     c.level_up()
    #     c.add_fresh_ap("int", 5)
    # print(str(c))

    # # MP wash 50 levels to level 130
    # for i in range(30): 
    #     c.level_up()
    #     c.add_fresh_ap("mp", 5)
    #     c.sim_ap_reset("mp", 5)
    #     c.add_stale_ap("str", 5)
    # print(str(c))

    # for i in range(8):
    #     c.sim_ap_reset("mp", 5)
    # print(str(c))

    # # Fresh HP washing
    # for i in range(75):
    #     c.level_up()
    #     c.add_fresh_ap("hp", 5)
    #     c.sim_ap_reset("mp", 5)
    #     c.add_stale_ap("str", 5)
    # print(str(c))


if __name__ == "__main__":
    main()