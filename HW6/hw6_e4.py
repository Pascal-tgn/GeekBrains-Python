class Car:
    speed: float
    color: str
    name: str
    is_police: bool
    speed: float(0.0)
    direction: str

    def __init__(self, color, name, is_police=False, speed=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def turn(self, direction):
        self.direction = direction
        print(f"{self.name} turned to the {self.direction}.")

    def stop(self):
        self.speed = 0
        print(f"{self.name} stopped.")

    def show_speed(self):
        print(f"{self.speed}'s speed is {self.speed} ")

    def go(self, speed):
        self.speed = speed
        self.show_speed()


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} is speeding! Current speed is {self.speed}")
        else:
            print(f"{self.name}'s speed is {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} is speeding! Current speed is {self.speed}")
        else:
            print(f"{self.name}'s speed is {self.speed}")


class SportCar(Car):
    def __init__(self, max_speed, color, name, is_police=False, speed=0):
        super(SportCar, self).__init__(color, name, is_police, speed)
        self.max_speed = max_speed


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True, speed=0):
        super(PoliceCar, self).__init__(color, name, is_police, speed)
        self.is_police = True


car1 = TownCar(color='Red', name='ABC123')
car2 = WorkCar(color='White', name='ZSL976')
car3 = SportCar(color='Red', name='AAA111', max_speed=350)
car4 = PoliceCar(color='White', name='LAPD327')

car1.speed = 100
car1.show_speed()
car1.speed = 50
car1.show_speed()
car2.speed = 50
car2.show_speed()
car2.turn("North")
print(f"{car4.is_police}")
