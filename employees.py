class CityEmployee:
    used_ids = set()

    def __init__(self, employee_id, name, salary):
        self.__employee_id = None
        self.__name = ""
        self.__salary = 0

        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if value in CityEmployee.used_ids:
            raise ValueError("Duplicate employee ID is not allowed.")

        if value <= 0:
            raise ValueError("Employee ID must be positive.")

        self.__employee_id = value
        CityEmployee.used_ids.add(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Name must have at least 2 characters.")

        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")

        if value < 12000:
            raise ValueError("Salary is too low for a city employee.")

        self.__salary = value

    def calculate_bonus(self):
        return self.salary * 0.05

    def show_details(self):
        return f"{self.name} | ID: {self.employee_id} | Salary: €{self.salary:.2f}"


class TransportStaff(CityEmployee):
    def __init__(self, employee_id, name, salary, licence_type):
        super().__init__(employee_id, name, salary)
        self.__licence_type = licence_type

    @property
    def licence_type(self):
        return self.__licence_type

    def calculate_bonus(self):
        return self.salary * 0.08


class HealthcareStaff(CityEmployee):
    def __init__(self, employee_id, name, salary, department):
        super().__init__(employee_id, name, salary)
        self.__department = department

    @property
    def department(self):
        return self.__department

    def calculate_bonus(self):
        return self.salary * 0.10


class ITStaff(CityEmployee):
    def __init__(self, employee_id, name, salary, programming_language):
        super().__init__(employee_id, name, salary)
        self.__programming_language = programming_language

    @property
    def programming_language(self):
        return self.__programming_language

    def calculate_bonus(self):
        return self.salary * 0.12