import random
def Quiz():
    while True:
     print("Welcome to the game!")
     score = 0
     failed = 1
 
     ## Question 1
     print("\nQuestion 1: What is a bird that doesn't fly?")
     answer1 = input("Answer is: ").lower()
 
     if answer1 == "penguin":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     else:
         print("Fly away!")
         print(f"You lost {score - failed}")

     ## Question 2
     print("\nQuestion 2: What is the science that focuses on the wealth of nations?")
     answer2 = input("Answer is: ").lower()
 
     if answer2 == "economics":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     else:
         print("You're broke!")
         print(f"You lost {score - failed}")
 
     ## Question 3
     print("\nQuestion 3: Where does snake & ladders game originate?")
     ## Multiple choice
     options1 = ["China", "Egypt", "India", "Greece"]
     random.shuffle(options1)
     print(", ".join(options1))
     answer3 = input("Choose the correct answer:")
 
     if answer3 == "India":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     else:
         print("Loser!")
         print(f"You lost {score - failed}")
 
     ## Question 4
     print("\nQuestion 4: What is Japan's currency?")
     options2 = ["ywan", "dinar", "dollar", "yen"]
     random.shuffle(options2)
     print(", ".join(options2))
     answer4 = input("Choose the correct answer:").lower()
 
     if answer4 == "yen":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     elif answer4 == "ywan":
         print("That is China's currency ")
         print(f"You lost {score - failed}")
     elif answer4 == "dinar":
         print("Sho betgol?!")
         print(f"You lost {score - failed}")
     elif answer4 == "dollar":
         print("USA! USA! USA!")
         print(f"You lost {score - failed}")
     else: 
         print("You're broke!")
         print(f"You lost {score - failed}")
 
     ## Question 5
     print("\nQuestion 5: The capital of Hungary is:")
     options3 = ["Bucharest", "Warsaw", "Budapest", "Vienna"]
     random.shuffle(options3)
     print(", ".join(options3))
     answer5 = input("Choose the correct answer:")
 
     if answer5 == "Budapest":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     else: 
         print("I am hungry!")
         print(f"You lost {score - failed}") 

     ## Question 6
     print("\nQuestion 6: Where is the united nations located at?")
     answer6 = input("")
 
     if answer6 == "New York":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     else:
         print("Wrong!")
         print(f"You lost {score - failed}") 

     ## Question 7
     print("\nQuestion 7: 3 Countries have coastlines on both the mediteranean and the atlantic ocean.")
     answer7 = input("True or False: ").lower()
 
     if answer7 == "true":
         print("Correct! France, Spain and Morocco are those countries.")
         score += 1
         print(f"Your score is {score}")
     else:
         print("Shipwreck!")
         print(f"You lost {score - failed}")
         
     ## Question 8 
     print("\nQuestion 8: How many pieces in a dominos game?")
     answer8 = input("Answer is: ")
     if answer8 == "28":
         print("Correct! let's play a dominos match!")
         score += 1
         print(f"Your score is {score}")
     else:
         print("Match's over!")
         print(f"You lost {score - failed}")
 
     ## Question 9
     print("\nQuestion 9: The first streaming platform is: ")
     options4 = ["netflix", "youtube", "OSN", "amazon prime"]
     random.shuffle(options4)
     print(", ".join(options4))
     answer9 = input("Choose the correct answer: ").lower()
     if answer9 == "youtube":
         print("Correct!")
         score += 1
         print(f"Your score is {score}")
     else: 
         print("Wrong! Youtube is the first streaming platform.")
         print(f"You lost {score - failed}")

     ## Question 10
     print("\nQuestion 10: Tallest mountain in the world is")
     answer10 = input(": ")
     if answer10 == "Everest":
        print("Good, climb it!")
        score += 1
        print(f"Your score is {score}")
     else: 
        print("Don't ever climb it!")
        print(f"You lost {score - failed}")
     
     ## Question 11 
     print("\nQuestion 11: The great wall is located at: ")
     options5 = ["China", "Japan", "Egypt", "Mexico"]
     random.shuffle(options5)
     print(", ".join(options5))
     answer11 = input("Choose the correct answer: ")
     if answer11 == "China":
        print("The great wall of china is one of the tallest structures in the world")
        score += 1
        print(f"Your score is {score}")
     elif answer11 == "Egypt":
        print("Egypt does have a wall located in old Cairo, but it's not The great wall")
        print(f"You lost {score - failed}")
     elif answer11 == "Japan":
        print("Japan is an island country, unlike its neighbour China it doesn't need a great wall to protect it")
        print(f"You lost {score - failed}")
     elif answer11 == "Mexico":
        print("The Aztec empire in Mexico was destroyed and now speak spanish.")
        print(f"You lost {score - failed}")
     else:
        print("Wrong!")
        print(f"You lost {score - failed}")

     ## Question 12
     print("\nQuestion 12: Who won the nobel prize multiple times?")
     options6 = ["Anwar Sadat", "Wilhelm Rontgen", "Marie Curie", "Albert Einstein"]
     random.shuffle(options6)
     print(", ".join(options6))
     answer12 = input("Choose the correct answer: ")
     if answer12 == "Anwar Sadat":
        print("Anwar Sadat won the nobel peace prize")
        print(f"You lost {score - failed}")
     elif answer12 == "Wilhelm Rontgen":
        print("Wilhelm Rontgen won the nobel prize in chemistry")
        print(f"You lost {score - failed}")
     elif answer12 == "Marie Curie":
        print("Correct! Marie Curie won the nobel prize in two science fields: chemistry and physics")
        score += 1
        print(f"Your score is {score}")
     elif answer12 == "Albert Einstein":
        print("Albert Einstein won the nobel prize in physics")
        print(f"You lost {score - failed}")

     ## Question 13
     print("\nQuestion 13: Russia is the first country to invent rockets")
     answer13 = input("True or False? ").lower()
     if answer13 == "true":
        print("Russia was the first country to use a space rocket to launch a man into space but it wasn't first rocket launch in history.")
        print(f"You lost {score - failed}")
     elif answer13 == "false":
        print("Germany was the first country to invent rockets but it was used in world war 2 in the final years of it.")
        score += 1
        print(f"Your score is {score}")
 
 
     print("\nGame over!")
     print(f"you scored {score} out of 13")
     if score == 13:
         print("Congratulations! perfect score!")
     elif score == 7:
         print("\nGood but it could be better")
     elif score >= 9:
        print("\n Excellent!")
     else: 
         print("Better luck next time")
     Play = input("Do you want to play again? (Yes/No): ").lower()
     if Play != "yes":
         print("Thank you for playing.")
         break
        

Quiz()