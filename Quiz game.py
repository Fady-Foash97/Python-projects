def Quiz():
    while True:
     print("Welcome to the game!")
 
     ## Question 1
     print("\nQuestion 1: What is a bird that doesn't fly?")
     answer1 = input("Answer is: ")
 
     if answer1 == "Penguin":
         print("Correct!")
     else:
         print("Fly away!")
 
     ## Question 2
     print("\nQuestion 2: What is the science that focuses on the wealth of nations?")
     answer2 = input("Answer is: ")
 
     if answer2 == "Economics":
         print("Correct!")
     else:
         print("You're broke!")
 
     ## Question 3
     print("\nQuestion 3: Where does snake & ladders game originate?")
     ## Multiple choice
     options1 = ["China", "Egypt", "India", "Greece"]
     print(", ".join(options1))
     answer3 = input("Choose the correct answer:")
 
     if answer3 == "India":
         print("Correct!")
     else:
         print("Loser!")
 
     ## Question 4
     print("\nQuestion 4: What is Japan's currency?")
     options2 = ["Ywan", "Dinar", "Dollar", "Yen"]
     print(", ".join(options2))
     answer4 = input("Choose the correct answer:")
 
     if answer4 == "Yen":
         print("Correct!")
     elif answer4 == "Ywan":
         print("That is China's currency ")
     elif answer4 == "Dinar":
         print("Sho betgol?!")
     elif answer4 == "Dollar":
         print("USA! USA! USA!")
     else: 
         print("You're broke!")
 
     ## Question 5
     print("\nQuestion 5: The capital of Hungary is:")
     options3 = ["Bucharest", "Warsaw", "Budapest", "Vienna"]
     print(", ".join(options3))
     answer5 = input("Choose the correct answer:")
 
     if answer5 == "Budapest":
         print("Correct!")
     else: 
         print("I am hungry!")
 
     ## Question 6
     print("\nQuestion 6: Who played the role of Raafat El Hagan?")
     answer6 = input("")
 
     if answer6 == "Mahmoud Abdul Aziz":
         print("Correct!")
     else:
         print("Wrong!")
 
     ## Question 7
     print("\nQuestion 7: 3 Countries have coastlines on both the mediteranean and the atlantic ocean.")
     answer7 = input("True or False: ")
 
     if answer7 == "True":
         print("Correct! France, Spain and Morocco are those countries.")
     else:
         print("Shipwreck!")
         
     ## Question 8 
     print("\nQuestion 8: How many pieces in a dominos game?")
     answer8 = input("Answer is: ")
     if answer8 == "28":
         print("Correct! let's play a dominos match!")
     else:
         print("Match's over!")
 
     ## Question 9
     print("\nQuestion 9: The first streaming platform is: ")
     options4 = ["Netflix", "Youtube", "OSN", "Amazon prime"]
     print(", ".join(options4))
     answer9 = input("Choose the correct answer: ")
     if answer9 == "Youtube":
         print("Correct!")
     else: 
         print("Wrong! Youtube is the first streaming platform.")
 
     print("Game over!")
     Play = input("Do you want to play again? (Yes/No): ")
     if Play != "yes":
         print("Thank you for playing.")
         break
        

Quiz()