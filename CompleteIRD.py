
from datetime import date
from os import name
from typing import final

import mysqlx


today = date.today()

name = []
address = []
age = []
Phone = []
gender = []
gender = []
maritial_status = []
insuranceDetails = []
disabilityCheck = []
diplomatJob = []
salary = []
total_tax_amount = []
allowances = []
grandTotalFinalTax = []


class taxCalculation():
    def __init__(self, salary,  maritial_status, diplomat, disability, gender, name, address, age, Phone, insuranceDetails, allowances, grandTotalFinalTax):
        self.salary = salary
        self.maritial_status = maritial_status
        self.diplomat = diplomat
        self.disability = disability
        self.gender = gender
        self.name = name
        self.address = address
        self.phone = Phone
        self.age = age
        self.insurancedetails = insuranceDetails
        self.allowances = allowances
        self.grandTotalFinalTax = grandTotalFinalTax

    @staticmethod
    def StaticInformation():
        print(
            '''
                            Income Tax Calculation System
                            --->>Lazimpat<---->Kathmandu<<--
    ____________________________________________________________________________________
        '''
        )
        print("आन्तरिक राजस्व विभाग  \t\t\t\t\t\t Date:", today)
        print("__________________________________________________________")

    @classmethod
    def EmployeeInformation(self, Num_of_people):
        for i in range(Num_of_people):
            name.append(input(f"[{i+1}] Enter your name : "))
            address.append(input(f"[{i+1}] Enter your address : "))
            Phone.append(input(f"[{i+1}] Enter your phone number : "))
            age.append(int(input(f"[{i+1}] Enter your age : ")))
            gender.append(input(f"[{i+1}] enter your gender : M : F: "))
            maritial_status.append(
                input(f"[{i+1}] are you married or not? if yes enter M else n : "))
            insuranceDetails.append(input(
                f"[{i+1}] Enter insurance details done or not if yes type [Y] else type [N] : "))
            disabilityCheck.append(input(
                f"[{i+1}] Do You have any Disabilities ? if yes type [y] else type [N] : "))
            diplomatJob.append(input(
                f"[{i+1}] DO you have diplomat job? if yes type [Y] else type [N] : "))
            if diplomatJob[i].lower() == "y":
                allowances.append(
                    int(input(f"[{i+1} Enter your foreign Allowances: ")))
            else:
                allowances.insert(i, 0)

            salary.append(int(input(f"[{i+1}] Enter your monthly salary : ")))
            print("________________________________________________________")

        return salary,  maritial_status, diplomatJob, disabilityCheck, gender, name, address, Phone, insuranceDetails, allowances

    def CalculateIndividual(self, monthlysalary):
        yearly_Salary = monthlysalary*12
        print("yearly salary : ", yearly_Salary)

        if yearly_Salary > 0 and yearly_Salary <= 400000:
            tax_amount = yearly_Salary*1/100

            return tax_amount

        elif yearly_Salary > 400000 and yearly_Salary <= 500000:
            taxable_Income = yearly_Salary-400000
            tax_amount = taxable_Income*10/100+4000

            return tax_amount

        elif yearly_Salary > 500000 and yearly_Salary <= 700000:

            taxable_Income = yearly_Salary-500000
            tax_amount = (taxable_Income*20/200)+10000

            return tax_amount

        elif yearly_Salary > 700000 and yearly_Salary <= 2000000:
            taxable_Income = yearly_Salary-700000
            tax_amount = (taxable_Income*30/100)+50000

            return tax_amount
        else:
            taxable_Income = yearly_Salary-2000000
            tax_amount = (taxable_Income*36/100)+440000

            return tax_amount

    def CalculateCouple(self, monthlysalary):

        yearly_Salary = monthlysalary*12
        print("yearly salary : ", yearly_Salary)

        if yearly_Salary > 0 and yearly_Salary <= 450000:
            tax_amount = yearly_Salary*1/100

            return tax_amount
        elif yearly_Salary > 450000 and yearly_Salary <= 550000:
            taxable_Income = yearly_Salary-450000
            tax_amount = taxable_Income*10/100+4500

            return tax_amount

        elif yearly_Salary > 550000 and yearly_Salary <= 750000:
            taxable_Income = yearly_Salary-550000
            tax_amount = (taxable_Income*20/100)+10000

            return tax_amount
        elif yearly_Salary > 750000 and yearly_Salary <= 2000000:
            taxable_Income = yearly_Salary-750000
            tax_amount = (taxable_Income*30/100)+50000

            return tax_amount

        else:
            taxable_Income = yearly_Salary-2000000
            tax_amount = (taxable_Income*36/100)+425000
            print("your tax amount= ", tax_amount)
            return tax_amount

    def setdisability(self, disbility):
        self.disability = disbility

    def getdisability(self):
        return self.disability

    def setdiplomat(self, diplomat):
        self.diplomat = diplomat

    def getdiplomat(self):
        return self.diplomat

    def setwomenEmployment(self, gender):
        self.gender = gender

    def getwomenEmployment(self):
        return self.gender

    def calculate_tax(self, numberofCustomer):
        final_tax = []

        for i in range(numberofCustomer):

            final_taxable_income = 0
            taxable_allowance = self.allowances[i]*0.25
            total_diplmat_taxable_income = taxable_allowance+self.salary[i]
            disability_salary = self.salary[i]/2
            if self.maritial_status[i].lower() == "y":
                if self.disability[i].lower() == "y" and self.diplomat[i].lower() == "y":

                    total_tax = self.CalculateCouple(
                        total_diplmat_taxable_income+disability_salary)
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)

                elif self.diplomat[i].lower() == "y":
                    total_tax = self.CalculateCouple(
                        total_diplmat_taxable_income)
                    final_tax.append(total_tax)
                elif self.disability[i].lower() == "y":
                    total_tax = self.CalculateCouple(disability_salary)
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)
                else:
                    total_tax = self.CalculateCouple(self.salary[i])
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)
            else:
                if self.disability[i].lower() == "y" and self.diplomat[i].lower() == "y":

                    total_tax = self.CalculateIndividual(
                        total_diplmat_taxable_income+disability_salary)
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)
                elif self.diplomat[i].lower() == "y":
                    total_tax = self.CalculateIndividual(
                        total_diplmat_taxable_income)
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)
                elif self.disability[i].lower() == "y":
                    total_tax = self.CalculateIndividual(disability_salary)
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)
                else:
                    total_tax = self.CalculateIndividual(self.salary[i])
                    final_tax.append(total_tax)
                    print("total tax: ", total_tax)

        print("method executed :")
        for i in range(numberofCustomer):
            if self.gender[i].lower() == "f":
                return_tax = final_tax[i]*0.1
                final = total_tax-return_tax
                self.grandTotalFinalTax.append(final)

            else:
                self.grandTotalFinalTax = list(final_tax)

    def display_information(self, number):
        for i in range(number):
            print(f''' 
            *****Here m resefrs to married y referse to yes and n refers to no********
                Name [{i+1}]: {self.name[i]} 
                Address of [{self.name[i]}]: {self.address[i]} 
                Contact of [{self.name[i]}]: {self.phone[i]}
                Maritial Status of [{self.name[i]}]: {self.maritial_status[i]}
                Insurance Detils of [{self.name[i]}]: {self.insurancedetails[i]}
                Diplomatic Status of [{self.name[i]}]:{self.diplomat[i]}
                Foreign Allowanceof [{self.name[i]}]: {self.allowances[i]}
                Monthly Salary of [{self.name[i]}]: {self.salary[i]}
                Total_Tax of [{self.name[i]}]: {self.grandTotalFinalTax[i]} 
                _______________________________

                ''')
        return grandTotalFinalTax



    def SaveData(self, number):
        data = open("data.txt", "w")
        for i in range(number):

            data.write(f''' 
            *****Here m resefrs to married y referse to yes and n refers to no********
                Name [{i+1}]: {self.name[i]} 
                Address of [{self.name[i]}]: {self.address[i]} 
                Contact of [{self.name[i]}]: {self.phone[i]}
                Maritial Status of [{self.name[i]}]: {self.maritial_status[i]}
                Insurance Detils of [{self.name[i]}]: {self.insurancedetails[i]}
                Diplomatic Status of [{self.name[i]}]:{self.diplomat[i]}
                Foreign Allowanceof [{self.name[i]}]: {self.allowances[i]}
                Monthly Salary of [{self.name[i]}]: {self.salary[i]}
                Total_Tax of [{self.name[i]}]: {self.grandTotalFinalTax[i]} 
                _______________________________

                ''')

    def saveintodatabase(self):
        for i in range(2):
            import mysql.connector
            mydatabase = mysql.connector.connect(host="localhost", user="root", passwd="", database="tax")
            cursor = mydatabase.cursor()
            query="insert into taxtable(name, address,contact,maritial_status,insurance_detail,diplomat_ststus,monthly_salary,foreign_allowance,total_tax) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(self.name[i],self.address[i],self.phone[i],self.maritial_status[i],self.insurancedetails[i],self.diplomat[i],self.salary[i],self.allowances[i],self.grandTotalFinalTax[i])
            cursor.execute(query,values)
            mydatabase.commit()
            mydatabase.close()


def main():
    taxCalculation.StaticInformation()
    Num_of_people = int(input("Number Of Customers: "))
    salary, maritial_status, diplomatJob, disabilityCheck, gender, name, address, Phone, insuranceDetails, allowances = taxCalculation.EmployeeInformation(Num_of_people)

    tcal = taxCalculation(salary, maritial_status, diplomatJob, disabilityCheck,
                          gender, name, address, age, Phone, insuranceDetails, allowances, grandTotalFinalTax)

    tcal.calculate_tax(Num_of_people)
    tcal.display_information(Num_of_people)
    tcal.SaveData(Num_of_people)
    tcal.saveintodatabase()


if __name__ == "__main__":
    main()
