import random

symbol= ["rock" , "paper" , "scissor"]
lenth=len(symbol)
random_choice=random.randint(0,lenth-1)
com_choosee=symbol[random_choice]
com_choose=str(com_choosee)


user_input= (input("write rock,  paper , scissor = "))
if user_input=="rock":
    print("you choose ROCK")
    print(f"computer choose {com_choose}")
    if com_choose=="rock":
        print("you draw")
    elif com_choose=="scissor":
        print("you win")
    else:
        print("you losssse")


elif user_input== "paper":
    print("you choose paper")
    print(f"computer choose {com_choose}")
    if com_choose=="paper":
      print("you draw")
    elif com_choose=="rock":
      print("you win")
    else:
      print("you lose")
else:
    print("you choose scissor")
    print(f"computer choose {com_choose}")
    if com_choose=="scissor":
        print("you draw")
    elif com_choose=="paper":
        print("you win")
    else:
        print("you lose")