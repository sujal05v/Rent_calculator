### Inputs we need from the user
#Total rent 
#total food ordered for snacking
#Electricity units spend
#charge per unit
#total persons living in room/flat

### Output
#total amount you've have to pay


rent = int(input("Enter your flat rent = "))
food = int(input("enter the food ordered for snacking ="))
electricity_spend = int(input("Enter the total of electricity spend ="))
charge_per_unit = int(input("Enter your charge per unit = "))
person = int(input("Enter the number of person= "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // person

print("Each person will pay = ", output)