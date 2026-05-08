import random


rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("""
      ooooooooooooooooooooooooooooooooooooo
      8                                .d88
      8  oooooooooooooooooooooooooooood8888
      8  8888888888888888888888888P"   8888    oooooooooooooooo
      8  8888888888888888888888P"      8888    8              8
      8  8888888888888888888P"         8888    8             d8
      8  8888888888888888P"            8888    8            d88
      8  8888888888888P"               8888    8           d888
      8  8888888888P"                  8888    8          d8888
      8  8888888P"                     8888    8         d88888
      8  8888P"                        8888    8        d888888
      8  8888oooooooooooooooooooooocgmm8888    8       d8888888
      8 .od88888888888888888888888888888888    8      d88888888
      8888888888888888888888888888888888888    8     d888888888
                                               8    d8888888888
         ooooooooooooooooooooooooooooooo       8   d88888888888
        d                       ...oood8b      8  d888888888888
       d              ...oood888888888888b     8 d8888888888888
      d     ...oood88888888888888888888888b    8d88888888888888
     dood8888888888888888888888888888888888b
""")
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. \n"))
if user_pick == 0:
    print(rock)
elif user_pick == 1:
    print(paper)
elif user_pick == 2:
    print(scissors)
else:
    print("You can only type 0, 1 or 2 to play.")

computer = [rock, paper, scissors]
computer_pick = random.choice(computer)
if 0 <= user_pick <= 2:
    print(f"Computer chose: \n {computer_pick}")


if user_pick == 0 and computer_pick == computer[0]:
    print("Draw game, try again!")
elif user_pick == 0 and computer_pick == computer[1]:
    print("You lose!")
elif user_pick == 0 and computer_pick == computer[2]:
    print("You win!")


if user_pick == 1 and computer_pick == computer[0]:
    print("You win!")
elif user_pick == 1 and computer_pick == computer[1]:
    print("Draw game, try again!")
elif user_pick == 1 and computer_pick == computer[2]:
    print("You lose!")


if user_pick == 2 and computer_pick == computer[0]:
    print("You lose!")
elif user_pick == 2 and computer_pick == computer[1]:
    print("You win!")
elif user_pick == 2 and computer_pick == computer[2]:
    print("Draw game, try again!")

