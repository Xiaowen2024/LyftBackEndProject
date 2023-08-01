from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, worn_array):
        self.worn_array = worn_array
        self.threshold = 0.9

    def needs_service(self):
        for worn_value in self.worn_array:
            if worn_value >= self.threshold:
                return True 
        return False 