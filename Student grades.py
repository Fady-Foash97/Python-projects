def Student_grades():
 while True:
    grades = float(input("Insert student grades: "))
    if grades >= 90 and grades == 100:
        print("Excellent!")
    elif grades >= 80 and grades < 90:
        print("Very good")
    elif grades >= 70 and grades < 80:
        print("good")
    elif grades >= 60 and grades < 70:
        print("Okay")
    elif grades < 60:
        print("Failed! try again next time.")
    repeat = str(input("Do you want to repeat the process? "))
    if repeat != "Yes":
        print("Process terminated")
        break



Student_grades()