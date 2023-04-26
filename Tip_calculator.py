#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_percentage = 1+ tip/100
# print(tip_percentage)
no_of_people = int(input("How many peoiple to split the bill? "))

bill_per_person = round((total_bill/no_of_people)*tip_percentage,2)
print(f"Each person should pay: ${bill_per_person:.2f}")