from car import Car
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 0

    def add_car(self):
            new_car = Car()
            self.cars.append(new_car)

    def remove_out_of_screen_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.level)

    def increase_speed(self):
        self.level += 1
