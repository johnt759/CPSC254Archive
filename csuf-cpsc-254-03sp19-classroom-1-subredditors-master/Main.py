# -*- coding: utf-8 -*-

from scraping import SubtoCSV
from subComparer import SubCompare, SubStats

menu = {}
menu['1']="Compare Two subreddits" 
menu['2']="Get Single-Subreddit Stats"
menu['3']="Update Existing Sub Data"
menu['4']="Exit"

while True: 

    for entry in menu: 
        print(entry, menu[entry])
    
    selection = input("Please Select:")
    if selection == '1':
        print()
        print("Enter two Subreddits to compare")
        sub1 = input()
        sub2 = input()
        try:
            openfile = open(sub1 + '.csv', 'r')
            openfile.close()
        except FileNotFoundError:
            SubtoCSV(sub1)
        try:
            openfile = open(sub2 + '.csv', 'r')
            openfile.close()
        except FileNotFoundError:
            SubtoCSV(sub2)
        SubCompare(sub1, sub2)
        
    elif selection == '2':
        print()
        print("Enter the Subreddit")
        sub1 = input()
        try:
            openfile = open(sub1 + '.csv', 'r')
            openfile.close()
        except FileNotFoundError:
            SubtoCSV(sub1)
        SubStats(sub1)
    elif selection == '3':
        print()
        sub1 = input("Enter the Subreddit to Update")
        SubtoCSV(sub1)
        print()
        print("Complete")
    elif selection == '4':
        break
    else:
        print('Invalid Entry')
        
        
    
