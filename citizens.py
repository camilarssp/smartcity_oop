class Citizen:
    def __init__(self, citizen_id, name, age):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__age = 0

        self.age = age

    @property
    def citizen_id(self):
        return self.__citizen_id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")

        self.__age = value

    def calculate_city_benefits(self):
        return 0

    def show_details(self):
        return f"{self.name} | Age: {self.age}"


class StudentCitizen(Citizen):
    def __init__(self, citizen_id, name, age, student_card):
        super().__init__(citizen_id, name, age)
        self.__student_card = student_card

    @property
    def student_card(self):
        return self.__student_card

    def calculate_city_benefits(self):
        return 40


class WorkingCitizen(Citizen):
    def __init__(self, citizen_id, name, age, employment_status):
        super().__init__(citizen_id, name, age)
        self.__employment_status = employment_status

    @property
    def employment_status(self):
        return self.__employment_status

    def calculate_city_benefits(self):
        return 20


class SeniorCitizen(Citizen):
    def __init__(self, citizen_id, name, age, pension_number):
        super().__init__(citizen_id, name, age)
        self.__pension_number = pension_number

    @property
    def pension_number(self):
        return self.__pension_number

    def calculate_city_benefits(self):
        return 60


class TouristCitizen(Citizen):
    def __init__(self, citizen_id, name, age, passport_number):
        super().__init__(citizen_id, name, age)
        self.__passport_number = passport_number

    @property
    def passport_number(self):
        return self.__passport_number

    def calculate_city_benefits(self):
        return 15