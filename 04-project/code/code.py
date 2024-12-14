import random

rock = '''

    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
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

game = [rock , scissor , paper]

ans = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
print(f"you choose: {ans}")

if(ans > 2):
    print("Enter Valid Input")
    exit()

print(game[ans])

computer = random.randint(0,2)
print(f"Computer Chooses {computer}:\n")
print(game[computer])

if(ans == computer):
    print("Tie!")
else:
    if (ans == 0 and computer == 2) or (ans == 1 and computer == 0) or (ans == 2 and computer == 1): 
        print("You lose!")
    else: 
        print("You win!") 
        



