from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, worn_array):
        self.worn_array = worn_array
        self.threshold = 3

    def needs_service(self):
        return sum(self.worn_array) >= self.threshold