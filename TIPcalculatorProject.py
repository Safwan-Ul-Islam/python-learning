# tip calculator

print("welcome to the tip calculator ")
bill= input("whaat was the total bill? ")
tip= input("what persentage tip would you like to give? 10, 12 or 15 ")
split= input("how many people to split tth bill")
total_bill= (float(bill)*int(tip)/100)+ float(bill)
split_bill=round(float(total_bill)/int(split),2)
print(f"Each perso should pay {split_bill}")


