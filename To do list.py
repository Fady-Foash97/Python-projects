tasks = []
completed_tasks = []

while True:
    print("Menu:")
    options = {
        "1. Add Task": 1, 
        "2. Mark Task as Done": 2,
        "3. Display Todo List": 3,
        "4. Display Completed List": 4,
        "5. Quit": 5
    }

    for option in options:
        print(option)

    choice = input("Enter your choice: ")

    if choice == "1":
           task = input("Enter task: ")
           tasks.append(task)
           print(f"Task added: {task}")
    elif choice == "2":
            if not tasks:
                 print("No tasks done")
            else:
              for i, task in enumerate(tasks):
                   print(f"{i + 1}. {task}")
                   done_index = input(int("Enter task number to mark as done: ")) - 1
                   if 0 <= done_index < len(tasks):
                        completed_task = tasks.pop(done_index)
                        completed_tasks.append(completed_task)
                        print(f"Task done: {completed_task}")
                   else:
                        print("Invalid task number.")
                   
    elif choice == "3":
         print("\n To-do list")
         if tasks:
          for task in tasks:
              print(f"- {task}") 
         else:
              print("You have no tasks")      
    elif choice == "4":
         if completed_tasks:
          print("\n Completed list")
         for task in completed_tasks:
              print(f"- {task}")
         else:
              print("No completed tasks yet.")     
    elif choice == "5":
         print("Goodbye!")
         break
    else:
         print("Invalid choice. Please enter a number from 1 to 5.")
        
          
    
     
         
         
    

     
      

        
