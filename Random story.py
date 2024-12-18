import random

def story_tel():

     Story = ["Oliver Twist", "Dracula", "Moby Dick", "Monte cristo"]
     Author = ["Mark Twain", "Bram Stoker", "Herman Melville", "Alexandre Dumas"]
     Story_gen = random.choice(Story)
     Author_gen = random.choice(Author)
     print(f"{Story_gen} is written by {Author_gen} ")



story_tel()