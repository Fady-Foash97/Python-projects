import pygame
import random
pygame.init()
pygame.mixer.init()
correct = pygame.mixer.Sound("609336__kenneth_cooney__completed.wav")
def Quiz():
    score = 0
    while True:
      print("Welcome to the game!")
      
      ## Question 1
      print("\nWhat is a bird that doesn't fly?")
      answer1 = input("Answer is: ").strip().lower()
      if answer1 == "penguin":
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("Fly away!") 
          score -= 1
          print(f"You lost {score} points out of 18 points")
          
 
      ## Question 2
      print("\nWhat is the science field that focuses on the wealth of nations?")
      answer2 = input("Answer is: ").lower()
      if answer2 == "economics":
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("You're broke!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
  
      ## Question 3
      print("\nWhere does snake & ladders game originate from?")
      ## Multiple choice
      options1 = ["1-China", "2-Egypt", "3-India", "4-Greece"]
      random.shuffle(options1)
      for option1 in options1:
          print(f"{option1}")
      answer3 = input("Choose the correct answer:")
      if answer3 in ["India", "3"]:
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("Loser!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
  
      ## Question 4
      print("\nWhat is Japan's currency?")
      options2 = ["1-ywan", "2-dinar", "3-dollar", "4-yen"]
      random.shuffle(options2)
      for option2 in options2:
          print(f"{option2}")
      answer4 = input("Choose the correct answer:").lower()
      if answer4 in ["yen", "4"]:
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      elif answer4 in ["ywan", "1"]:
          print("That is China's currency ")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer4 in ["dinar", "2"]:
          print("Sho betgol?!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer4 in ["dollar", "3"]:
          print("USA! USA! USA!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      else: 
          print("You're broke!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
  
      ## Question 5
      print("\nThe capital of Hungary is:")
      options3 = ["1-Bucharest", "2-Warsaw", "3-Budapest", "4-Vienna"]
      random.shuffle(options3)
      for option3 in options3:
          print(f"{option3}")
      answer5 = input("Choose the correct answer:").upper()
      if answer5 in ["Budapest", "3"]:
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      elif answer5 in ["Warsaw","2"]: 
          print("Wrong! Warsaw is the capital of Poland")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer5 in ["Bucharest", "1"]: 
          print("Wrong! Bucharest is the capital of Romania")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer5 in ["Vienna","4"]: 
          print("Wrong! Vienna is the capital of Austria")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      else:
          print("I am hungry!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
           
 
      ## Question 6
      print("\nWhere is the united nations located at?")
      answer6 = input("")
      if answer6 == "New York":
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("Wrong!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
 
      ## Question 7
      print("\n3 Countries have coastlines on both the mediterranean sea and the atlantic ocean.")
      answer7 = input("True or False: ").lower()
      if answer7 == "true":
          print("Correct! France, Spain and Morocco are those countries that have coastlines \non both the mediterranean sea and the atlantic ocean.")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("Shipwreck!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
      ## Question 8
      print("\nHow many pieces in a dominos game?")
      answer8 = input("Answer is: ")
      if answer8 == "28":
          print("Correct! let's play a dominos match!")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("Match's over!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
      ## Question 9
      print("\nThe first streaming platform is: ")
      options4 = ["1-netflix", "2-youtube", "3-OSN", "4-amazon prime"]
      random.shuffle(options4)
      for option4 in options4:
          print(f"{option4}")
      answer9 = input("Choose the correct answer: ").lower()
      if answer9 in ["youtube", "2"]:
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      else: 
          print("Wrong! Youtube is the first streaming platform.")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
 
      ## Question 10
      print("\nTallest mountain in the world is")
      answer10 = input(": ").upper()
      if answer10 == "Everest":
         print("Good, climb it!")
         score += 1
         print(f"Your score is {score} points")
      else: 
         print("Don't ever climb it!")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
         
      
      ## Question 11
      print("\nThe great wall is located at: ")
      options5 = ["1-China", "2-Japan", "3-Egypt", "4-Mexico"]
      random.shuffle(options5)
      for option5 in options5:
          print(f"{option5}")
      answer11 = input("Choose the correct answer: ").upper()
      if answer11 in ["China", "1"]:
         print("The great wall of china is one of the tallest structures in the world")
         score += 1
         print(f"Your score is {score} points")
      elif answer11 in ["Egypt", "3"]:
         print("Egypt does have a wall located in old Cairo, but it's not The great wall")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
      elif answer11 in ["Japan", "2"]:
         print("Japan is an island country, unlike China it doesn't need a great wall to protect it")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
      elif answer11 in ["Mexico", "4"]:
         print("The Aztec empire in Mexico was destroyed and now speak spanish.")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
      else:
         print("Wrong!")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
         
 
      ## Question 12
      print("\nWho won the nobel prize multiple times?")
      options6 = ["1-Anwar Sadat", "2-Wilhelm Rontgen", "3-Marie Curie", "4-Albert Einstein"]
      random.shuffle(options6)
      for option6 in options6:
          print(f"{option6}")
      answer12 = input("Choose the correct answer: ").upper()
      if answer12 in ["Anwar Sadat", "1"]:
         print("Anwar Sadat won the nobel peace prize")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
      elif answer12 in ["Wilhelm Rontgen", "2"]:
         print("Wilhelm Rontgen won the nobel prize in chemistry")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
      elif answer12 in ["Marie Curie", "3"]:
         print("Correct! Marie Curie won the nobel prize in two science fields: chemistry and physics")
         score += 1
         print(f"Your score is {score} points")
      elif answer12 in ["Albert Einstein", "4"]:
         print("Albert Einstein won the nobel prize in physics")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
         
 
      ## Question 13
      print("\nRussia is the first country to invent rockets")
      answer13 = input("True or False? ").lower()
      if answer13 == "true":
         print("Russia was the first country to use a space rocket to launch a man into space,\nbut it wasn't the first rocket launch in history,\nit was Germany during world war 2.")
         score -= 1
         print(f"You lost {score} point(s) out of 18 points")
      elif answer13 == "false":
         print("Germany was the first country to invent rockets but it was used in world war 2 in the final years of it.")
         score += 1
         print(f"Your score is {score} points")
         
         
      ## Question 14
      print("\nWhat is the biggest selling video game in the world?")
      options7 = ["1-Witcher 3", "2-GTA 5", "3-Super mario bros", "4-Minecraft"]
      random.shuffle(options7)
      for option7 in options7:
          print(f"{option7}")
      answer14 = input("Choose the correct answer: ").upper()
      if answer14 in ["GTA 5", "2"]:
          print("Correct!")
          score += 1
          print(f"Your score is {score} points")
      else:
          print("Wrong!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
          
       ## Question 15
      print("\nWho was the US president who signed the civil rights act?")
      options8 = ["1-John Kennedy", "2-Jimmy Carter", "3-Lyndon B Johnson", "4-Richard Nixon"]
      random.shuffle(options8)
      for option8 in options8:
          print(f"{option8}")
      answer15 = input("Choose the correct answer: ").upper()
      if answer15 in ["John Kennedy", "1"]:
          print("John Kennedy was assassinated in 1963 and the act was signed later.")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer15 in ["Jimmy Carter", "2"]:
          print("Jimmy Carter ruled the USA in the 70s but the act was signed in the 60s.")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer15 in ["Lyndon B Johnson", "3"]:
          print("Correct! Lyndon B Johnson signed the civil rights act in 1964: his first year as president of the USA")
          score += 1
          print(f"Your score is {score} points")
      elif answer15 in ["Richard Nixon", "4"]:
          print("Richard Nixon was president of the USA from 1969 until his resignation in 1974 after the watergate scandal")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      else:
          print("Wrong!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
          
          
       ## Question 16
      print("\nWho was the actor who played the main character in the matrix?")
      options9 = ["1-Keanu Reeves", "2-Tom Cruise", "3-Christian Bale", "4-Nicolas Cage"]
      random.shuffle(options9)
      for option9 in options9:
          print(f"{option9}")
      answer18 = input("Choose the correct answer: ").upper()
      if answer18 in ["Keanu Reeves", "1"]:
          print("that's correct, wake up from the matrix.")
          score += 1
          print(f"Your score is {score} points out of 18 points")
      else:
          print("The matrix has you.")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
       ## Question 17
      print("\nWho won the most academy awards?")
      options10 = ["1-Tom Hanks", "2-Meryl Streep", "3-Walt Disney", "4-Daniel Day Lewis"]
      random.shuffle(options10)
      for option10 in options10:
          print(f"{option10}")
      answer17 = input("Choose the correct answer: ").upper()
      if answer17 in ["3", "Walt Disney"]:
          print("Correct! Walt Disney won the most academy awards and was nominated 59 times")
          score += 1
          print(f"Your score is {score} points out of 18 points")
      else:
          print("Wrong!")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
       ## Question 18:
      print("\nWhich country that had the most winners in chess?")
      options11 = ["1-USA", "2-Russia", "3-Britain"]
      random.shuffle(options11)
      for option11 in options11:
          print(f"{option11}")
      answer18 = input("Choose the correct answer: ").upper()
      if answer18 in ["1", "USA"]:
          print("Although USA has a grandmaster like Bobbie Fischer, but that's just an exception, \nChess is not a national game in the USA")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      elif answer18 in ["2", "Russia"]:
          print("Correct! chess is a national game in Russia, it's studied in school, \nRussia has two grandmasters with the most wins:\nGarry Kasparov and Karpov")
          score += 1
          print(f"Your score is {score} points out of 18 points")
      elif answer18 in ["3", "Britain"]:
          print("Although chess is popular in Britain, it is not a national sport like football and boxing.")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      else:
          print("Wrong")
          score -= 1
          print(f"You lost {score} point(s) out of 18 points")
      ## Question 19:
      print("\n")
      print("\n")
      print("\nGame over!")
      print(f"you scored {score} points out of 18")
      if score == 18:
         print("Congratulations! perfect score!")
      elif score == 7:
          print("\nGood but it could be better")
      elif score >= 10:
         print("\nExcellent!")
      else: 
          print("Better luck next time")
      Play = input("Do you want to play again? (Yes/No): ").lower()
      if Play != "yes":
          print("Thank you for playing.")
          break
Quiz()