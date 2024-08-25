import random
x='''
                _                                         _                        
               | |                                       (_)                       
 _ __ ___   ___| | ___ __   __ _ _ __   ___ _ __ ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ / '_ \ / _` | '_ \ / _ \ '__/ __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <| |_) | (_| | |_) |  __/ |  \__ \ (__| \__ \__ \ (_) | |  \__ \
|_|  \___/ \___|_|\_\ .__/ \__,_| .__/ \___|_|  |___/\___|_|___/___/\___/|_|  |___/
                    | |         | |                                                
                    |_|         |_|                                                       
'''                                            
print(x)
print("Welcome to the Game Rock Paper Scissors!!Let's Play and decidewho's the best!!!")
print("Ready!Lets begin")
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
op=[rock,paper,scissors]
user_input=int(input("Enter 0 for rock ,1 for paper,and 2 for scissors"))
user_choice=op[user_input]
print("You chose \n",user_choice)
machineChoice=random.choice(op)
print("Machine chose\n",machineChoice)
if(machineChoice==user_choice):
    print("Oh shit!!It's a draw")
elif(machineChoice==rock):
    if(user_choice==paper):
        print("Yeah!!You won the game!!Congratulations")
    else:
        print("oh...Sorry...you lost the game!!Try Again")
elif(machineChoice==paper):
    if(user_choice==scissors):
        print("Yeah!!You won the game!!Congratulations")
    else:
        print("oh...Sorry...you lost the game!!Try Again")
elif(machineChoice==scissors):
    if(user_choice==rock):
        print("Yeah!!You won the game!!Congratulations")
    else:
        print("oh...Sorry...you lost the game!!Try Again")   