## Intellectual game
## Attachments
import random
import pygame
## Initialize background music
pygame.init()
pygame.mixer.init()
##pygame.mixer.music.load("792340__zhr__chill-background-music-3.wav")
##pygame.mixer.music.play(-1)
correct_sound = pygame.mixer.Sound("609336__kenneth_cooney__completed.wav")
wrong_sound = pygame.mixer.Sound("Windows XP Shutdown.wav")
## Introduction
print("Let's play a game to test your brains")
## Puzzle 1
print("\nPuzzle 1: Your computer is running slow")
puzzle1 = input("\n")
puzzle1 = puzzle1.strip()
## Physical problem
if puzzle1 == "Cleaning the dust out of my computer":
    print("\nClever")
    correct_sound.play()
    tools = ["Screwdriver", "Cleaning cloth", "Spray", "Hair dryer"]
    print("\nTools to use:")
    for tool in tools:
        print(f"{tool}")
    print("\nYou are well prepared but you need a mask and sunglasses to cover your face from dust")
## Performance problem
elif puzzle1 == "If the problem is internal, I would use antivirus":
    print("\nYou are well prepared for any cyber security problem")
    correct_sound.play()
else:
    print("\nTry again")
    wrong_sound.play()
## Puzzle 2
print("\nPuzzle 2: Your warehouse is full of random supplies")
puzzle2 = input("\n")
puzzle2 = puzzle2.strip()
if puzzle2 == "Arrange supplies based on category":
    print("\nExcellent, you are a smart manager")
    correct_sound.play()
elif puzzle2 == "Arrange supplies based on requirement":
    print("\nYou are a smart seller")
    correct_sound.play()
else:
    print("\nTry again")
    wrong_sound.play()
## Puzzle 3
print("\nPuzzle 3: You are in a desert, you feel hungry, \nSuddenly! you saw an animal")
puzzle3 = input("\n")
puzzle3 = puzzle3.strip()
if puzzle3 == "I would hunt it with whatever weapon I have":
    weapons = ["Hunting rifle", "Knife", "A bow and arrow"]
    for weapon in weapons:
        print(f"-{weapon}")
    correct_sound.play()
else:
    print("\nTry again")
    wrong_sound.play()
## Puzzle 4
baby = pygame.mixer.Sound("625686__mlaudio__baby-toddler-laugh-giggle.wav")
happy = pygame.mixer.Sound("75697__robinhood76__01126-happy-baby-shout-4.wav")
print("\nPuzzle 4: Your baby is crying.")
Decisions = ["Make a funny face", "Give him milk to drink", "Give him his favourite toy"]
random.shuffle(Decisions)
for Decision in Decisions:
    print(f"-{Decision}")
puzzle4 = input("\n")
puzzle4 = puzzle4.strip()
if puzzle4 == "Make a funny face":
    print("\nYou made the baby laugh!")
    baby.play()
    print("\nYou are a great parent")
elif puzzle4 == "Give him milk to drink":
    print("\nThat's what the baby needed")
    happy.play()
    print("\nYou are a great parent")
elif puzzle4 == "Give him his favourite toy":
    print("\nHe stopped crying and started playing")
    happy.play()
    print("\nYou are a great parent")
else:
    print("\nTry again")
    wrong_sound.play()
## Puzzle 5
mission_complete = pygame.mixer.Sound("665206__silverillusionist__level-upmission-complete-primal-1.wav")
alarm = pygame.mixer.Sound("161930__viertelnachvier__house-alarm.wav")
gun = pygame.mixer.Sound("[EVANO.COM] Pistol Sound Effect-HQ_1.wav")
mission_failed = pygame.mixer.Sound("[EVANO.COM] Metal Gear Solid PS1 Game Over Theme (Voiceless Version)-HQ_2.wav")
print("\nPuzzle 5: You are a spy on a top secret mission, there's a locked door in front of you.")
print("\nChoose your approach:")
options = ["Pick lock", "Kick the door"]
for option in options:
    print(f"-{option}")
puzzle5 = input("\n")
puzzle5 = puzzle5.strip()
if puzzle5 == "Pick lock":
    print("\nSmart way, no one will know you were really here")
    mission_complete.play()
elif puzzle5 == "Kick the door":
    print("\nCongratulations, your cover is blown!")
    alarm.play()
    print("\nGet your gun ready!")
    guard = input("two guards, one hiding behind a crate, the other behind a wall, \nwho will you shoot first? ")
    if guard == "The guard behind the wall then the other one":
        print("\nExcellent shot mister Wick!")
        gun.play()
    else:
        print("\nMission failed!")
        mission_failed.play()
else:
    print("\nMission failed!")
    mission_failed.play()
## Puzzle 6
victory = pygame.mixer.Sound("[EVANO.COM] Freedom Fighters - Choir of Liberty-HQ_1.wav")
lost = pygame.mixer.Sound("462474__felixblume__church-bells-at-noon-on-sunday-prague_1.wav")
print("\nPuzzle 6: You travel back in time to world war 2, you are part of the Russian army")
print("\nWhat primary choice of weapon you would have?")
weapons = ["Mosin nagant", "Mosin nagant with scope", "PPSH machine gun"]
random.shuffle(weapons)
for weapon in weapons:
    print(f"-{weapon}")
