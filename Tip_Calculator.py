print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent= tip/100  # calculating the tip percentage 

total_tip_amount= bill * tip_percent # getting the tip amount 

total_bill = bill + total_tip_amount #adding it to the bill

bill_per_person = total_bill/people # Dividing the total bill 

final_amount = round(bill_per_person,2) #rounding Off the amount by 2 decimal places 

print(f"Each Person will pay :${final_amount}")#Displaying the amount that should be paid per person 