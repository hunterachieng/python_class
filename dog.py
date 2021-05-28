class Dog:
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color
    def get_lost(self):
        return f"A {self.color} {self.age} {self.breed} has just been rescued from the borehole"

    def running(self):
        return f"{self.breed} are quite fast."
        

       