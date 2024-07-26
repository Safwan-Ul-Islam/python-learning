# print particuler number


'''print("hell"[3])


# integer adding

print(12 + 12)
print(12.654 + 12_976)'''


#   float

3.1416


# boolean

True
False


# type check
'''a= 34
print(type(a))'''


# type check or adding a string with a integer by cahnging data type number to str
'''name = len(input("write your name?"))
new_name=str(name)
print("your name has" + new_name + "characters")'''


# int to str to float
'''a= 34
print("number is" + str(a) + str(22))
print(10 + a)
print(10 + float(a))'''

# exersice take a str number input and separate and add them

'''two_digit_number= input("two digit = ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))'''

# operators
'''print(3+5)
print(3-5)
print(3*5)
print(3/5)
print(3**5) #to the power  \\ PEMDAS =parenthesis mexponents multiplication divisioon add sub
print(int(3+5*6/2-4))'''

# BMI calculator
'''height= input("ENTER HEIGHT IN METERS=")
weight= input("ENTER WEIGHT IN KILOGRAMS=")
print(int(float(weight)/((float(height)**2))))'''

# alternative
'''height=input()
weight=input()
int_weight= int(weight)
float_height=float(height)
BMI= int_weight/(float_height**2)
print(int(BMI))'''

# round numbers to some decimal
'''print(round(3/2))
print(3//2)
print(round(2/3,3)) #to 3 decimal '''

# update
'''a=5
a+=1
print(a)'''

# mix types print f-string

'''score= 12
height=12
win=True
print(f"so he is {score}, {height},{win}")'''


# write aprogram that will take your age and show how many weeks u have left to  age 90
age =input("write your age in years = ")
age_weeks= int(age)*52.143
weeks_left= int(90*52.143)-float(age_weeks)
intweeks_left= int(weeks_left)
print(f"your age left in weeks is {intweeks_left}")
