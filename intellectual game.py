## Intellectual game
## Attachments
import random
import pygame
## Initialize background music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("792340__zhr__chill-background-music-3.wav")
pygame.mixer.music.play(-1)
correct_sound = pygame.mixer.Sound("609336__kenneth_cooney__completed.wav")
wrong_sound = pygame.mixer.Sound("Windows XP Shutdown.wav")
## Introduction
print("Let's play a game to test your brains")
## Puzzle 1
print("\nPuzzle 1: Your computer is running slow")
puzzle1 = input("\n")
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
elif puzzle1 == "If the problem is internal, I would use antivirus and antispyware programs":
    print("\nYou are well prepared for any cyber security problem")
    correct_sound.play()
else:
    print("\nTry again")
    wrong_sound.play()
## Puzzle 2
print("\nPuzzle 2: Your warehouse is full of random supplies")
puzzle2 = input("\n")
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
puzzle6 = input("\nWhat weapon will you use?")
if puzzle6 == "Mosin nagant":
    print("\nIt works well on the frontlines")
    correct_sound.play()
    pygame.time.delay(2000)
elif puzzle6 == "Mosin nagant with scope":
    print("\nYou have the ultimate weapon, this weapon was the reason the Russians won many battles against the Germans")
    victory.play()
    pygame.time.delay(9000)
elif puzzle6 == "PPSH machine gun":
    print("\nThis gun works well on close range, but the magazine is emptied fast")
    correct_sound.play()
    pygame.time.delay(2000)
else:
    print("\nRest in peace")
    lost.play()
    pygame.time.delay(7000)
## Puzzle 7
##print("\nPuzzle 7: You wake up one day and discovered you have a superpower to read people's minds")

    
    


