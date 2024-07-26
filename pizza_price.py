print("Thank you for chooseing python pizza deliveries")
size= input("select the sixe of the pizza 'L' 'M' 'S' = ")
if size=="L":
    lbill=25
    print(f"you have selected large size which will cost {lbill}$")
    add_pepparoni= input("do you want to add some peppearoni? Y or N = ")
    if add_pepparoni=="Y":
       bill= lbill + 3
    else: 
        bill = lbill
elif size=="M":
    mbill=20
    print(f"you have selected medium size which will cost {mbill}$")
    add_pepparoni= input("do you want to add some peppearoni? Y or N = ")
    if add_pepparoni=="Y":
       bill= mbill + 2
    else: 
        bill = mbill
elif size=="S":
    sbill=15
    print(f"you have selected small size which will cost {sbill}$")
    add_pepparoni= input("do you want to add some peppearoni? Y or N = ")
    if add_pepparoni=="Y":
      bill= sbill + 1
    else: 
        bill = sbill

add_cheese= input("do you want to add some cheese? Y or N = ")
if add_cheese=="Y":
    bill= bill + 1
    print(f"your final bill is {bill}")
else :
    print(f"your final bill is {bill}")
print("thank you very much for testing python pizzassss")