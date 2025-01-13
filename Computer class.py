class Computer:
        def __init__(self, hardware):
                self.hardware = hardware 

        def __str__(self):
                return self.hardware

keyboard = Computer("Keyboard")
mouse = Computer("Mouse")
monitor = Computer("Monitor")
speakers = Computer("Speakers")
hard_drive = Computer("Hard drive")
printer = Computer("Printer")
print(f"{keyboard} is used to write letters and numbers")
print(f"{mouse} is used to click on software")
print(f"{monitor} is used to display the computer's operations")
print(f"{speakers} are used to extract sound")
print(f"The {hard_drive} is used to store data")
print(f"{printer} is used to print text as documents and papers")