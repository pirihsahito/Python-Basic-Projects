import random
user = int(input('Enter 0 for Snake, 1 for Water, 2 for Gun: '))
computer = random.randint(0, 2)

options = {0: "Sanke", 1: "Water", 2: "Gun"}

print(f"Computer chose: {options[computer]}")

if(user == computer):
    print("It's a DRAW!")

elif(user == 0):
    print(user)
    if(computer == 1):
        print('You Win!')
    else:
        print('You Lose!')

elif(user == 1):
    print(user)
    if(computer == 2):
        print('You Win!')
    else:
        print('You Lose!')

elif(user == 2):
    print(user)
    if(computer == 0):
        print('You Win!')
    else:
        print('You Lose!')