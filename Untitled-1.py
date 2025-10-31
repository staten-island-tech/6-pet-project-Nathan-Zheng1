class Pet:
    def __init__(self, name, age, happiness, sleep):
        Kitty = Pet("Kitty", 1, 0, 10)
        self.name = name
        self.age = age
        self.__happiness = happiness
        self.sleep = sleep
        
    def play(self):
        self.__happiness += 1
        self.__sleep -= 1
        print(f"The cat is having fun! Happiness increased to {self.happiness}.")
        
    def show_happiness(self):
        return f"Happiness: {self.happiness}"
    
    def sleeping(self):
        self.sleep += 1
        print(f"{self.name} is sleeping! Sleep increased by 1!")
Pet.play(Pet)