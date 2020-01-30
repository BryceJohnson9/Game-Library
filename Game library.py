#!/usr/bin/python3
#Bryce Johnson
#1-27-20    

import pickle
games = {1:["FPS", "Halo 3", "Bungee", "Microsoft", "Xbox 360", "2007", "10", "either", "30.00", "yes", "1/15/2008", "This game blows chunks"], 2:["Fighting", "Mortal Combat 11", "Netherealm Studios", "Warner Bros. Ineractive Entertainment", "Xbox One", "2019", "82%", "Both", "39.99", "No", "4/23/19", "You use combos to KO opponents"]}
''' Gives the user different options to pick games '''

def add_game():
    print ("Running add_game()")
    new_key = len(games) + 1
    new_entry = []
    valid = False
    while not valid:
        genre = input("What is the genre? ")
        new_entry.append(genre)
        title = input("What is the tile? ")
        new_entry.append(games)
        developer = input("What company developed the game? ")
        new_entry.append(developer)
        publisher = input("What company published the game? ")
        new_entry.append(publisher)
        system = input("What system is the game for? ")
        new_entry.append(system)
        release_date = input("When was the game released? ")
        new_entry.append(release_date)
        rating = input("What is the rating of the game? ")
        new_entry.append(rating)
        multi_single_both = input("Is the game single playe, multiplaer, or both? ")
        new_entry.append(multi_single_both)
        price = input("What is the price of the game? ")
        new_entry.append(price)
        completion = input("Did you complete the game? ")
        new_entry.append(completion)
        purchase_date = input("When is the date you purchased the game? ")
        new_entry.append(purchase_date)
        notes = input("What is the description of the game? ")
        new_entry.append(notes)
        answer = input("Is this correct?")
        if answer.lower() in ("yes" or "y"):
            valid = True
        
    games[new_key] = new_entry
    
def edit_game():
    print("Here is the Library: ")
    edit_entry = games[edit]
    for key in games.keys():
        print(key, "-", games[key][1])
    edit_key = int(input("Which game do you want to change?"))
    print("Current genre:", edit_entry[0])
    edit_entry[0] = input("New genre:")
    print("Current Title:" , edit_entry[1])
    edit_entry[1] = input("New Title:")
    print("Current developer:", edit_entry[2])
    edit_entry[2] = input("New developer:")
    print("Current publisher:", edit_entry[3])
    edit_entry[3] = input("New publisher:")
    print("Current system:", edit_entry[4])
    edit_entry[4] = input("New system:")
    print("Current release date:", edit_entry[5])
    edit_entry[5] = input("New release date:")
    print("Current rating:", edit_entry[6])
    edit_entry[6] = input("New rating:")
    print("Current Multiplayer:", edit_entry[7])
    edit_entry[7] = input("New multiplayer:")
    print("Current price:", edit_entry[8])
    edit_entry[8] = input("New price:")
    print("Current completion:", edit_entry[9])
    edit_entry[9] = input("New completion:")
    print("Current Purchase date:", edit_entry[10])
    edit_entry[10] = input("New purchase date:")
    print("Current notes:", edit_entry[11])
    edit_entry[11] = input("New notes:")
                   
def print_all():
    key_list = games.keys()
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher:", games[key][3])
        print("System: ", games[key][4])
        print("Release date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Multi/single/both: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beat it?: ", games[key][9])
        print("Purchase date: ", games[key][10])
        print("Notes: ", games[key][11])
        
def search_title():
    print ("Running search_title()")
    
def remove_game():
    print ("Running remove_game()")
    
def save_data():
    print ("Running save_data()")
    
def search():
    print ("Running search()")
    genre = input("What is the game you would like to search?")
    for key in games.keys():
        print(games[key][0])
        if genre in games[key][0]:
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Developer: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("System: ", games[key][4])
            print("Release date: ", games[key][5])
            print("Rating: ", games[key][6])
            print("Multi/single/both: ", games[key][7])
            print("Price: ", games[key][8])
            print("Beat it?: ", games[key][9])
            print("Purchase date: ", games[key][10])
            print("Notes: ", games[key][11])
    
def quit():
    print("Running quit()")
    
keep_going = True

data_file = open("game_lib.pickle", "rb")
games = pickle.load(data_file)
data_file.close()    

while keep_going:
    print("""
    Welcome to Game Library
    ---------------------------
    
    MAIN MENU
    1) Add game
    2) Edit game
    3) Print all games
    4) Search by title    
    5) Remove a game
    6) Save database
    7) Search
    
    Q) Quit
    
    """)
        
    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_all()       
    elif choice == "4":
        search_title(True)
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save_data()
    elif choice == "7":
        search()
    elif choice == "Q":
        quit()
        
    else:
        print("*** NOT A VALID CHOICE ***\n")    