from mscharacter import Character

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
    buccTo30kPlan()
    # c = Character("buccaneer", 62, 3071, 0, 185, 26, 4, 110, 5, 0, 68)
    # c.sim_ap_reset("mp", 1)

if __name__ == "__main__":
    main()