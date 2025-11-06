class Pet:
    def __init__(self, name, age, happiness, sleepiness, hunger):
        self.name = name
        self.age = age
        self.happiness = happiness
        self.sleepiness = sleepiness
        self.hunger = hunger
    
    def play(self):
        if self.sleepiness >= 5:
            print("Kitty is too tired to play!")
        else:
            self.happiness += 1
            self.sleepiness += 1
            print("Kitty is having fun, but is now tired! Happiness increased by 1, sleepiness increased by 1.")
    
    def sleep(self):
        if self.sleepiness <= 1:
            print("No need to sleep! Kitty is energetic!")
        else:
            self.sleepiness += 1

    def show_stats(self):
        print(self.__dict__)

    def eat(self):
        if self.hunger <= 2:
            print("Kitty is NOT hungry right now.")
        else:
            self.hunger -= 1
            print("Kitty is feeling less hungry now! Hunger decreased by 1.")

Kitty = Pet("Kitty", 1, 1, 0, 5)

print("Welcome to Kitty's adventure! In this game, you control a 'Pet' called Kitty! Keep him alive, eat him, kill him, or let him live a normal life! All the powers in your hands!")
while True:
    user_input = input("Would you like to commit an action? Type 'exit' to leave.")
    if user_input == "exit":
        print("Thank you for playing!")
        break
    if Kitty.hunger >= 10:
        print("You forgot to feed kitty! Kitty has died!")
        break
    if user_input == "Play":
        Kitty.play()
    elif user_input == "Sleep":
        Kitty.sleep()
    elif user_input == "Stats":
        Kitty.show_stats()
    elif user_input == "Eat":
        Kitty.eat()