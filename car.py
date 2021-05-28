class Car:
    model = "Toyota"
    def __init__(self,color,mileage,material):
        self.color = color
        self.mileage = mileage
        self.material = material
    def new_car(self):
        return f"I just bought a new {self.model} that has a mileage of {self.mileage} liters/km"
    def car_material(self):
        return f"My {self.model} is {self.color} and made of {self.material}"
      