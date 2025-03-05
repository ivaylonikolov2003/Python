class Car:
    def __init__(self, brand, model, year, fuel_consumption, fuel_tank = 55, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption
        self.fuel_tank = fuel_tank
        self.fuel_level = fuel_tank
        self.service_history = []

    def drive(self, km):
        fuel_needed = (km / 100) * self.fuel_consumption
        if fuel_needed > self.fuel_level:
            print("Not enough fuel to drive this distance!")
        else:
            self.mileage += km
            self.fuel_level -= fuel_needed
            print(f"Car drove {km} km. Remaining fuel: {self.fuel_level:.2f}")

    def refuel(self, liters):
        if self.fuel_level + liters > self.fuel_tank:
            print("Too much fuel! Tank is full.")
            self.fuel_level = self.fuel_tank
        else:
            self.fuel_level += liters
            print(f"Refueled {liters} L. Current fuel: {self.fuel_level:.2f} L")

    def add_service_record(self, date, description, cost):
        self.service_history.append({"date": date, "description": description, "cost": cost})
        print(f"Added service record: {date} - {description} (${cost})")

    def show_service_history(self):
        if not self.service_history:
            print("No service history available")
        else:
            print("Service History:")
            for record in self.service_history:
                print(f"{record['date']} - {record['description']} (${record['cost']})")

    def __str__(self):
        return (f"Car: {self.brand} {self.model} ({self.year})\n"
                f"Mileage: {self.mileage} km\n"
                f"Fuel Level: {self.fuel_level:.2f} L")

