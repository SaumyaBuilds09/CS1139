Weight=float(input("Enter your weight"))
Height=float(input("Enter your height"))
BMI=(Weight/(Height**2))
if BMI<=18.5:
    print("You are Underweight")
elif BMI>18.5 and BMI<=25:
    print("You have a normal weight")
elif BMI>25 and BMI<=30:
    print("You are slightly overweight")
elif BMI>30 and BMI<=35:
    print("you are obese")
else:
    print("You are clinically obese") 