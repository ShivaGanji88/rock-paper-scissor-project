#this is rock paper scissors project

#importing random

import random

#rock paper scissors emojis
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#taking individuals as a list
adding_together = [rock, paper, scissors]


users_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. \n"))

if (users_choice >= 3) or (users_choice < 0):
    print("entered wrong number")  

else:
    print("User choose: ")
    print(adding_together[users_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Choose: ")
    print(adding_together[computer_choice])

    if users_choice == computer_choice:
        print("it's Draw")

    elif computer_choice > users_choice:
        print("Computer Wins")

    elif users_choice == 0 and computer_choice == 2:
        print("You Win")

    elif computer_choice == 0 and users_choice == 2:
        print("Computer wins")       

    elif users_choice > computer_choice:
        print("You win")
    