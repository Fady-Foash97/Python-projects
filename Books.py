while True:
 Books = {
     "Mark Twain": "Tom Sawyer",
     "Bram Stoker": "Dracula",
     "Herman Melville": "Moby Dick",
     "Alexandre Dumas": "Three musketeers"
 }

 for author, book in Books.items():
     print(f"-{book}")
 Select = input("Select a book from the list: ")
 for author, book in Books.items():
  if Select == book:
     print(f"{book} by {author}")
 repeat = input("Want another book? ")
 if repeat != "yes":
     print("Thank you for purchasing")
     break
