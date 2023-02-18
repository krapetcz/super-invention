from dataclasses import dataclass


__last_id = 0


def get_next_id():
    global __last_id
    __last_id += 1
    return __last_id


@dataclass()
class Customer:

    id: int
    first_name: str
    last_name: str
    age: float = 0.0
    phone_number: str = ""

    def __str__(self):
        return f'ID: {self.id}\nLast Name: {self.last_name}\nFirst Name: {self.first_name}\nAddress: {self.age}\nPhone Number: {self.phone_number}'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, val: str):
        self.first_name, self.last_name = val.split(" ")


class CustomerBuilder:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = 0.0
        self.phone_number = ""

    def set_first_name(self, val):
        self.first_name = val
        return self

    def set_last_name(self, val):
        self.last_name = val
        return self

    def is_valid(self) -> bool:
        return self.first_name is not None and self.last_name is not None

    def build(self) -> Customer:
        if not self.is_valid():
            raise ValueError("Invalid data is set into builder")
        return Customer(get_next_id(), self.first_name, self.last_name, self.age, self.phone_number)




