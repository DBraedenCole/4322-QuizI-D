'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv','r')
reader = csv.reader(infile,delimiter=',')
next(reader)


#create an empty dictionary
emp = {}

#use a loop to iterate through the csv file
for r in reader:
#check if the employee fits the search criteria

    if r[3] == "Marketing":
        if r[4] == "CSR":
            name = r[1]+" "+r[2]
            sal = float(r[5])
            emp[name] = sal

#iternate through the dictionary and print out the key and value as per printout

for n, s in emp.items():
    print(f"Manager Name: {n} Current Salary: ${s:,.2f}")

print()
print('=========================================')
print()

for i in emp.values():
    new = float(i)
    newsal = round(float(new)*1.1, 2)
    emp[name] = newsal

for name, sal in emp.items():
    print(f"Manager Name: {name} New Salary: ${sal:,.2f}")

          
        

        
    
