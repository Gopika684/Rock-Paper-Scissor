rent=int(input("Enter your hostel/flat rent ="))
food=int(input("Enter the amt of food ordered = "))
electricity=int(input("Enter the total of electricity spent ="))
charge_per_unit=int(input("Enter the charge per unit ="))
persons=int(input("Enter the no of persons living in room ="))
total_bill=electricity*charge_per_unit
output=(food + rent + total_bill)//persons
print("Each person will pay =",output)