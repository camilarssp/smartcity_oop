from abc import ABC, abstractmethod


class SmartService(ABC):
    def __init__(self, service_id, service_name, base_cost):
        self.__service_id = service_id
        self.__service_name = service_name
        self.__base_cost = 0

        self.base_cost = base_cost

    @property
    def service_id(self):
        return self.__service_id

    @property
    def service_name(self):
        return self.__service_name

    @property
    def base_cost(self):
        return self.__base_cost

    @base_cost.setter
    def base_cost(self, value):
        if value < 0:
            raise ValueError("Base cost cannot be negative.")

        self.__base_cost = value

    @abstractmethod
    def activate_service(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass

    @abstractmethod
    def calculate_cost(self):
        pass


class EmergencyService(SmartService):
    def __init__(self, service_id, service_name, base_cost, priority_level, emergency_timer, resources):
        super().__init__(service_id, service_name, base_cost)

        self.__priority_level = 0
        self.__emergency_timer = 0
        self.__resources = 0

        self.priority_level = priority_level
        self.emergency_timer = emergency_timer
        self.resources = resources

    @property
    def priority_level(self):
        return self.__priority_level

    @priority_level.setter
    def priority_level(self, value):
        if value < 1 or value > 5:
            raise ValueError("Priority level must be between 1 and 5.")

        self.__priority_level = value

    @property
    def emergency_timer(self):
        return self.__emergency_timer

    @emergency_timer.setter
    def emergency_timer(self, value):
        if value < 0:
            raise ValueError("Emergency timer cannot be negative.")

        self.__emergency_timer = value

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        if value < 1:
            raise ValueError("Resources must be at least 1.")

        self.__resources = value

    def activate_service(self):
        return f"{self.service_name} activated with priority level {self.priority_level}."

    def generate_report(self):
        return (
            f"Emergency Report: {self.service_name} | "
            f"Timer: {self.emergency_timer} minutes | "
            f"Resources: {self.resources}"
        )

    def calculate_cost(self):
        return self.base_cost + (self.priority_level * 50) + (self.resources * 20)


class FireEmergencyService(EmergencyService):
    def __init__(self, service_id, service_name, base_cost, priority_level, emergency_timer, resources):
        super().__init__(
            service_id,
            service_name,
            base_cost,
            priority_level,
            emergency_timer,
            resources
        )