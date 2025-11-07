class Pet:
    def __init__(self, name, age, happiness, sleepiness, hunger, food, money):
        self.name = name
        self.age = age
        self.happiness = happiness
        self.sleepiness = sleepiness
        self.hunger = hunger
        self.food = food
        self.money = money
    
    def work(self):
        if self.sleepiness >= 5:
            print("Kitty is too tired to work!")
        else:
            self.money += 100
            self.sleepiness += 2
            self.hunger += 1
            self.happiness -= 1
            print("Kitty is working! Increased cash. Increased Sleepiness and Hunger.")

    def play(self):
        if self.sleepiness >= 5:
            print("Kitty is too tired to play!")
        else:
            self.happiness += 1
            self.sleepiness += 1
            self.hunger += 0.5
            print("Kitty is having fun, but is now tired! Happiness increased by 1, sleepiness increased by 1.")
    
    def sleep(self):
        if self.sleepiness <= 1:
            print("No need to sleep! Kitty is energetic!")
        else:
            self.sleepiness += 1
            self.hunger += 2
            self.age += 1
            print("Kitty is sleeping...but Kitty has become hungry and grown up! Sleep increased by 1. Hunger increased by 2. Age increased by 1.")
        
    def shop(self):
        user_input = input("Welcome to cat central! Would you like to buy some cat food?")
        if user_input == "no":
            print("Alright! Come back next time!")
        elif user_input == "yes":
            user_input = input("Alright! Cat food is 75 dollars. Would you like to proceed?")
            if user_input == "yes":
                self.money -= 75
                self.food += 1
                print("Thank you for your purchase! See you soon.")

    def show_stats(self):
        print(self.__dict__)

    def eat(self):
            if self.food == 0:
                print("Kitty does not have any food to eat.")
            else:
                self.hunger -= 0.5
                print("Kitty is feeling less hungry now! Hunger decreased by 1.")

Kitty = Pet("Kitty", 1, 5, 0, 5, 1, 100)

print("Welcome to Kitty's adventure! In this game, you control a 'Pet' called Kitty! Kitty is able to run  a multitude of functions: Eat, Sleep, Play, Stats, Work, and Shop. Your goal is to make it to the age of 100! Keep him alive, eat him, kill him, or let him live a normal life! All the powers in your hands!")
while True:
    user_input = input("Would you like to commit an action? Type 'exit' to leave.")
    if user_input == "exit":
        print("Thank you for playing!")
        break
    if Kitty.hunger >= 10:
        print("You forgot to feed kitty! Kitty has died!")
        break
    if Kitty.hunger <= 0:
        print("Oh no! You fed Kitty too much! Kitty exploded!")
        break
    if Kitty.happiness <= 0:
        print("Kitty is depressed...game. over.")
        break
    if user_input == "Play":
        Kitty.play()
    elif user_input == "Sleep":
        Kitty.sleep()
    elif user_input == "Stats":
        Kitty.show_stats()
    elif user_input == "Eat":
        Kitty.eat()
    elif user_input == "Work":
        Kitty.work()
    elif user_input == "Shop":
        Kitty.shop()