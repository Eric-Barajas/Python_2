class Pet:
    def __init__(self, name , type , tricks, noise ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5 
        self.health += 10
        return self
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    def noise(self):
        print(self.noise)



class Ninja:
    def __init__( self, first_name , last_name , treats , pet_food , pet ):
        self.first_name= first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
# implement the following methods:
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat
        return self
    def bathe(self):
        self.pet.noise()
        return 

Mumbles = Pet("Mr.Mumbles", "Kitten",["go undercover","barrel role","jump on command"], "MEOW" )

Jordan = Ninja("Jordan", "Jarell", "Beggin", "Iams", Mumbles )

Jordan.walk()

Mumbles.health()