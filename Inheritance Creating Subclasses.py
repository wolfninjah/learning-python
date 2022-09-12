# Inheritance / Creating Subclasses

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first  # can be stet same as well
        self.last = last  # can be set same as well
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # it his is inheritance or a subclass
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # If you want to add something other than main class method
        super().__init__(first, last, pay)
        # Employee.__init__(self,first,last,pay)
        # It is same as the super method
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        # If you want to add something other than main class method
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Sapkota', 2000, 'Python')  # instance of the class
dev_2 = Developer('Coro', 'Kandel', 10000, 'Java')  # instance of the class
emp_1 = Employee('lo', 'la', 2000)

mgr_1 = Manager('sue', 'smith', 90000, [dev_1])
# print(dev_1.email)
# print(dev_1.prog_lang)

print(mgr_1.email)
mgr_1.add_emp(dev_2)  # added 2nd dev
mgr_1.remove_emp(dev_1)  # removed 1st developer
mgr_1.print_emp()

print(isinstance(mgr_1, Employee))  # finds out whether it is instance or no
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
# to check whether it is a sub class or no
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

'''
print(dev_1.pay)
dev_1.apply_raise()  # It will not have any change on salary of employee
emp_1.apply_raise()
print(dev_1.pay)
print(emp_1.pay)  # it will use raise amount of employee class
'''
