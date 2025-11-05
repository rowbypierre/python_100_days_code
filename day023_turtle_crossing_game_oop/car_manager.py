from turtle import Turtle
from random import choice, choices

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
CAR_LOCATIONS = [(x, y) for x in range(-300, 300, 60) for y in range(-250, 250, 50)]


class CarManager:
    def __init__(self, total_cars):
        self.total_cars = int(total_cars)
        self.cars = self.add_cars()
        self.max_speed = STARTING_MOVE_DISTANCE

    def add_cars(self):
        cars = []
        for location in choices(CAR_LOCATIONS, k=self.total_cars):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.turtlesize(1, 3)
            car.fillcolor(choice(COLORS))
            car.setheading(0)
            car.goto(*location)
            cars.append(car)

        return cars

    def drive_cars(self):
        "Drive cars east "
        for car in self.cars:
            car.forward(self.max_speed)

    def speed_up_cars(self):
        "Speed up cars."
        self.max_speed += MOVE_INCREMENT

    def return_cars(self):
        "Return vehicles to start position when out of view."
        for car in self.cars:
            if car.xcor() > 350:
                car.goto(car.xcor() * -1, car.ycor())

    def is_road_kill(self, animal):
        "Confirm (bool) that animal (Turtle()) has contacted a car."
        accidents = [True if car.distance(animal) < 20 else False for car in self.cars ]
        return any(accidents)
