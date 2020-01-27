#!/usr/bin/python3
#Bryce Johnson
#1-27-20

import pickle

''' Gives the user different options to pick games '''

def add_game():
    print ("Running add_game()")
    #game = input("What is the game you would like to add?")
    #if game in base:
        #print(" GAME ALREADY EXISTS. ")
    #else:
def print_all():
    print ("Running print_all()")
    
def search_title():
    print ("Running search_title()")
    
def remove_game():
    print ("Running remove_game()")
    
def save_data():
    print ("Running save_data()")
    
def quit():
    print("Running quit()")
    
keep_going = True

while keep_going:
    print("""
    Welcome to Game Library
    ---------------------------
    
    MAIN MENU
    1) Add/Edit game
    2) Print all games
    3) Search by title    
    4) Remove a game
    5) Save database
    
    Q) Quit
    
    """)
        
    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search_title()       
    elif choice == "4":
        remove_game(True)
    elif choice == "5":
        save_data()
    elif choice == "Q":
        quit()
        
    else:
        print("*** NOT A VALID CHOICE ***\n")    