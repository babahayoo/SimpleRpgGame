from classes.Game import bColors, Person

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bColors.FAIL + bColors.BOLD + " AN ENEMY ATTACK!" + bColors.ENDC)

while running:
    print("========")
    player.chooseAction()
    choice = input("Choose action : ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You attacked for ", dmg, ", Enemy HP current is : ", enemy.getHp())
    elif index == 1:
        player.chooseMagic()
        magicChoice = int(input("Choose Magic : ")) - 1
        magicDamage = player.generateSpellDamage(magicChoice)
        spell = player.getSpellName(magicChoice)
        cost = player.getSpellMpCost(magicChoice)

        currentMp = player.getMp()

        if cost > currentMp:
            print(bColors.FAIL + "\nNOT ENOUGH MP\n" + bColors.ENDC)
            continue
        player.reduceMp(cost)
        enemy.takeDamage(magicDamage)
        print(bColors.OKBLUE + "\n" + spell + " deals ", str(magicDamage), " points of damage" + bColors.ENDC)

    enemyChoice = 1

    enemyDamage = enemy.generateDamage()
    player.takeDamage(enemyDamage)
    print("Enemy attacks for ", enemyDamage, " Player HP : ", player.getHp())

    print("--------------------")
    print("Enemy HP : ", bColors.FAIL + str(enemy.getHp()) + "/" + str(enemy.getMaxHp()) + bColors.ENDC + "\n")

    print("Youre HP : ", bColors.OKGREEN + str(player.getHp()) + "/ " + str(player.getMaxHp()) + bColors.ENDC)
    print("Youre MP : ", bColors.OKBLUE + str(player.getMp()) + "/ " + str(player.getMaxMp()) + bColors.ENDC)

    if enemy.getHp() == 0:
        print(bColors.OKGREEN + "YOU WIN !" + bColors.ENDC)
        running = False
    elif player.getHp() == 0:
        print(bColors.FAIL + "Your enemy has defeated you" + bColors.ENDC)
        running = False
