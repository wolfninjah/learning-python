class Employee:

    def __init__(self, first, last):
        self.first = first  # can be stet same as well
        self.last = last  # can be set same as well

    # first name changed but in email it is still john
    @property  # this will help to change attribute and help without changing whole code to prantheses
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # for deleting name
    def fullname(self):
        print('Delete Name!!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')


emp_1.fullname = 'Corey Schafer'

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

