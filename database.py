# import mysql.connector
import pymysql
num_people = 2
name = []
address = []
salary = []
for i in range(num_people):
    name.append(input(f"Enter name [{i+1}] "))
    address.append(input(f"address [{i+1}] "))
    salary.append(int(input(f"salary [{i+1}] ")))
mydatabase = pymysql.connect(
    host="localhost", user="root", passwd="", database="tax")


cursor = mydatabase.cursor()
for i in range(num_people):
   
    query='''insert into newdata (name, address,salary) values(%s,%s,%s,)'''
    record=({name},{address},{salary})

    cursor.execute(query,record)
       

    print("Successfully inserted ")

    mydatabase.commit()
    mydatabase.close()
