from Car import Car
from ElectricCar import ElectricCar

def main():
    car1 = Car("Audi", "A3 SportBack", 2008, 5.9)
    car1.drive(500)
    car1.add_service_record("2023-05-10", "Oil change", 50)
    car1.add_service_record("2024-02-15", "Brake replacement", 200)
    car1.show_service_history()
    print(car1)

    #tesla = ElectricCar("Tesla", "Model S", 2022, 100)
    #tesla.drive(200)
    #print(tesla)
    #tesla.charge(30)

if __name__ == "__main__":
    main()