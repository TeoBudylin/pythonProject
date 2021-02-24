class Car:
    speed = 0
    def __init__(self, color, name, is_police=0):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"автомобиль начал движение со скоростью {self.speed} км/ч")

    def stop(self):
        self.speed = 0
        print("Автомобиль остановился")

    def turn(self, direction):
            if direction == "right":
                print("автомобиль повернул направо")
            elif direction == "left":
                print("автомобиль повернул налево")
            else:
                print("неправильное направление")

    def show_speed(self):
        print(f"Скорость автомобиля - {self.speed} км/ч")

class TownCar(Car):
    def show_speed(self):
        print(f"Скорость автомобиля - {self.speed} км/ч")
        if self.speed > 40:
            print("Скорость превышена!")

town_car_1 = TownCar(color="red", name="Ferrari")


town_car_1.go(speed=100)

town_car_1.turn("right")

town_car_1.show_speed()