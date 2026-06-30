from employees import CityEmployee, TransportStaff, HealthcareStaff, ITStaff
from citizens import Citizen, StudentCitizen, WorkingCitizen, SeniorCitizen, TouristCitizen
from transport import Bus, Taxi, Metro, Train, ElectricScooter, AirTaxi
from services import FireEmergencyService


def main():
    print("SMART CITY OOP SYSTEM")
    print("=" * 50)

# Employees

    print("\nSection A - Employees")

    employees = [
        CityEmployee(1, "Ana", 30000),
        TransportStaff(2, "Bruno", 32000, "Bus Licence"),
        HealthcareStaff(3, "Clara", 45000, "Emergency Department"),
        ITStaff(4, "Daniel", 50000, "Python")
    ]

    for employee in employees:
        print(employee.show_details())
        print(f"Bonus: €{employee.calculate_bonus():.2f}")
        print("-" * 30)

# Citizens

    print("\nSection B - Citizens")

    citizens = [
        StudentCitizen(101, "Maria", 21, "ST123"),
        WorkingCitizen(102, "John", 35, "Full-time"),
        SeniorCitizen(103, "Robert", 70, "PN456"),
        TouristCitizen(104, "Laura", 28, "BR987")
    ]

    for citizen in citizens:
        print(citizen.show_details())
        print(f"City Benefit: €{citizen.calculate_city_benefits()}")
        print("-" * 30)

    
# Transport

    print("\nSection C - Transport")

    transports = [
        Bus(201, "Bus", 2.00, 0.8),
        Taxi(202, "Taxi", 4.00, 1.5),
        Metro(203, "Metro", 2.50, 0.4),
        Train(204, "Train", 3.00, 0.6),
        ElectricScooter(205, "Electric Scooter", 1.00, 0.1),
        AirTaxi(206, "Air Taxi", 20.00, 2.5)
    ]

    distance = 10

    for transport in transports:
        print(f"Transport: {transport.name}")
        print(f"Fare for {distance}km: €{transport.calculate_fare(distance):.2f}")
        print(f"Emissions: {transport.calculate_emissions(distance):.2f}kg CO2")
        print("-" * 30)

# Emergency Service


    print("\nSection D - Emergency Service")

    emergency = FireEmergencyService(
        301,
        "Fire Emergency Service",
        500,
        priority_level=5,
        emergency_timer=8,
        resources=6
    )

    print(emergency.activate_service())
    print(emergency.generate_report())
    print(f"Emergency Cost: €{emergency.calculate_cost():.2f}")

# Validation Tests

    print("\nVALIDATION TESTS")

    try:
        invalid_employee = CityEmployee(1, "Duplicate", 30000)
    except ValueError as error:
        print(f"Validation worked: {error}")

    try:
        invalid_salary = CityEmployee(5, "Bad Salary", -100)
    except ValueError as error:
        print(f"Validation worked: {error}")

    try:
        invalid_distance = Bus(207, "Invalid Bus", 2.00, 0.8)
        invalid_distance.calculate_fare(-5)
    except ValueError as error:
        print(f"Validation worked: {error}")

    try:
        invalid_emergency = FireEmergencyService(
            302,
            "Invalid Emergency",
            500,
            priority_level=10,
            emergency_timer=8,
            resources=6
        )
    except ValueError as error:
        print(f"Validation worked: {error}")


if __name__ == "__main__":
    main()