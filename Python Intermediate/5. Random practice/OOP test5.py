class Vehicle:
    def __init__(self, name, max_speed, mileage, colour="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

class Bus(Vehicle):

    def car_stats():
        return f"Color:", {self.colour}, "Vehicle name:", {self.name}, "Speed:", {self.max_speed}, "Mileage:", {self.mileage}


Bus("nelly", 180, 12, "white").car_stats()