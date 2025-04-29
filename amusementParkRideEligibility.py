#1
#amusement park ride eligibility

height = int(input("Please Enter your Height : "))
age = int(input("Please Enter your age : "))

if age < 12 and height >= 120 :
    print("Can ride !")
elif age >= 12 or age < 18 and height >= 110 :
    print("Can ride !") 
elif age > 18:
    print("Can ride !") 
else:
    print("Not eligible for the ride")  
    

