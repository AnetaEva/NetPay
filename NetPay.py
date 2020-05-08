employee_name = input('Name of employee: ')

weekly_work_hours = float(input('How many hours did you work this week?: '))

pay_rate = float(input('What is your hourly rate?: $'))

#Net Pay without seeing the breakdown from gross pay and tax using the pay rate * work hours * (1 - 0.05)
net_pay = pay_rate * weekly_work_hours * (1 - 0.05)
print('Net Pay without breakdown.')
print('- Net Pay: $', format(net_pay, '.2f'), sep='')

#Net Pay with breakdown of gross pay, tax, and Net Pay using tax rate 0.05
tax_rate = 0.05

gross_pay = weekly_work_hours * pay_rate
tax = gross_pay * tax_rate
alternate_net_pay = gross_pay - tax

print('Net Pay with breakdown.')
print('- Gross Pay: $', format(gross_pay, '.2f'), sep='')
print('- Tax: $', format(tax, '.2f'), sep='')
print('- Alternate net pay: $', format(alternate_net_pay, '.2f'), sep='')
