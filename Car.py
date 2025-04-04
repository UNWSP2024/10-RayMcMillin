#Ray McMillin, 4/4/25, Car Program

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed

car = Car(2006, "Honda")

for _ in range(5):
    car.accelerate()
    print(f"Current Speed: {car.get_speed()} mph")

for _ in range(5):
    car.brake()
    print(f"Current Speed: {car.get_speed()} mph")
