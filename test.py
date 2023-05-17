from mscharacter import Character

def buccTo30kPlan():
    c = Character("buccaneer", 62, 3071, 1674, 185, 26, 4, 110, 5, 0, 0, 68)

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
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("str", 5)
    print(str(c))
    
    print("At 150 we can start removing INT whenever")
    while(c.int > 4):
        c.sim_ap_reset("int", 1)
        c.add_stale_ap("str", 1)
    print(str(c))
    
    print("Continue HP washing until we run out of excess MP")
    c.level_up()
    c.add_fresh_ap("hp", 1)
    for i in range(27):
        c.sim_ap_reset("mp", 1)
        c.add_stale_ap("hp", 1)

    while c.mp - 16 >= c.minimum_mp and c.level < 200:
        c.level_up()
        c.add_fresh_ap("hp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("str", 5)
    print(str(c))

    while c.level < 200:
        c.level_up()
        c.add_fresh_ap("str", 5)

    while c.mp - 16 >= c.minimum_mp and c.ap_in_hp_mp_pool > 0:
        c.sim_ap_reset("mp", 1)
        c.add_stale_ap("str", 1)

    print(str(c))

    print('\nWash instructions:\n')
    print('\t1.) Move 20 points from STR to INT and use our 5 fresh ap for HP wash APR -MP +INT')
    print('\t2.) For 35 levels (lvl 62 - lvl 102) MP wash with fresh AP put into MP then using APR for -MP +INT')
    print('\t3.) From lvl 102 - lvl 150 standard HP wash with fresh AP put into HP then using APR for -MP +STR')
    print('\t4.) At 150 we can reset INT to STR')
    print('\t5.) HP wash the rest of your levels with fresh AP put into HP and APR for -MP +STR. Can get away with 27 stale washes (eg. APR -MP +HP allowing for 5 levels where fresh AP is put into STR)')
    

def NLtest():
    c = Character("thief", 33, 1176, 798, 5, 25, 30, 126, 0, 0, 0, 60)  

    # Pump INT till 200 Base
    for i in range (15):
        c.level_up()
        c.add_fresh_ap("int", 5)
    print(str(c))

    # MP wash with AP reset going towards INT until base of 400 int
    while c.int < 400:
        c.level_up()
        c.add_fresh_ap("mp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("int", 5)
    print(str(c))

    # MP wash with AP reset going towards LUK
    while c.level < 150:
        c.level_up()
        c.add_fresh_ap("mp", 5)
        c.sim_ap_reset("mp", 5)
        c.add_stale_ap("luk", 5)
    print(str(c))

    # Reset INT into LUK
    while c.int > 4:
        c.sim_ap_reset("int", 1)
        c.add_stale_ap("luk", 1)
    print(str(c))

    print("At this point we have enough excess MP to fully stale HP wash (assuming we had enough NX)")
    print("Can do a mix of stale washes or fresh HP washes with -MP +LUK")

    c.level_up()
    c.add_fresh_ap("hp", 5)
    while c.mp - c.mp_lost_from_resetting > c.minimum_mp: 
        c.sim_ap_reset("mp", 1)
        c.add_stale_ap("hp", 1)
    print(str(c))

    print('\nWash instructions:\n')
    print('\t1.) Pump base INT on lvl up until 200 base INT')
    print('\t2.) First MP wash cycle with fresh AP put into MP then using AP reset for -MP +INT until 400 base INT')
    print('\t3.) Second MP wash cycle with fresh AP put into MP then using AP reset for -MP +LUK until 23150 MP')
    print('\t4.) At lvl 150 Reset Base INT to LUK (maybe some DEX if needed)')
    print('\t5.) HP wash forever, should have enough MP to stale wash to max HP. Fresh wash when possible, stale wash when possible, can also put fresh AP directly into LUK if no NX available on level up')



def main():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # NLtest()
    buccTo30kPlan()

if __name__ == "__main__":
    main()