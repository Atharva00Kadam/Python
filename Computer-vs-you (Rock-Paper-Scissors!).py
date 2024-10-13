
abc = input("Welcome to my rock paper scissors game! Type 0 for rock, 1 for paper, 2 for scissors!: ")

#rock
a = (""" Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
b = (""" Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
#Scissors
c = (""" Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if abc == "0":
    print("You chose rock\n"+ a)
if abc == "1":
    print("You chose paper\n"+ b)
if abc == "2":
    print("You chose scissors\n"+ c)


rock_paper_scissors = [a, b, c]
import random
hi = random.randint(0, 2)
print(rock_paper_scissors[hi])

if hi == abc:
    print("We tied! LOL")
elif hi == 0 and abc == 1:
    print("You lose")
elif hi == 0 and abc == 2:
    print("You win")
elif hi == 1 and abc == 2:
    print("You lose")
elif hi == 2 and abc == 0:
    print("You lose")
else:
    quit()
