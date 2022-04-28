class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def alldata(self):
        return 'First name: {}\n' \
               'Last name: {}\n' \
               'Pay: {}\n' \
               'Email: {}\n'.format(self.first, self.last, self.pay, self.email)


emp_1 = Employee('André', 'Marques', 4000)
print('Name: ' + emp_1.fullname())
print(emp_1.alldata())
