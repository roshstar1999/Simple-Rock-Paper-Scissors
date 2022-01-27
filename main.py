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
x=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

ar=[rock,paper,scissors]
print(ar[x])
import random
pc=random.choice(ar)
print(pc)
if x==0:
  if pc==rock:
    j=0
    print('Its a Tie!')
  elif pc== paper:
    j=-1
  else:
    j=1
elif x==1:
  if pc==paper:
    j=0
    
  elif pc== scissors:
    j=-1
  else:
    j=1
else:
  if pc==scissors:
    j=0
    print('Its a Tie!')
  elif pc== rock:
    j=-1
  else:
    j=1

if j==0:
  print('Its a Tie!')
elif j==-1:
  print('Maybe Next time :|')
else:
  print('You win Yeeeeaaaaaah!!  :)')

  

