class Pet:
    def __init__(Kitty, name, age, happiness, sleep):
        Kitty.name = name
        Kitty.age = age
        Kitty.__happiness = happiness
        Kitty.sleep = sleep
        Meowy = Pet("Meowy", 1, 0, 10)
        
    def play(Kitty):
        Kitty.__happiness += 1
        Kitty.sleep -= 1
        print(f"The cat is having fun! But its become tired! Happiness increased to {Kitty.__happiness}. Energy decreased to {Kitty.sleep}")
        return Kitty.__happiness and Kitty.sleep
        
    def show_happiness(Kitty):
        print(f"Meowy's happiness is now {Kitty.__happiness}")
        return Kitty.__happiness
    
    def sleeping(Kitty):
        Kitty.sleep += 1
        print(f"{Kitty.name} is sleeping! Sleep increased by 1!")
Pet.play("Kitty")