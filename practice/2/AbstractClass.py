# abstract class contains abstract methods. we have signature for it but no implementations
# we have to import abstract base class everytime to create an abstract class.
from abc import ABC, abstractmethod
from math import pi


class AbstractClassName(ABC):
    # abstract methods must be annotated with @abstractmethod
    @abstractmethod
    def abstract_method_name(self):
        pass


# we have to provide the implementation in the child class and then create object for child class or else
# it will become abstract class.

class child(AbstractClassName):
    def abstract_method_name(self):
        return "Hello"

    def method_a(self):
        return "Hello"


object = child()
print(object.abstract_method_name())


# abstract_ref = AbstractClassName()

class Iphone(ABC):

    @abstractmethod
    def camera(self):
        pass

    @abstractmethod
    def speaker(self):
        pass

    @abstractmethod
    def OS(self):
        pass

    @abstractmethod
    def chipset(self):
        pass


class IphoneModel1(Iphone):

    def camera(self):
        return "Sony x.1"

    def speaker(self):
        return "speaker 1"

    def OS(self):
        return "Mac version1"

    def chipset(self):
        return "snap dragon x.01"


iphone1 = IphoneModel1()


class IphoneModel2(Iphone):

    def camera(self):
        return "Sony x.2"

    def speaker(self):
        return "Speaker 2"

    def OS(self):
        return "Mac version 3"

    def chipset(self):
        return "snap dragon x.04"

    def security(self):
        return "Security Protocal"


# abstract class can contain both abstract and normal methods, but you can't instantiate a class once it is declared as abstract.
class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + self.last_name

    @abstractmethod
    def get_salary(self):
        pass  # there is no implementation


class FulltimeEmployee(Employee):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:

    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")


payroll = Payroll()

payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

payroll.print()




