line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]
map= [line1,line2,line3]

print("X marks the spot")
position= input("write the position number in 3d array to mark that position x (uppercase) = ")
letter= position[0]
abc= ["A","B","C"]
index_letter= abc.index(letter)
index_number= int(position[1])-1
map[index_number][index_letter] = "x"
print(f"{line1}\n{line2}\n{line3}")
