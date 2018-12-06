import pygame
import random
import pygame.freetype
import sys


pygame.init()




# You can look at the code if you want
# I'm not great at leaving comments for most things so sorry
# Alpha V1.00


DisplayWidth,DisplayHeight = 1000, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
game_font = pygame.freetype.Font("Font.ttf", 24)
pygame.display.set_caption("Monster Clash")

def MainScreen():
    run = True
    Lvl = "main"

    while run is True:
        gameDisplay.fill((144, 155, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Lvl == "main":
                    if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                        run = False
                    if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                        Lvl = "credits"
                if Lvl == "credits":
                    if pos[0] > 725 and pos[0] < 925 and pos[1] > 660 and pos[1] < 710:
                        Lvl = "main"
        pos = pygame.mouse.get_pos()

        if Lvl == "main":

            game_font = pygame.freetype.Font("Font.ttf", 100)

            text_surface, rect = game_font.render(("Monster Clash"), (0, 0, 0))
            gameDisplay.blit(text_surface, (240, 100))

            game_font = pygame.freetype.Font("Font.ttf", 50)

            text_surface, rect = game_font.render(("Alpha 1.00"), (0, 0, 0))
            gameDisplay.blit(text_surface, (400, 200))

            game_font = pygame.freetype.Font("Font.ttf", 24)

            if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (250, 460, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (250, 460, 200, 100), 0)

            if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (500, 460, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (500, 460, 200, 100), 0)

            text_surface, rect = game_font.render(("Play"), (0, 0, 0))
            gameDisplay.blit(text_surface, (325, 500))

            text_surface, rect = game_font.render(("Credits"), (0, 0, 0))
            gameDisplay.blit(text_surface, (575, 500))
        if Lvl == "credits":
            pos = pygame.mouse.get_pos()
            if pos[0] > 725 and pos[0] < 925 and pos[1] > 660 and pos[1] < 710:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (750, 660, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (750, 660, 200, 100), 0)

            game_font = pygame.freetype.Font("Font.ttf", 75)

            text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
            gameDisplay.blit(text_surface, (150, 300))

            text_surface, rect = game_font.render(("Beta Tester/Helper: Shinta"), (0, 0, 0))
            gameDisplay.blit(text_surface, (150, 450))

            game_font = pygame.freetype.Font("Font.ttf", 24)

            text_surface, rect = game_font.render(("Back"), (0, 0, 0))
            gameDisplay.blit(text_surface, (825, 700))

        pygame.display.update()
        clock.tick(30)

def MonsterGen():
    global Skill
    MonsterStats = {}
    MonsterStats["Health"] = int(random.randint(75,125) * Skill)
    MonsterStats["Attack"] = int(random.randint(7,12) * Skill)
    MonsterStats["Speed"] = int(random.randint(75,125) * Skill)
    MonsterStats["Magic"] = int(random.randint(7,12) * Skill)
    MonsterStats["GoldWorth"] = MonsterStats["Health"] + MonsterStats["Speed"] + MonsterStats["Attack"] + MonsterStats["Magic"]
    MonsterStats["MaxHealth"] = MonsterStats["Health"]
    return MonsterStats
def game_loop():
    global Skill
    game_run = True

    Skill = 0.25

    Stats = {}
    Stats["Health"] = random.randint(75,125)
    Stats["Attack"] = random.randint(7,12)
    Stats["Speed"] = random.randint(75,125)
    Stats["Magic"] = random.randint(7,12)
    OldHealth = Stats["Health"]
    Monster = MonsterGen()
    MonsterOldHealth = Monster["Health"]
    MonsterDead = False
    MonsterDead2 = False
    fight = True
    attack = False
    magicAttack = False
    PlayerDead = False
    msgType = ""
    msg = ""
    msg2 = ""
    Levels = [1,1,1,1]
    PlyrAcc = 90
    MagicType = ""
    Class = ""
    Auto = False

    gold = 0
    HealthItems = [["Health Canister", "Iron Armor", "Iridium Armor"], [500, 2500, 15000]]
    AttackItems = [["Iron Sword", "Giant Sword", "Dark Pulser"], [500, 2500, 15000]]
    SpeedItems = [["Running Shoes", "Winged Sandals", "Teleportation"], [500, 2500, 15000]]
    MagicItems = [["Small Wand", "Gandalf's Staff", "Chony's Staff"], [500, 2500, 15000]]
    MiscItems = [["Less Missing", "Change Magic Type", "OP Late Game Buff"], [15000, 5000, 3000000]]

    MainScreen()


    MagicSetup = True

    while MagicSetup == True:
        gameDisplay.fill((144, 155, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                    MagicType = "Healing"
                    MagicSetup = False
                if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                    MagicType = "Damage"
                    MagicSetup = False
        pos = pygame.mouse.get_pos()

        text_surface, rect = game_font.render(("What magic type do you want?"), (0, 0, 0))
        gameDisplay.blit(text_surface, (350, 300))

        if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (250, 460, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (250, 460, 200, 100), 0)

        if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (500, 460, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (500, 460, 200, 100), 0)

        text_surface, rect = game_font.render(("Healing"), (0, 0, 0))
        gameDisplay.blit(text_surface, (325, 500))

        text_surface, rect = game_font.render(("Damage"), (0, 0, 0))
        gameDisplay.blit(text_surface, (575, 500))

        pygame.display.update()
        clock.tick(30)

    Setup = True

    while Setup is True:
        gameDisplay.fill((144, 155, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 75 and pos[0] < 275 and pos[1] > 640 and pos[1] < 740:
                    Class = "Tank"
                    Stats["Health"] += 50
                    Setup = False


                if pos[0] > 375 and pos[0] < 575 and pos[1] > 640 and pos[1] < 740:
                    Class = "Knight"
                    Stats["Health"] += 10
                    Stats["Attack"] += 8
                    Setup = False

                if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
                    Class = "Scout"
                    Stats["Speed"] += 15
                    Setup = False
                if pos[0] > 75 and pos[0] < 275 and pos[1] > 440 and pos[1] < 540:
                    Class = "Wizard"
                    Stats["Magic"] += 15
                    Stats["Health"] -= 20
                    Setup = False
                if pos[0] > 375 and pos[0] < 575 and pos[1] > 440 and pos[1] < 540:
                    Class = "Swordsman"
                    Stats["Speed"] += 10
                    Stats["Attack"] += 5
                    Setup = False
        pos = pygame.mouse.get_pos()

        if pos[0] > 75 and pos[0] < 275 and pos[1] > 640 and pos[1] < 740:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (75, 650, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (75, 650, 200, 100), 0)

        if pos[0] > 375 and pos[0] < 575 and pos[1] > 640 and pos[1] < 740:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (375, 650, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (375, 650, 200, 100), 0)

        if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 650, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 650, 200, 100), 0)

        if pos[0] > 75 and pos[0] < 275 and pos[1] > 440 and pos[1] < 540:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (75, 450, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (75, 450, 200, 100), 0)

        if pos[0] > 375 and pos[0] < 575 and pos[1] > 440 and pos[1] < 540:
            pygame.draw.rect(gameDisplay, (100, 0, 0), (375, 450, 200, 100), 0)
        else:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (375, 450, 200, 100), 0)

        text_surface, rect = game_font.render(("What Class do you want?"), (0, 0, 0))
        gameDisplay.blit(text_surface, (400, 100))

        text_surface, rect = game_font.render(("Tank"), (0, 0, 0))
        gameDisplay.blit(text_surface, (150, 690))

        text_surface, rect = game_font.render(("Knight"), (0, 0, 0))
        gameDisplay.blit(text_surface, (450, 690))

        text_surface, rect = game_font.render(("Scout"), (0, 0, 0))
        gameDisplay.blit(text_surface, (775, 690))

        text_surface, rect = game_font.render(("Wizard"), (0, 0, 0))
        gameDisplay.blit(text_surface, (145, 490))

        text_surface, rect = game_font.render(("Swordsman"), (0, 0, 0))
        gameDisplay.blit(text_surface, (430, 490))



        pygame.display.update()
        clock.tick(30)

    OldHealth = Stats["Health"]


    while game_run == True:

        gameDisplay.fill((144, 155, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if fight == True:
                    pos = pygame.mouse.get_pos()

                    if pos[0] > 350 and pos[0] < 550 and pos[1] > 450 and pos[1] < 550:
                        attack = True
                    if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                        magicAttack = True
                else:
                    if MonsterDead == True:
                        Stats["Health"] = OldHealth
                        if pos[0] > 50 and pos[0] < 250 and pos[1] > 640 and pos[1] < 740:
                            Levels[0] += 1
                            Stats["Health"] = int(Stats["Health"]*1.5)
                            OldHealth = int(OldHealth * 1.5)
                            MonsterDead2 = True
                            MonsterDead = False
                        if pos[0] > 350 and pos[0] < 550 and pos[1] > 640 and pos[1] < 740:
                            Levels[1] += 1
                            Stats["Attack"] = int(Stats["Attack"] * 1.5)
                            MonsterDead2 = True
                            MonsterDead = False
                        if pos[0] > 650 and pos[0] < 850 and pos[1] > 640 and pos[1] < 740:
                            Levels[2] += 1
                            Stats["Speed"] = int(Stats["Speed"] * 1.5)
                            MonsterDead2 = True
                            MonsterDead = False
                        if pos[0] > 650 and pos[0] < 850 and pos[1] > 440 and pos[1] < 540:
                            Levels[3] += 1
                            Stats["Magic"] = int(Stats["Magic"] * 1.5)
                            MonsterDead2 = True
                            MonsterDead = False




        if MonsterDead == True:
            pos = pygame.mouse.get_pos()


            text_surface, rect = game_font.render(("What do you want to upgrade?"), (0, 0, 0))
            gameDisplay.blit(text_surface, (350, 500))

            if pos[0] > 75 and pos[0] < 275 and pos[1] > 640 and pos[1] < 740:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (75, 650, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (75, 650, 200, 100), 0)

            if pos[0] > 375 and pos[0] < 575 and pos[1] > 640 and pos[1] < 740:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (375, 650, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (375, 650, 200, 100), 0)

            if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 650, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 650, 200, 100), 0)

            if pos[0] > 700 and pos[0] < 900 and pos[1] > 440 and pos[1] < 540:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 450, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 450, 200, 100), 0)

            text_surface, rect = game_font.render(("Level " + str(Levels[0]) + " Health"), (0, 0, 0))
            gameDisplay.blit(text_surface, (120, 690))

            text_surface, rect = game_font.render(("Level " + str(Levels[1]) + " Attack"), (0, 0, 0))
            gameDisplay.blit(text_surface, (420, 690))

            text_surface, rect = game_font.render(("Level " + str(Levels[2]) + " Speed"), (0, 0, 0))
            gameDisplay.blit(text_surface, (745, 690))

            text_surface, rect = game_font.render(("Level " + str(Levels[3]) + " Magic"), (0, 0, 0))
            gameDisplay.blit(text_surface, (745, 490))


        if MonsterDead2 == True:
            gold += Monster["GoldWorth"]
            Skill = Skill * 1.25
            Monster = MonsterGen()
            MonsterOldHealth = Monster["Health"]
            fight = True
            MonsterDead2 = False

            choosing = True
            while choosing == True:
                gameDisplay.fill((144, 155, 220))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                            Shop = True
                            choosing = False
                        if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                            Shop = False
                            choosing = False

                text_surface, rect = game_font.render(("Do you want to go to the shop?"), (0, 0, 0))
                gameDisplay.blit(text_surface, (350, 300))
                text_surface, rect = game_font.render(("Gold: " + str(gold)), (0, 0, 0))
                gameDisplay.blit(text_surface, (420, 330))

                pos = pygame.mouse.get_pos()

                if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                    pygame.draw.rect(gameDisplay, (100, 0, 0), (250, 460, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (250, 460, 200, 100), 0)

                if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                    pygame.draw.rect(gameDisplay, (100, 0, 0), (500, 460, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (500, 460, 200, 100), 0)

                text_surface, rect = game_font.render(("Yes"), (0, 0, 0))
                gameDisplay.blit(text_surface, (325, 500))

                text_surface, rect = game_font.render(("No"), (0, 0, 0))
                gameDisplay.blit(text_surface, (575, 500))

                pygame.display.update()
                clock.tick(30)

            #Shopping
            ShopLevel = "Main"
            while Shop == True:


                gameDisplay.fill((144, 155, 220))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if ShopLevel == "Main":
                            if pos[0] > 75 and pos[0] < 275 and pos[1] > 640 and pos[1] < 740:
                                ShopLevel = "Health"

                            if pos[0] > 375 and pos[0] < 575 and pos[1] > 640 and pos[1] < 740:
                                ShopLevel = "Attack"

                            if pos[0] > 700 and pos[0] < 900 and pos[1] > 440 and pos[1] < 540:
                                ShopLevel = "Speed"

                            if pos[0] > 75 and pos[0] < 275 and pos[1] > 440 and pos[1] < 540:
                                ShopLevel = "Magic"

                            if pos[0] > 375 and pos[0] < 575 and pos[1] > 440 and pos[1] < 540:
                                ShopLevel = "Misc"

                            if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
                                Shop = False
                        if ShopLevel != "Main":
                            if pos[0] > 75 and pos[0] < 275 and pos[1] > 440 and pos[1] < 540:
                                if ShopLevel == "Health" and HealthItems[1][0] != "bought":
                                    if gold >= HealthItems[1][0]:
                                        gold -= HealthItems[1][0]
                                        HealthItems[1][0] = "Bought"
                                        HealthItems[0][0] = "none"
                                        Stats["Health"] = int(Stats["Health"] * 1.4)
                                        OldHealth = Stats["Health"]
                                        Shop = False
                                if ShopLevel == "Attack" and AttackItems[1][0] != "bought":
                                    if gold >= AttackItems[1][0]:
                                        gold -= AttackItems[1][0]
                                        AttackItems[1][0] = "Bought"
                                        AttackItems[0][0] = "none"
                                        Stats["Attack"] = int(Stats["Attack"] * 1.4)
                                        Shop = False
                                if ShopLevel == "Magic" and MagicItems[1][0] != "bought":
                                    if gold >= MagicItems[1][0]:
                                        gold -= MagicItems[1][0]
                                        MagicItems[1][0] = "Bought"
                                        MagicItems[0][0] = "none"
                                        Stats["Magic"] = int(Stats["Magic"] * 1.4)
                                        Shop = False
                                if ShopLevel == "Speed" and SpeedItems[1][0] != "bought":
                                    if gold >= SpeedItems[1][0]:
                                        gold -= SpeedItems[1][0]
                                        SpeedItems[1][0] = "Bought"
                                        SpeedItems[0][0] = "none"
                                        Stats["Speed"] = int(Stats["Speed"] * 1.4)
                                        Shop = False
                                if ShopLevel == "Misc" and MiscItems[1][0] != "bought":
                                    if gold >= MiscItems[1][0]:
                                        gold -= MiscItems[1][0]
                                        MiscItems[1][0] = "Bought"
                                        MiscItems[0][0] = "none"
                                        PlyrAcc += 10
                                        Shop = False



                            if pos[0] > 375 and pos[0] < 575 and pos[1] > 440 and pos[1] < 540:
                                if ShopLevel == "Health" and HealthItems[1][1] != "bought":
                                    if gold >= HealthItems[1][1]:
                                        gold -= HealthItems[1][1]
                                        HealthItems[1][1] = "Bought"
                                        HealthItems[0][1] = "none"
                                        Stats["Health"] = int(Stats["Health"] * 2)
                                        OldHealth = Stats["Health"]
                                        Shop = False
                                if ShopLevel == "Attack" and AttackItems[1][1] != "bought":
                                    if gold >= AttackItems[1][1]:
                                        gold -= AttackItems[1][1]
                                        AttackItems[1][1] = "Bought"
                                        AttackItems[0][1] = "none"
                                        Stats["Attack"] = int(Stats["Attack"] * 2)
                                        Shop = False
                                if ShopLevel == "Magic" and MagicItems[1][1] != "bought":
                                    if gold >= MagicItems[1][1]:
                                        gold -= MagicItems[1][1]
                                        MagicItems[1][1] = "Bought"
                                        MagicItems[0][1] = "none"
                                        Stats["Magic"] = int(Stats["Magic"] * 2)
                                        Shop = False
                                if ShopLevel == "Speed" and SpeedItems[1][1] != "bought":
                                    if gold >= SpeedItems[1][1]:
                                        gold -= SpeedItems[1][1]
                                        SpeedItems[1][1] = "Bought"
                                        SpeedItems[0][1] = "none"
                                        Stats["Speed"] = int(Stats["Speed"] * 2)
                                        Shop = False
                                if ShopLevel == "Misc" and MiscItems[1][1] != "bought":
                                    if gold >= MiscItems[1][1]:
                                        gold -= MiscItems[1][1]
                                        MiscItems[1][1] = "Bought"
                                        MiscItems[0][1] = "none"
                                        if MagicType == "Healing":
                                            MagicType = "Damage"
                                        else:
                                            MagicType = "Healing"

                                        Shop = False


                            if pos[0] > 700 and pos[0] < 900 and pos[1] > 440 and pos[1] < 540:
                                if ShopLevel == "Health" and HealthItems[1][2] != "bought":
                                    if gold >= HealthItems[1][2]:
                                        gold -= HealthItems[1][2]
                                        HealthItems[1][2] = "Bought"
                                        HealthItems[0][2] = "none"
                                        Stats["Health"] = int(Stats["Health"] * 4)
                                        OldHealth = Stats["Health"]
                                        Shop = False
                                if ShopLevel == "Attack" and AttackItems[1][2] != "bought":
                                    if gold >= AttackItems[1][2]:
                                        gold -= AttackItems[1][2]
                                        AttackItems[1][2] = "Bought"
                                        AttackItems[0][2] = "none"
                                        Stats["Attack"] = int(Stats["Attack"] * 4)
                                        Shop = False
                                if ShopLevel == "Magic" and MagicItems[1][2] != "bought":
                                    if gold >= MagicItems[1][2]:
                                        gold -= MagicItems[1][2]
                                        MagicItems[1][2] = "Bought"
                                        MagicItems[0][2] = "none"
                                        Stats["Magic"] = int(Stats["Magic"] * 4)
                                        Shop = False
                                if ShopLevel == "Speed" and SpeedItems[1][2] != "bought":
                                    if gold >= SpeedItems[1][2]:
                                        gold -= SpeedItems[1][2]
                                        SpeedItems[1][2] = "Bought"
                                        SpeedItems[0][2] = "none"
                                        Stats["Speed"] = int(Stats["Speed"] * 4)
                                        Shop = False
                                if ShopLevel == "Misc" and MiscItems[1][2] != "bought":
                                    if gold >= MiscItems[1][2]:
                                        gold -= MiscItems[1][2]
                                        MiscItems[1][2] = "Bought"
                                        MiscItems[0][2] = "none"

                                        PlyrAcc = 1000
                                        Stats["Health"] *= 1000
                                        Stats["Attack"] *= 1000
                                        Stats["Magic"] *= 1000
                                        Stats["Speed"] *= 1000

                                        Shop = False


                            if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
                                ShopLevel = "Main"





                pos = pygame.mouse.get_pos()

                if ShopLevel == "Main":

                    if pos[0] > 75 and pos[0] < 275 and pos[1] > 640 and pos[1] < 740:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (75, 650, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (75, 650, 200, 100), 0)

                    if pos[0] > 375 and pos[0] < 575 and pos[1] > 640 and pos[1] < 740:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (375, 650, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (375, 650, 200, 100), 0)

                    if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 650, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 650, 200, 100), 0)

                    if pos[0] > 75 and pos[0] < 275 and pos[1] > 440 and pos[1] < 540:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (75, 450, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (75, 450, 200, 100), 0)

                    if pos[0] > 375 and pos[0] < 575 and pos[1] > 440 and pos[1] < 540:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (375, 450, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (375, 450, 200, 100), 0)

                    if pos[0] > 700 and pos[0] < 900 and pos[1] > 440 and pos[1] < 540:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 450, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 450, 200, 100), 0)

                    text_surface, rect = game_font.render("What shop section do you want?", (0, 0, 0))
                    gameDisplay.blit(text_surface, (400, 100))

                    text_surface, rect = game_font.render(("Health"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (150, 690))

                    text_surface, rect = game_font.render(("Attack"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (450, 690))

                    text_surface, rect = game_font.render(("Exit"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (775, 690))

                    text_surface, rect = game_font.render(("Magic"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (145, 490))

                    text_surface, rect = game_font.render(("Misc"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (430, 490))

                    text_surface, rect = game_font.render(("Speed"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (775, 490))

                elif ShopLevel != "Main":



                    text_surface, rect = game_font.render("What do you want to buy?", (0, 0, 0))
                    gameDisplay.blit(text_surface, (400, 100))

                    if pos[0] > 75 and pos[0] < 275 and pos[1] > 440 and pos[1] < 540:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (75, 450, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (75, 450, 200, 100), 0)

                    if pos[0] > 375 and pos[0] < 575 and pos[1] > 440 and pos[1] < 540:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (375, 450, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (375, 450, 200, 100), 0)

                    if pos[0] > 700 and pos[0] < 900 and pos[1] > 440 and pos[1] < 540:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 450, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 450, 200, 100), 0)

                    if pos[0] > 700 and pos[0] < 900 and pos[1] > 640 and pos[1] < 740:
                        pygame.draw.rect(gameDisplay, (100, 0, 0), (700, 650, 200, 100), 0)
                    else:
                        pygame.draw.rect(gameDisplay, (255, 0, 0), (700, 650, 200, 100), 0)

                    if ShopLevel == "Health":
                        text_surface, rect = game_font.render((HealthItems[0][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (100, 490))
                        text_surface, rect = game_font.render((HealthItems[0][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (400, 490))
                        text_surface, rect = game_font.render((HealthItems[0][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (725, 490))
                        text_surface, rect = game_font.render(str(HealthItems[1][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (125, 510))
                        text_surface, rect = game_font.render(str(HealthItems[1][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (425, 510))
                        text_surface, rect = game_font.render(str(HealthItems[1][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (750, 510))
                    if ShopLevel == "Attack":
                        text_surface, rect = game_font.render((AttackItems[0][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (100, 490))
                        text_surface, rect = game_font.render((AttackItems[0][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (400, 490))
                        text_surface, rect = game_font.render((AttackItems[0][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (725, 490))
                        text_surface, rect = game_font.render(str(AttackItems[1][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (125, 510))
                        text_surface, rect = game_font.render(str(AttackItems[1][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (425, 510))
                        text_surface, rect = game_font.render(str(AttackItems[1][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (750, 510))
                    if ShopLevel == "Speed":
                        text_surface, rect = game_font.render((SpeedItems[0][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (100, 490))
                        text_surface, rect = game_font.render((SpeedItems[0][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (400, 490))
                        text_surface, rect = game_font.render((SpeedItems[0][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (725, 490))
                        text_surface, rect = game_font.render(str(SpeedItems[1][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (125, 510))
                        text_surface, rect = game_font.render(str(SpeedItems[1][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (425, 510))
                        text_surface, rect = game_font.render(str(SpeedItems[1][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (750, 510))
                    if ShopLevel == "Magic":
                        text_surface, rect = game_font.render((MagicItems[0][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (100, 490))
                        text_surface, rect = game_font.render((MagicItems[0][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (400, 490))
                        text_surface, rect = game_font.render((MagicItems[0][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (725, 490))
                        text_surface, rect = game_font.render(str(MagicItems[1][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (125, 510))
                        text_surface, rect = game_font.render(str(MagicItems[1][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (425, 510))
                        text_surface, rect = game_font.render(str(MagicItems[1][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (750, 510))
                    if ShopLevel == "Misc":
                        text_surface, rect = game_font.render((MiscItems[0][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (100, 490))
                        text_surface, rect = game_font.render((MiscItems[0][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (400, 490))
                        text_surface, rect = game_font.render((MiscItems[0][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (725, 490))
                        text_surface, rect = game_font.render(str(MiscItems[1][0]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (125, 510))
                        text_surface, rect = game_font.render(str(MiscItems[1][1]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (425, 510))
                        text_surface, rect = game_font.render(str(MiscItems[1][2]), (0, 0, 0))
                        gameDisplay.blit(text_surface, (750, 510))

                    text_surface, rect = game_font.render(("Exit"), (0, 0, 0))
                    gameDisplay.blit(text_surface, (775, 690))

                pygame.display.update()
                clock.tick(30)

            choosing = True

            while choosing == True:
                gameDisplay.fill((144, 155, 220))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                            Auto = True
                            choosing = False
                        if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                            Auto = False
                            choosing = False
                pos = pygame.mouse.get_pos()

                text_surface, rect = game_font.render("Health: " + str(Stats["Health"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (40, 250))
                text_surface, rect = game_font.render("Attack: " + str(Stats["Attack"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (40, 300))
                text_surface, rect = game_font.render("Speed: " + str(Stats["Speed"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (40, 350))

                text_surface, rect = game_font.render("Enemies Health: " + str(Monster["Health"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (800, 250))
                text_surface, rect = game_font.render("Enemies Attack: " + str(Monster["Attack"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (800, 300))
                text_surface, rect = game_font.render("Enemies Speed: " + str(Monster["Speed"]), (0, 0, 0))
                gameDisplay.blit(text_surface, (800, 350))

                text_surface, rect = game_font.render(("Do you want auto or manual?"), (0, 0, 0))
                gameDisplay.blit(text_surface, (350, 300))

                if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                    pygame.draw.rect(gameDisplay, (100, 0, 0), (250, 460, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (250, 460, 200, 100), 0)

                if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                    pygame.draw.rect(gameDisplay, (100, 0, 0), (500, 460, 200, 100), 0)
                else:
                    pygame.draw.rect(gameDisplay, (255, 0, 0), (500, 460, 200, 100), 0)

                text_surface, rect = game_font.render(("Auto"), (0, 0, 0))
                gameDisplay.blit(text_surface, (325, 500))

                text_surface, rect = game_font.render(("Manual"), (0, 0, 0))
                gameDisplay.blit(text_surface, (575, 500))

                pygame.display.update()
                clock.tick(30)




        if PlayerDead == True:
            game_run = False


        if fight == True:


            #Health Bar

            pygame.draw.rect(gameDisplay, (255, 0, 0), (40, 200, 200, 20), 0)
            pygame.draw.rect(gameDisplay, (0, 255, 0), (40, 200, (Stats["Health"]/OldHealth)*200, 20), 0)

            pygame.draw.rect(gameDisplay, (255, 0, 0), (760, 200, 200, 20), 0)
            pygame.draw.rect(gameDisplay, (0, 255, 0), (960-((Monster["Health"] / MonsterOldHealth) * 200), 200, ((Monster["Health"] / MonsterOldHealth) * 200)+1, 20), 0)

            #Stats
            text_surface, rect = game_font.render("Health: " + str(Stats["Health"]), (0, 0, 0))
            gameDisplay.blit(text_surface, (40, 250))
            text_surface, rect = game_font.render("Attack: " + str(Stats["Attack"]), (0, 0, 0))
            gameDisplay.blit(text_surface, (40, 300))
            text_surface, rect = game_font.render("Speed: " + str(Stats["Speed"]), (0, 0, 0))
            gameDisplay.blit(text_surface, (40, 350))

            text_surface, rect = game_font.render("Enemies Health: " + str(Monster["Health"]), (0, 0, 0))
            gameDisplay.blit(text_surface, (800, 250))
            text_surface, rect = game_font.render("Enemies Attack: " + str(Monster["Attack"]), (0, 0, 0))
            gameDisplay.blit(text_surface, (800, 300))
            text_surface, rect = game_font.render("Enemies Speed: " + str(Monster["Speed"]), (0, 0, 0))
            gameDisplay.blit(text_surface, (800, 350))

            pos = pygame.mouse.get_pos()

            if pos[0] > 250 and pos[0] < 440 and pos[1] > 450 and pos[1] < 550:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (250, 460, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (250, 460, 200, 100), 0)

            if pos[0] > 500 and pos[0] < 700 and pos[1] > 450 and pos[1] < 550:
                pygame.draw.rect(gameDisplay, (100, 0, 0), (500, 460, 200, 100), 0)
            else:
                pygame.draw.rect(gameDisplay, (255, 0, 0), (500, 460, 200, 100), 0)

            text_surface, rect = game_font.render(("Attack"), (0, 0, 0))
            gameDisplay.blit(text_surface, (325, 500))

            text_surface, rect = game_font.render(("Magic"), (0, 0, 0))
            gameDisplay.blit(text_surface, (575, 500))

            if Auto == True:
                attack = True

            if attack == True:
                if Stats["Speed"] > Monster["Speed"]:
                    Stopped = False
                    if random.randint(1,100) <= PlyrAcc:
                        att = random.randint(int(Stats["Attack"]/1.5),int(Stats["Attack"]*1.5))
                        Monster["Health"] -= att
                        msg = "You hit the Monster for " + str(att) + " damage"
                        if random.randint(1,100) <= PlyrAcc - 10 and Stopped is False and Class ==  "Swordsman" and Stats["Speed"] >= 500:
                            att += random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                            Monster["Health"] -= att
                            msg = "You got a double hit for " + str(att) + " damage"
                        else:
                            Stopped = True

                        if random.randint(1,100) <= PlyrAcc - 20 and Stopped is False and Class ==  "Swordsman" and Stats["Speed"] >= 1500:
                            att += random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                            Monster["Health"] -= att
                            msg = "You got a Triple hit for " + str(att) + " damage"
                        else:
                            Stopped = True

                        if random.randint(1,100) <= PlyrAcc - 40 and Stopped is False and Class ==  "Swordsman" and Stats["Speed"] >= 5000:
                            att += random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                            Monster["Health"] -= att
                            msg = "You got a Quadra hit for " + str(att) + " damage"
                        else:
                            Stopped = True
                    else:
                        msg = "You went to hit the monster, but missed"
                    msgType = "Attack"
                    if Monster["Health"] <= 0:
                        MonsterDead = True
                        fight = False

                    if MonsterDead != True:
                        if random.randint(1, 100) <= 75:
                            if random.randint(1, 100) <= 90:
                                att = random.randint(int(Monster["Attack"] / 1.5), int(Monster["Attack"] * 1.5))
                                Stats["Health"] -= att
                                msg2 = "You were hit by the Monster for " + str(att) + " damage"
                            else:
                                msg2 = ("The Mosnter tried to hit you, but missed")
                        else:
                            heal = random.randint(int(Monster["Magic"] / 1.5), int(Monster["Magic"] * 1.5))
                            if heal + Monster["Health"] > Monster["MaxHealth"]:
                                heal = Monster["MaxHealth"] - Monster["Health"]
                            Monster["Health"] += heal
                            msg2 = ("The Monster healed for " + str(heal) + "health")
                    if Stats["Health"] <= 0:
                        PlayerDead = True
                        fight = False
                else:
                    if random.randint(1,100) <= 75:
                        if random.randint(1,100) <= 90:
                            att = random.randint(int(Monster["Attack"] / 1.5), int(Monster["Attack"] * 1.5))
                            Stats["Health"] -= att
                            msg2 = "You were hit by the Monster for " + str(att) + " damage"
                        else:
                            msg2 = ("The Mosnter tried to hit you, but missed")
                    else:
                        heal = random.randint(int(Monster["Magic"]/1.5),int(Monster["Magic"]*1.5))
                        if heal + Monster["Health"] > Monster["MaxHealth"]:
                            heal = Monster["MaxHealth"] - Monster["Health"]
                        Monster["Health"] += heal
                        msg2 = ("The Monster healed for " + str(heal) + "health")

                    if Stats["Health"] <= 0:
                        PlayerDead = True
                        fight = False

                    if PlayerDead != True:
                        if random.randint(1,100) <= PlyrAcc:
                            Stopped = False
                            att = random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                            Monster["Health"] -= att
                            msg = "You hit the Monster for " + str(att) + " damage"
                            if random.randint(1, 100) <= PlyrAcc - 10 and Stopped is False and Class == "Swordsman" and \
                                    Stats["Speed"] >= 500:
                                att += random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                                Monster["Health"] -= att
                                msg = "You got a double hit for " + str(att) + " damage"
                            else:
                                Stopped = True

                            if random.randint(1, 100) <= PlyrAcc - 20 and Stopped is False and Class == "Swordsman" and \
                                    Stats["Speed"] >= 1500:
                                att += random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                                Monster["Health"] -= att
                                msg = "You got a Triple hit for " + str(att) + " damage"
                            else:
                                Stopped = True

                            if random.randint(1, 100) <= PlyrAcc - 40 and Stopped is False and Class == "Swordsman" and \
                                    Stats["Speed"] >= 5000:
                                att += random.randint(int(Stats["Attack"] / 1.5), int(Stats["Attack"] * 1.5))
                                Monster["Health"] -= att
                                msg = "You got a Quadra hit for " + str(att) + " damage"
                            else:
                                Stopped = True

                        else:
                            msg = "You went to hit the monster, but missed"
                        msgType = "Attack"
                    if Monster["Health"] <= 0:
                        MonsterDead = True
                        fight = False

                attack = False

            if magicAttack == True:
                if Stats["Speed"] > Monster["Speed"]:
                    if MagicType == "Damage":
                        if random.randint(1, 100) <= PlyrAcc:
                            att = random.randint(int(Stats["Magic"]/1.5),int(Stats["Magic"]*1.5))
                            Monster["Health"] -= att
                            msg = "You casted a spell upon the Monster for " + str(att) + " damage"
                        else:
                            msg = "You tried to cast a spell, but you fizzled"
                    else:
                        heal = random.randint(int(Stats["Magic"] / 1.5), int(Stats["Magic"] * 1.5))
                        if heal + Stats["Health"] > OldHealth:
                            heal = OldHealth - Stats["Health"]
                        Stats["Health"] += heal
                        msg = ("You healed yourself for " + str(heal) + "health")
                    msgType = "Magic"
                    if Monster["Health"] <= 0:
                        MonsterDead = True
                        fight = False


                    if MonsterDead != True:
                        if random.randint(1, 100) <= 75:
                            if random.randint(1, 100) <= 90:
                                att = random.randint(int(Monster["Attack"] / 1.5), int(Monster["Attack"] * 1.5))
                                Stats["Health"] -= att
                                msg2 = "You were hit by the Monster for " + str(att) + " damage"
                            else:
                                msg2 = ("The Mosnter tried to hit you, but missed")
                        else:
                            heal = random.randint(int(Monster["Magic"] / 1.5), int(Monster["Magic"] * 1.5))
                            if heal + Monster["Health"] > Monster["MaxHealth"]:
                                heal = Monster["MaxHealth"] - Monster["Health"]
                            Monster["Health"] += heal
                            msg2 = ("The Monster healed for " + str(heal) + "health")
                    if Stats["Health"] <= 0:
                        PlayerDead = True
                        fight = False
                else:
                    if random.randint(1,100) <= 75:
                        if random.randint(1,100) <= 90:
                            att = random.randint(int(Monster["Attack"] / 1.5), int(Monster["Attack"] * 1.5))
                            Stats["Health"] -= att
                            msg2 = "You were hit by the Monster for " + str(att) + " damage"
                        else:
                            msg2 = ("The Mosnter tried to hit you, but missed")
                    else:
                        heal = random.randint(int(Monster["Magic"]/1.5),int(Monster["Magic"]*1.5))
                        if heal + Monster["Health"] > Monster["MaxHealth"]:
                            heal = Monster["MaxHealth"] - Monster["Health"]
                        Monster["Health"] += heal
                        msg2 = ("The Monster healed for " + str(heal) + "health")
                    if Stats["Health"] <= 0:
                        PlayerDead = True
                        fight = False

                    if MagicType == "Damage":
                        if PlayerDead != True and random.randint(1,100) <= PlyrAcc:
                            att = random.randint(int(Stats["Magic"] / 1.5), int(Stats["Magic"] * 1.5))
                            Monster["Health"] -= att
                            msg = "You casted a spell upon the Monster for " + str(att) + " damage"
                        else:
                            msg = "You tried to cast a spell, but you fizzled"
                    else:
                        heal = random.randint(int(Stats["Magic"] / 1.5), int(Stats["Magic"] * 1.5))
                        if heal + Stats["Health"] > OldHealth:
                            heal = OldHealth - Stats["Health"]
                        Stats["Health"] += heal
                        msg = ("You healed yourself for " + str(heal) + "health")

                    msgType = "Magic"
                    if Monster["Health"] <= 0:
                        MonsterDead = True
                        fight = False



                magicAttack = False


            text_surface, rect = game_font.render((msg), (0, 0, 0))
            if msgType == "Attack":
                gameDisplay.blit(text_surface, (330, 350))
            if msgType == "Magic":
                gameDisplay.blit(text_surface, (275, 350))
            text_surface, rect = game_font.render((msg2), (0, 0, 0))
            gameDisplay.blit(text_surface, (310, 400))




        pygame.display.update()
        clock.tick(30)

    print("Skill level is a way to see how good you did compared to others")
    print("Skill: " + str(int(Skill)))


game_loop()