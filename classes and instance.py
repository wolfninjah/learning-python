# class and instance

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.fname = first  # can be stet same as well
        self.lname = last  # can be set same as well
        self.pay = pay
        self.email = 'first' + 'last' + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):  # alternative for 1st method by using class
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)  # It will print 0 because there are no employees currently as employees are added below
# this line

emp_1 = Employee('Corey', 'Sapkota', 2000)  # instance of the class
emp_2 = Employee('Coro', 'Kandel', 10000)  # instance of the class

# both are unique instances
''''''''''
print(emp_1)
print(emp_2)
emp_1.first = 'Corey'
emp_1.last = 'Sapkota'
emp_1.email = "CoreySapkota@gmail.com"
emp_1.pay = 2000

emp_2.first = 'Coro'
emp_2.last = 'Kandel'
emp_2.email = "CoroKandel@gmail.com"
emp_2.pay = 10000
'''''''''''
# alternative is available upwards


print(emp_1.email)
print(emp_2.email)
# 1st method but a bit long
print('{} {}'.format(emp_1.fname, emp_1.lname))
# 2nd method by using class
print(emp_2.fullname())
print(emp_1.fullname())

'''
the components inside () are called argument
'''

# CLASS VARIABLES

print(emp_1.raise_amount)  # this can be accessed from class as well as the instance
print(Employee.raise_amount)  # this can be accessed from class as well as the instance
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)

'''
if you want to do for class do with the name of the class Employee in here
and if you want to do for instance do it with the name of instance only emp_1 in here
'''

print(Employee.num_of_emps)  # it was printed 2 because the line is below the instanciation ...
