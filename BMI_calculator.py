height=input("enter you height in meter = ")
weight=input("enter your weight in kilograms = ")
int_weight= int(weight)
float_height=float(height)
BMI= round(int_weight/(float_height**2),2)

if BMI<=18.5:
    print(f"your BMI is {BMI} you are under weight")
elif BMI<=25:
    print(f"your BMI is {BMI} you are normal weight")
elif BMI<=30:
    print(f"your BMI is {BMI} you are slightly overweight")
elif BMI<=35:
    print(f"your BMI is {BMI} you are obese")
else :
    print(f"your BMI is {BMI} you are clinically obese")