# list
# 0 to start the index from front and -1 to start the index from last

division_of_bd= ["dhaka","khulna","sylhet"]
print(division_of_bd[1])
print(division_of_bd[-1]) 

# to change any list item
division_of_bd[1]= "KHULNA"
print(division_of_bd)

# to add an item to the end of the list

division_of_bd.append("Barishal")
print(division_of_bd)

# toextend the list with multiple items

division_of_bd.extend(["Barishal","chittagong"])
print(division_of_bd)


# nested list ... a list inside a list
players = ["messi, neymar , kohli, sakib"]
footballplayers= ["messi, neymar"]
cricket_palyers= ["sakib, kohli"]
players = [footballplayers,cricket_palyers]
print(players)