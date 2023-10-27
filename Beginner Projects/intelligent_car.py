class Car:
    def __init__(self, fuel_consumption, possible_destinations):
        self.fuel_consumption = fuel_consumption
        self.possible_destinations = possible_destinations
        self.total_distance = 0
        self.distance_left = 0

    def ride(self, distance):
        try:
            self.check_distance(distance)
        except Exception as e:
            print(e)
        else:
            self.total_distance += distance
            self.distance_left -= distance
            print(f"The ride was successfull! Distance traveled: {distance}")
        
    def check_distance(self, distance):
        if self.distance_left < distance:
            raise ValueError("Not enough fuel, recharge the car!")   

    def recharge(self, fuel):
        self.distance_left += fuel * self.fuel_consumption
        print(f"Car charged successfully! Distance left to ride: {self.distance_left}.")

    def calculate_average_speed(self, distance, duration):
        try:
            average_speed = distance / duration
            return average_speed
        except ZeroDivisionError:
            return distance

    def ride_to_destination(self, destination):
        if destination in self.possible_destinations:
            distance = self.possible_destinations[destination]
            self.ride(distance)
            print(f"Reached {destination}!")
        else:
            print("Destination not in possible destinations!")
    
    
possible_destinations = {
    "Eriador": 100,
    "Gondor" : 50
}

ford_mustang = Car(14, possible_destinations)
ford_mustang.ride(10)
ford_mustang.recharge(10)
ford_mustang.ride(50)

average_speed = ford_mustang.calculate_average_speed(150, 0)
print("Average speed: {average_speed}")

ford_mustang.ride_to_destination("Gondor")

ford_mustang.ride_to_destination("Wonderland")