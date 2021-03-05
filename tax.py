class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def income_tax(self, pay):
        pay = int(pay)
        allowance = 12500
        basic_rate = 50000
        high_rate = 150000

        basic_tax = 0.2
        high_tax = 0.4
        add_tax = 0.45

        def deduct_allowance(pay):
            if pay >= 125000:
                return 0
            else:
                pay -= 100000
                allowance -= pay / 2
                return allowance


        if pay <= allowance:
            return '{} {} will not pay any tax for the 2020/21 tax year'.format(self.first, self.last)

        elif pay > allowance and pay < basic_rate:
            b_taxable_pay = pay - allowance
            basic_payable = b_taxable_pay * basic_tax
            return '''
            {} {}'s Tax Summary:
            Income Tax Liability For Tax Year 2020/21: £{:0.2f}
            Your Take Home Pay: £{:0.2f}
                    '''.format(self.first, self.last, basic_payable, pay - basic_payable)

        elif pay > basic_rate and pay <= high_rate:
            if pay > 100000:
                allowance = deduct_allowance(pay)
                pay_reduced_allow = pay - allowance
                basic_payable = basic_rate * basic_tax
                high_payable = (pay_reduced_allow - basic_rate) * high_tax
                return '''
                {} {}'s Tax Summary
                Income Tax Liability For Tax Year 2020/21: £{:0.2f}
                Your Take Home Pay: £{:0.2f}
                        '''.format(self.first, self.last, high_payable + basic_payable, pay - (high_payable + basic_payable))

            else:
                pay_deduct = pay - allowance
                basic_payable = pay * basic_tax
                high_taxable_pay = pay - allowance - basic_rate
                high_payable = high_taxable_pay * high_tax
                return '''
                {} {}'s Tax Summary:
                Income Tax Liability For Tax Year 2020/21: £{:0.2f}
                Your Take Home Pay: £{:0.2f}
                        '''.format(self.first, self.last, high_payable + basic_payable, pay - (high_payable + basic_payable))

        elif pay > high_rate:
            adv_pay = pay - high_rate
            basic_payable = basic_rate * basic_tax
            high_payable = 100000 * high_tax
            adv_payable = (pay - high_rate) * add_tax
            return '''
            {} {}'s Tax Summary
            Income Tax Liability For Tax Year 2020/21: £{:0.2f}
            Your Take Home Pay: £{:0.2f}
                        '''.format(self.first, self.last, basic_payable + high_payable + adv_payable, pay - (basic_payable + high_payable + adv_payable))

# Access records or add another person to the database
print('Please Enter Your First Name, Last Name and Gross (Pre-tax) Income For The Year.')
first_name = input('First Name: ')
last_name = input('Last Name: ')
pay = input('Gross Income: ')

emp1 = Employee(first_name, last_name, pay)
print(Employee.income_tax(emp1, emp1.pay))
