from employee import Employee


class Company:
    def __init__(self, name, country, sector):
        self.name = name
        self.country = country
        self.sector = sector

    def compdata(self):
        return '[Company data] \n' \
               'Name: {}\n' \
               'Country: {}\n' \
               'Sector: {}\n'.format(self.name, self.country, self.sector)

    def emp_comp(self, company, emp):
        if company == emp:
            return '{} works on {}'.format(emp, company)
        else:
            return 'Error'


emp_1 = Employee('André', 'Silva', 3000, '3M')
emps = [emp_1]
print('Name: ' + emps[0].fullname() + '\n' + emps[0].empdata())

comp_1 = Company('GE', 'Usa', 'Production')
comps = [comp_1]
print(comps[0].compdata())

Company.emp_comp(emp_1.company, comp_1.name)