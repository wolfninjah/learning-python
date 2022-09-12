# class and instance

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first  # can be stet same as well
        self.last = last  # can be set same as well
        self.pay = pay
        self.email = first + last + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Sapkota', 2000)  # instance of the class
emp_2 = Employee('Coro', 'Kandel', 10000)  # instance of the class
'''
Employee.set_raise_amt(1.05)  # All will riase because we ran this set raise amount method and it is class method

print(emp_1.raise_amt)  # this can be accessed from class as well as the instance
print(Employee.raise_amt)  # this can be accessed from class as well as the instance
print(emp_2.raise_amt)

emp_str_1 = 'JOhn-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)  # class method as alternative structure

print(new_emp_1.email)
print(new_emp_1.pay)
'''

import datetime

my_date = datetime.date(2016, 7, 10)  # because the 10th is sunday in this day
my_date = datetime.date(2016, 7, 11)  # becuase is 11th of 7 is monday

print(Employee.is_workday(my_date))
