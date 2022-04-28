class Employee:
    def __init__(self, first, last, pay, company):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.company = company

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def empdata(self):
        return 'First name: {}\n' \
               'Last name: {}\n' \
               'Pay: {}\n' \
               'Company: {}\n' \
               'Email: {}\n'.format(self.first, self.last, self.pay, self.company,self.email)
