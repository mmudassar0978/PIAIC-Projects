# -*- coding: utf-8 -*-
"""Project4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iEYGKrtyQQi75IiAU9WvgwL46zOkbwGA
"""

# Project 4: Rock, paper, scissors Python Project

import random
import time

while(True):
  User_input = int(input("Enter 1,2,3 for Rock, Paper and Scissors respectively : "))
  if (User_input != 1 and User_input != 2 and User_input != 3):
    raise ValueError("You enter invalid number!")
  else:
    if User_input == 1:
      u_select = "Rock"
    elif User_input == 2:
      u_select = "Paper"
    elif User_input == 3:
      u_select = "Scissors"
    print(f"You selected the {u_select}!")


  Computer_input = random.randint(1, 3)
  if Computer_input == 1:
    c_select = "Rock"
  elif Computer_input == 2:
    c_select = "Paper"
  elif Computer_input == 3:
    c_select = "Scissors"
  print(f"Computer selected the {c_select}!")


  if u_select == c_select:
    print("You and computer selected same options you the Game Draw!")
  elif u_select == "Rock" and c_select == "Scissors":
    print("You win the game!")
  elif u_select == "Paper" and c_select == "Rock":
    print("You win the game!")
  elif u_select == "Scissors" and c_select == "Paper":
    print("You win the game!")
  else:
    print("Computer wins the game!")

  ask = input("Are you want to play game again? Kindly enter yes/no : ")
  if ask.lower() == "yes":
    continue
  else:
    break