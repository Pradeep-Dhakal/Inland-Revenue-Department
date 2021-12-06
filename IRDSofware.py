print("\t\tIncome Tax Calculation System:\t")
print("\t\t\tLzimpat Kathmandu:")
print("__________________________________________________________")
print("\t\tWelcome to the Income Tax Calculation System:\t")
print("__________________________________________________________")

numberofPeople = 2
nameList = []
addressLIst = []
ageLIst = []
salaryList = []
stattusList = []
# choose=int(input("Enter 1 for insert details \n enter 2 for see details "))
for i in range(numberofPeople):
    name = input("enter your name: ")
    nameList.append(name)
    address = input("enter your address: [{i+1}]:")
    addressLIst.append(address)
    age = int(input("enter your age: [{i+1}]:"))
    ageLIst.append(age)
    monthly_salary = int(input("Enter your monthly income : [{i+1}]:"))
    salaryList.append(monthly_salary)
    maritual_status = input(
        "are you married or not? if yes enter M else n  [{i+1}]:")
    stattusList.append(maritual_status.upper())


def ifIndividual(monthlysalary):
    yearly_Salary = monthlysalary*12
    print("yearly salary : ", yearly_Salary)

    if yearly_Salary > 0 and yearly_Salary <= 400000:
        tax_amount = yearly_Salary*1/100
        print("Your tax amount is :", tax_amount)
    elif yearly_Salary > 400000 and yearly_Salary <= 500000:
        taxable_Income = yearly_Salary-400000
        tax_amount = taxable_Income*10/100+4000
        print("your tax amount= ", tax_amount)

    elif yearly_Salary > 500000 and yearly_Salary <= 700000:
        taxable_Income = yearly_Salary-500000
        tax_amount = (taxable_Income*20/100)+10000
        print("your tax amount= ", tax_amount)

    elif yearly_Salary > 700000 and yearly_Salary <= 2000000:
        taxable_Income = yearly_Salary-700000
        tax_amount = (taxable_Income*30/100)+50000
        print("your tax amount= ", tax_amount)
    else:
        taxable_Income = yearly_Salary-2000000
        tax_amount = (taxable_Income*36/100)+440000
        print("your tax amount= ", tax_amount)
    # ifIndividual(monthly_salary)


def ifMarried(monthlysalary):
    yearly_Salary = monthlysalary*12
    print("yearly salary : ", yearly_Salary)

    if yearly_Salary > 0 and yearly_Salary <= 450000:
        tax_amount = yearly_Salary*1/100
        print("Your tax amount is :", tax_amount)
    elif yearly_Salary > 450000 and yearly_Salary <= 550000:
        taxable_Income = monthly_salary-450000
        tax_amount = taxable_Income*10/100+4500
        print("your tax amount= ", tax_amount)

    elif yearly_Salary > 550000 and yearly_Salary <= 750000:
        taxable_Income = yearly_Salary-550000
        tax_amount = (taxable_Income*20/100)+10000
        print("your tax amount= ", tax_amount)

    elif yearly_Salary > 750000 and yearly_Salary <= 2000000:
        taxable_Income = yearly_Salary-750000
        tax_amount = (taxable_Income*30/100)+50000
        print("your tax amount= ", tax_amount)

    else:
        taxable_Income = yearly_Salary-2000000
        tax_amount = (taxable_Income*36/100)+425000
        print("your tax amount= ", tax_amount)

    # ifMarried(monthly_salary)
for i in range(numberofPeople):
    if(stattusList[i].lower() == 'n'):
        ifIndividual(salaryList[i])
    elif(stattusList[i].lower() == 'y'):
        ifMarried(salaryList[i])
    else:
        pass