puzzle6 = input("\n")
puzzle6 = puzzle6.strip()
if puzzle6 == "Mosin nagant":
    print("\nIt works well on the frontlines\n")
    correct_sound.play()
elif puzzle6 == "Mosin nagant with scope":
    print("\nYou have the ultimate weapon, this weapon was the reason the Russians won many battles against the Germans")
    victory.play()
elif puzzle6 == "PPSH machine gun":
    print("\nThis gun works well on close range, but the magazine is emptied fast")
    correct_sound.play()
else:
    print("\nRest in peace")
    lost.play()
## Puzzle 7
Evil = pygame.mixer.Sound("Low of Solipsism - Death Note [Extended]_1.wav")
Hero = pygame.mixer.Sound("Hans Zimmer - A Watchful Guardian The Dark Knight_1.wav")
Wise = pygame.mixer.Sound("Interstellar Main Theme - Extra Extended - Soundtrack by  Hans Zimmer_1.wav")
print("\nPuzzle 7: You wake up one day and discovered you have a superpower to read people's minds")
Choices = ["Manipulate people", "Empathize with people", "Protect the innocent"]
random.shuffle(Choices)
for choice in Choices:
    print(f"- {choice}")
puzzle7 = input("\nHow would you use your superpower? ")
puzzle7 = puzzle7.strip()
if puzzle7 == "Manipulate people":
    print("\nYou choose power over morality, that path leads to corruption")
    Evil.play()
    pygame.time.delay(9000)
elif puzzle7 == "Empathize with people":
    print("\nYou are wise, understanding others is a noble way")
    Wise.play()
    pygame.time.delay(9000)
elif puzzle7 == "Protect the innocent":
    print("\nYou are a true hero, but remeber, \nbe humble, \nyou either die a hero or live long enough to see yourself become the villain")
    Hero.play()
    pygame.time.delay(16000)
else:
    print("\nTry again")
    wrong_sound.play()
    pygame.time.delay(9000)
## Puzzle 8 
Weapons = pygame.mixer.Sound("cs 1.6 aug weapon animations ｜ T weapon.wav")
Desperate = pygame.mixer.Sound("Dying Light Soundtrack - Harran.wav")
Hunter = pygame.mixer.Sound("The Walking Dead OST   Daryl's Theme extended.wav")
Death = pygame.mixer.Sound("Leon Kennedy Death Sound - Resident Evil 4 remake (2023).wav")
print("\nPuzzle 8: The world has ended! \nzombies have taken over the world!")
print("\nChoose your loadout:")
Tools = ["Ak47, Knife, Shotgun, Sniper rifle, Truck with food supplies", 
         "Pistol, Shotgun, Car", 
         "Crossbow, Baseball bat, Knife, Flashlight, Binoculars, Backpack for food"]
random.shuffle(Tools)
for Tool in Tools:
    print(f"-{Tool}")
puzzle8 = input("\n")
puzzle8 = puzzle8.strip()
if puzzle8 == "Ak47, Knife, Shotgun, Sniper rifle, Truck with food supplies":
    print("\nYou are well prepared for anything, you are the John Wick and James Bond of zombie apocalypse!")
    Weapons.play()
    pygame.time.delay(3000)
elif puzzle8 == "Pistol, Shotgun, Car":
    print("\nQuick and efficient, but you won't survive for long!")
    Desperate.play()
    pygame.time.delay(9000)
elif puzzle8 == "Crossbow, Baseball bat, Knife, Flashlight, Binoculars, Backpack for food":
    print("\nYou are a natural born hunter like Daryl Dixon from walking dead.")
    Hunter.play()
    pygame.time.delay(9000)
else:
    print("\nRest in peace")
    Death.play()
    pygame.time.delay(3000)
## Puzzle 9
print("\nPuzzle 9: You are trying to steal a car, which tactic to use?")
Police = pygame.mixer.Sound("Police chase.wav")
Complete = pygame.mixer.Sound("[EVANO.COM] Grand Theft Auto IV Mission Complete Theme (Long Version)-HQ_1.wav")
Hacker = pygame.mixer.Sound("Hacking Watch dogs 2.wav")
Tactics = ["Break the window", "Pick the car lock and hotwire it", "Hack the car's security system if its electric"]
print("\nChoose the following tactics:")
random.shuffle(Tactics)
for Tactic in Tactics:
    print(f"-{Tactic}")
puzzle9 = input("\n")
puzzle9 = puzzle9.strip()
if puzzle9 == "Break the window":
    print("Congratulations, you are wanted by police!")
    Police.play()
    pygame.time.delay(7000)
elif puzzle9 == "Pick the car lock and hotwire it":
    print("Mission passed!")
    Complete.play()
    pygame.time.delay(9000)
elif puzzle9 == "Hack the car's security system if its electric":
    print("You are a ghost, you can hack through any system!")
    Hacker.play()
    pygame.time.delay(9000)
    
    


    
    


