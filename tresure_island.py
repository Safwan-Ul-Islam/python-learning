print("welcome to tresure island. Your mission is to find the tresure")
left_right= input("You are at a cross road where do you want to go? 'left' or 'right'")
if left_right== "left":
    print("you come an llake .There is a island in thee middle of the lake.  ")
    wait_swim= input("type 'wait' to wait for a boat ortype 'swim' to swim across")
    if wait_swim== "wait":
        print("you arrived at the island unharmed")
        rbl= input("there is house with three doors. where do you want to go? 'red' or 'blue or 'yellow''")
        if rbl == "red":
           print("game over")
        elif rbl=="blue":
           print("game over")
        elif rbl=="yellow":
           print("you have found the tresure")
    else:
       print("game over")

else:
       print("game over")