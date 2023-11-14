#!/usr/bin/env python
# coding: utf-8

# # Text Based Adventure game using python

# In[12]:


import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the treasure hidden deep within.")
    time.sleep(1)
    print("Be cautious, as your choices will determine your fate!")
    time.sleep(1)
    print("Let's begin!\n")

def forest_path():
    print("You come across a fork in the road.")
    time.sleep(1)
    print("Do you want to go left or right?")
    while True:
        choice = input("Enter 'left' or 'right': ").lower()
        if choice in ['left', 'right']:
            return choice
        else:
            print("Invalid input! Choose 'left' or 'right'.")

def encounter_wolves():
    print("You follow the left path...")
    time.sleep(1)
    print("You encounter a pack of wolves!")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1. Try to scare them away")
    print("2. Slowly back away")
    while True:
        wolf_choice = input("Enter your choice (1 or 2): ")
        if wolf_choice == "1":
            print("You scare the wolves away and continue on.")
            time.sleep(1)
            print("You reach a river blocking your path.")
            return 'river'
        elif wolf_choice == "2":
            print("You back away but they chase you!")
            time.sleep(1)
            print("Game Over!")
            return 'game_over'
        else:
            print("Invalid input! Choose 1 or 2.")

def shortcut():
    print("You take the right path...")
    time.sleep(1)
    print("You find a shortcut!")
    time.sleep(1)
    print("You reach the river.")
    return 'river'

def river_crossing():
    print("You reached the river.")
    time.sleep(1)
    print("There's a boat nearby.")
    time.sleep(1)
    print("Do you want to row across the river?")
    while True:
        choice = input("Enter 'yes' or 'no': ").lower()
        if choice == "yes":
            print("You row across successfully!")
            time.sleep(1)
            print("Congratulations! You found the treasure!")
            return 'win'
        elif choice == "no":
            print("You decide to swim...")
            time.sleep(1)
            print("The current is too strong!")
            time.sleep(1)
            print("Game Over!")
            return 'game_over'
        else:
            print("Invalid input! Choose 'yes' or 'no'.")

def game():
    introduction()
    path_choice = forest_path()

    if path_choice == 'left':
        result = encounter_wolves()
    else:
        result = shortcut()

    if result == 'river':
        result = river_crossing()

    if result == 'win':
        print("\nThank you for playing! You won!")
    elif result == 'game_over':
        print("\nThank you for playing! Game Over!")

# Start the game
game()


# In[ ]:





# In[ ]:




