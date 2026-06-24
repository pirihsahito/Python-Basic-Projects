# user:
#       S(0)    W(1)    G(2)
 
# S(0)    d    w    l

# W(1)   l    d    w

# G(2)   w    l    d

#  0 for Draw, 1 for Win, -1 for Lose

import random

rule = [
        [0, -1, 1],
        [1, 0, -1],
        [-1, 1, 0]
]

user = int(input('Enter 0 for Snake, 1 for Water, 2 for Gun: '))

print('You chose:', user)

computer = random.randint(0, 2)

options = {0: "Sanke", 1: "Water", 2: "Gun"}

print(f"Computer chose: {options[computer]}")

result = rule[computer][user]

if result == 0:
    print("It's Draw!")

if result == 1:
    print("You Win!")

if result == -1:
    print("You Lose!")