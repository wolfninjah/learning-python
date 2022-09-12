# class and instance

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):  # called when we create instance forex emp1 here
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):  # to find length of fullname of employee
        return len(self.fullname())


emp_1 = Employee('Corey', 'Sapkota', 2000)  # instance of the class
emp_2 = Employee('Coro', 'Kandel', 10000)  # instance of the class

print(len(emp_1)) # to find length of full name of employee

print('test'.__len__())

# print(emp_1+emp_2)  to add salary of 2 employees


# print(emp_1)  # We get a location or object code

# print(repr(emp_1))  # used while debugging
# print(str(emp_1) ) # readable representation of the object


# print(emp_1.__repr__()) # same as up
# print(emp_1.__str__())  # same as up

'''
print(1 + 2)

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))
'''
