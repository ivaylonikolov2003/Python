from Car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity, mileage=0):
        super().__init__(brand, model, year, fuel_consumption=0, mileage=mileage)
        self.battery_capacity = battery_capacity
        self.battery_level = battery_capacity

    def charge(self, kWh):
        if self.battery_level + kWh > self.battery_capacity:
            print("Battery is fully charged!")
            self.battery_level = self.battery_capacity
        else:
            self.battery_level += kWh
            print(f"Charged {kWh} kWh. Current battery level: {self.battery_level:.2f} kWh")

    def drive(self, km):
        battery_needed = km * 0.2
        if battery_needed > self.battery_level:
            print("Not enough battery to drive this distance!")
        else:
            self.mileage += km
            self.battery_level -= battery_needed
            print(f"Electric car drove: {km} km. Remaining battery: {self.battery_level:.2f} kWh")

    def __str__(self):
        return (f"Electric Car: {self.brand} {self.model} ({self.year})\n"
                f"Mileage: {self.mileage} km\n"
                f"Battery Level: {self.battery_level:.2f} kWh")