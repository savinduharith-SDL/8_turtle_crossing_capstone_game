from car import Car
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def remove_out_of_screen_cars(self):
        for car in self.cars:
            if car.xcor() > -280:
                pass
                #TODO : Implement the logic


