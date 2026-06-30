from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, transport_id, name, base_fare, emission_rate):
        self.__transport_id = transport_id
        self.__name = name
        self.__base_fare = 0
        self.__emission_rate = 0

        self.base_fare = base_fare
        self.emission_rate = emission_rate

    @property
    def transport_id(self):
        return self.__transport_id

    @property
    def name(self):
        return self.__name

    @property
    def base_fare(self):
        return self.__base_fare

    @base_fare.setter
    def base_fare(self, value):
        if value < 0:
            raise ValueError("Base fare cannot be negative.")

        self.__base_fare = value

    @property
    def emission_rate(self):
        return self.__emission_rate

    @emission_rate.setter
    def emission_rate(self, value):
        if value < 0:
            raise ValueError("Emission rate cannot be negative.")

        self.__emission_rate = value

    @abstractmethod
    def calculate_fare(self, distance):
        pass

    def calculate_emissions(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        return distance * self.emission_rate


class Bus(Transport):
    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        return self.base_fare + distance * 0.60


class Taxi(Transport):
    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        surge_price = 1.25
        return (self.base_fare + distance * 1.80) * surge_price


class Metro(Transport):
    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        return self.base_fare + distance * 0.45


class Train(Transport):
    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        return self.base_fare + distance * 0.70


class ElectricScooter(Transport):
    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        return self.base_fare + distance * 0.30


class AirTaxi(Transport):
    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        surge_price = 1.50
        return (self.base_fare + distance * 5.00) * surge_price