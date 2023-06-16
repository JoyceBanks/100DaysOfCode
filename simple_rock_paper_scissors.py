import random

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
rps_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))

if rps_user == 0:
  print(rock)
  user_choice = 'r'
elif rps_user == 1:
  print(paper)
  user_choice = 'p'
else:
  print(scissors)
  user_choice = 's'
 
rps_list = [rock, paper, scissors]
rps_computer = random.choice(rps_list)
print(f"Computer chose: {rps_computer}")

if user_choice == 'r' and rps_computer == scissors:
  print("You win")
elif user_choice == 'r' and rps_computer == rock:
    print("It's a Tie")
elif user_choice == 's' and rps_computer == paper:
  print("You win")
elif user_choice == 's' and rps_computer == scissors:
    print("It's a Tie")
elif user_choice == 'p' and rps_computer == rock:
  print("You win")
elif user_choice == 'p' and rps_computer == paper:
    print("It's a Tie")
else:
  print("You lose")
