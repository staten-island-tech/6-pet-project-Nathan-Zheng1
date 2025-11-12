import random
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
            self.money += 100
            self.sleepiness += 2
            self.hunger += 1
            self.happiness -= 1
            print("Kitty is working! Increased cash. Increased Sleepiness and Hunger. Decreased happiness.")

    def play(self):
        if self.sleepiness >= 8:
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
            user_input = input("Are you sure you would like to proceed? Kitty will lose 2 sleepiness and age up at the cost of gaining 3 hunger.")
            if user_input == "yes":
                self.sleepiness -= 2
                self.hunger += 3
                self.age += 1
                print("Bold move.")
            elif user_input == "no":
                print("Wise choice, come back later.")
        
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
                self.food -= 0.5
                print("Kitty is feeling less hungry now! Hunger decreased by 0.5")
    
    def wheel(self):
            while True:
                if self.money < 25:
                    print("Halt! You do not have enough money to play!")
                    break
                else:
                    user_input = input("Would you like to spin the magnificent wheel of doom? The price per spin is 25 dollars! Spinning a value of 1 will win the huge jackpot! The values 2, 3, 4, or 5 will all award a prize...and the number 67... Type 'exit' to leave.")
                    if user_input == "exit":
                        print("Goodbye!")
                        break
                    elif user_input == "yes":
                        self.money -= 25
                        x = random.randint(1,100)
                        print(x)
                        if x == 1:
                            print("You won the jackpot! Cash increased by 1000. Happiness increased by 5")
                            self.happiness += 5
                            self.money += 1000
                        elif x == 2 or x == 3 or x == 4 or x == 5:
                            print("You won a prize! Increased cash by 50, increased cat food by 1. Happiness increased by 1.")
                            self.money += 50
                            self.food += 1
                        elif x == 67:
                            print("How unfortunate...cash decreased by 67...")
                            self.money -= 67
                        else:
                            print("Unlucky! No winner this time. ")
                    elif user_input == "no":
                        print("Come again next time!")
                    else:
                        print("Invalid response.")

Kitty = Pet("Kitty", 1, 5, 0, 5, 1, 100)

print("Welcome to Kitty's adventure! In this game, you control a 'Pet' called Kitty! Kitty is able to run  a multitude of functions: Eat, Sleep, Play, Stats, Work, and Shop. Your goal is to make it to the age of 100! To do this, you must be able to sleep 100 times, but be warned, each time you sleep is costly! Make sure to keep your stats good before you sleep, or kitty might just die...Keep him alive, eat him, kill him, or let him live a normal life! All the powers in your hands!")
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
    elif user_input == "Gamble":
        Kitty.wheel()
    else:
        print("Invalid input, try again.")