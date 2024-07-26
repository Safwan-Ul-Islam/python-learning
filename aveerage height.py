
student_heights= input("input the heights of the students = ").split() #takin input in a lsit
for n in range (0,len(student_heights)): #range indicates range
     student_heights[n]= int(student_heights[n])
total_height=0
for height in student_heights:
    total_height= total_height+height

    
    print(f"total height {total_height}")
av=total_height/len(student_heights)
print(f"avrage height{av}") 
 