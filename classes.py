# This is a script where I will attempt to learn object oriented programming by creating a pokemon game
from enum import Enum

class Stats(Enum):
    Attack = 0
    Defence = 1
    Speed = 2
    Health = 3

class Type(Enum):
    NORMAL = 0
    GRASS = 1
    WATER = 2
    FIRE = 3

class Pokemon:
    # init is used to set values for each square
    def __init__(self,name="", type=Type.NORMAL, stats=[], moveset=[]):
        self.name = name
        self.type = type
        self.stats = stats 
        self.moveset = moveset 
    # This is the getter
    # self is used to refer to an object that we dont possess a name for
    def get_name(self):
        print("Retrieving the name")
        return self.name
    # we put a __ before this private field

    # This is a setter
    def set_name(self, value):
        self.name = value

    # This is the getter
    def get_type(self):
        print("Retrieving the Type")
        return self.type

    # This is the setter
    def set_type(self, value):
        self.type = value 

    # Moveset
    def set_stats(self, value):
        self.stats = value
    
    def get_stats(self):
        return self.stats
    
    # Moveset
    def set_moveset(self, value):
        self.moveset = value
    
    def get_moveset(self):
        return self.moveset

    def fight(self, opponent):
        user_input = input("Choose " + self.name + "  move")
        print(self.name + " used ", user_input)
        # battle calculations
        # RAW attack value v1.0
        damage = self.stats[Stats.Attack.value]
        opponent.stats[Stats.Health.value] -= damage 

    def __str__(self) -> str:
        return "Your Pokemon is: " + self.name + " and it is a " + self.type.name +" type!" 




