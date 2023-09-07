class Player:
    def __init__(self):
        self.name = ""
        self.statPoints = 0
        self.strength = 0
        self.magic = 0
        self.armor = 0
        self.health = 0
        self.level = 1
        self.charClass = ""
    
    def selectClass(self):
        options = ["Barbarian", "Paladin", "Sorcerer"]
        print("\nPlease select your class.")
        print("Options: Barbarian, Paladin, Sorcerer")
        classChosen = False
        while classChosen == False:
            classChoice = input()
            if classChoice in options:
                if classChoice == options[0]:
                    self.strength = 3
                    self.health = 3
                    print("You have chosen Barbarian, your stats will be:")
                    p1.printStats()
                if classChoice == options[1]:
                    self.strength = 1
                    self.magic = 1
                    self.armor = 2
                    self.health = 2
                    print("You have chosen Paladin, your stats will be:")
                    p1.printStats()
                if classChoice == options[2]:
                    self.magic = 4
                    self.health = 2
                    print("You have chosen Sorcerer, your stats will be:")
                    p1.printStats()
                classChosen = True
            else:
                print("Thats not an option, try again.")

    def printStats(self):
        print(f"Level: {self.level}\nStrength: {self.strength}\nMagic: {self.magic}\nArmor: {self.armor}\nHealth: {self.health}\n\nYou have {self.statPoints} stat points available.")




p1 = Player()
print("Hello adventurer! To start, please enter your name below.")
p1.name = input()
print(f"\nNow {p1.name}, the deathly dungeon awaits ahead of you. Go forth and expel the enemy from this plane!")
p1.selectClass()
