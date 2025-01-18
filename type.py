import random

class Hat:
    
    houses = ["Gryffindor", "Hupplepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Harry")