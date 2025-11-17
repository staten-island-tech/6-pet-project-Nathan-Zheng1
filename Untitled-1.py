import random
class Pet:
    def __init__(self, name, age, happiness, sleepiness, hunger, food, money, health):
        self.name = name
        self.age = age
        self.happiness = happiness
        self.sleepiness = sleepiness
        self.hunger = hunger
        self.food = food
        self.money = money
        self.health = health
    
    def work(self):
            x = random.randint(1,10)
            if x == 1:
                user_input = input("While working, something random occured...your co-worker has offered to leave the building and risk your salary for...something? You agree, not wanting to live through you shift any longer. Infront of you are three choices to escape: (1) exit the building via the main door, (2) climb out the window, (3) climb through the vent inside the bathroom.")
                x = int(user_input)
                if x == 1:
                    user_input = input("Intresting plan...the guard at the front was sleeping! You and your co-worker proceed to leave the building, completely unexpected! Suddenly, your co-worker tells you he plans to rob a bank...you've came so far already, right? Now, you have to discuss a way to rob a bank. (1) Enter through the main door, threaten everyone with a gun, and rush to escape the building. (2) Sneak your way to the back door, breaking in, and stealing from cash vaults. (3) Enter through the main door, threaten cashier with gun, leave the building.")
                    if x == 1:
                        print("You run in, guns blazing, firing shots into the floor! Everythings looking well!...for the first 4 seconds. Looks like you forgot guards exist! You and your coworker get shot and die...")
                        Kitty.health -= 10
                    elif x == 2:
                        print("You sneak your way through the guards, reaching the back door. Once there, you open the vault, and slowly sneak through the hallways. Banks have cameras...your not slick. The duo is caught on the cameras, and the cops are called. By the time your done robbing everything, the cops are already there. You get shot on the spot.")
                        Kitty.health -= 10
                    elif x == 3:
                        print("You walk up to the cashier, and pull a gun concealed by your work bag. Terrified, the cashier sowly puts all the money in the register inside the bag, and you walk out the building with not much, but it was, afterall, the safest offer.")
                        Kitty.money += 1250
                        Kitty.happiness += 5
                elif x == 2:
                    print("As you open the window, a large draft blows into the office! Papers go flying, all employees are alarmed, the office is pure chaos! You rush out the window...on the 10th floor?")
                    Kitty.health -= 10
                elif x == 2:
                    print("Sneaky...I like that. You proceed through the vents, but forgot to account for one thing...the vents are paper thin. You fall through the vent above the office, smashing your back into the floor. The boss punished you!")
                    self.money -= 100
            self.money += 125
            self.sleepiness += 1.5
            self.hunger += 1.5
            self.happiness -= 1
            print("Kitty is working! Increased cash. Increased Sleepiness and Hunger. Decreased happiness.")

    def play(self):
        if self.sleepiness >= 8:
            print("Kitty is too tired to play!")
        else:
            self.happiness += 2
            self.sleepiness += 1
            self.hunger += 0.5
            print("Kitty is having fun, but is now tired! Happiness increased by 2, sleepiness increased by 0.5, and hunger increased by 0.5.")
    
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
            else:
                print("Invalid Input, try again.")
        
    def shop(self):
        user_input = input("Welcome to cat central! Cat food is 100 dollars each, how many would you like? Type 'exit' to leave.")
        if user_input == "exit":
            print("Alright! Come back next time!")
        else:
            x = int(user_input)
            y = x * 100
            self.money -= 100 * x
            self.food += 1 * x
            print("Thank you for your purchase! See you soon.")

    def show_stats(self):
        print(self.__dict__)

    def eat(self):
            if self.food == 0:
                print("Kitty does not have any food to eat.")
            else:
                self.hunger -= 1
                self.food -= 0.25
                print("Kitty is feeling less hungry now! Hunger decreased by 1, food decreased by 0.25.")
    
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
                        self.money -= 20
                        x = random.randint(1,999)
                        print(x)
                        if x == 1:
                            print("You won the jackpot! Cash increased by 10000. Happiness increased by 10")
                            self.happiness += 10
                            self.money += 10000
                        elif x == 2 or x == 3 or x == 4 or x == 5:
                            print("You won a prize! Increased cash by 500, increased cat food by 2. Happiness increased by 2.")
                            self.money += 500
                            self.food += 2
                            self.happiness += 2
                        elif x == 69:
                            print("Hm....69?...Here, have 69 dollars!")
                            self.money += 69
                        elif x == 67:
                            print("How unfortunate...cash decreased by 67...")
                            self.money -= 67
                        elif x == 999 or x == 677:
                            print("Intresting...have 1000!")
                            self.money += 1000
                        else:
                            print("Unlucky! No winner this time. ")
                    elif user_input == "no":
                        print("Come again next time!")
                    else:
                        print("Invalid response.")

Kitty = Pet("Kitty", 1, 5, 0, 5, 1, 100, 10)

print("Welcome to Kitty's adventure! In this game, you control a 'Pet' called Kitty! Kitty is able to run  a multitude of functions which you can find in info. Your goal is to make it to the age of 100! To do this, you must be able to sleep 100 times, but be warned, each time you sleep is costly! Make sure to keep your stats good before you sleep, or kitty might just die...Keep him alive, eat him, kill him, or let him live a normal life! All the powers in your hands! Please type 'Info' of you need more information about this game.")
while True:
    if Kitty.hunger >= 10:
        print(f"You forgot to feed kitty! Kitty has died! Age: {Kitty.age}")
        break
    if Kitty.hunger <= 0:
        print(f"Oh no! You fed Kitty too much! Kitty exploded! Age: {Kitty.age}")
        break
    if Kitty.happiness <= 0:
        print(f"Kitty is depressed...game. over. Age: {Kitty.age}")
        break
    if Kitty.sleepiness >= 10:
        print("Oh no! Kitties sleepiness reached 10! Kitty fell asleep randomly and got robbed. Sleepiness decreased by 2, money decreased by 100")
        Kitty.money -= 100
        Kitty.sleepiness -= 2
    if Kitty.health <= 0:
        print("Kitty has died to a injury.")
    user_input = input("Would you like to commit an action? Type 'exit' to leave.")
    if user_input == "exit":
        print("Thank you for playing!")
        break
    if user_input == "Info":
        print("In this game, you control a 'Pet' named Kitty. All functions currently availible include Eat, Sleep, Play, Stats, Work, Shop and Gamble. Kitty will die if hunger exceeds 10, hunger decreases to 0, or if happiness decreases to 0.")
    elif user_input == "Play":
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