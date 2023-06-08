# -*- coding: utf-8 -*-

import csv

def SubCompare (sub1, sub2):
    
    sub1Dict = {} #will be populated with the contents of the csv of sub1
    sub2Dict = {} #will be populated with the contents of the csv of sub2
    diffs = {}
    
    sub1Total = 0
    sub2Total = 0
    
    with open(sub1 + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            try: 
                if row:
                    if (int(row[1]) >= 5):
                        sub1Dict[row[0]] = int(row[1])
                        sub1Total += int(row[1])
            except UnicodeDecodeError:
                pass
    
    with open(sub2 + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            try:
               if row:
                    if (int(row[1]) >= 5):
                        sub2Dict[row[0]] = int(row[1])
                        sub2Total += int(row[1])
            except UnicodeDecodeError:
                pass
    
    for key in sub1Dict:
        if (key in sub2Dict and sub1Dict[key] >= 5):
            diffs[key] = ((sub2Dict[key] / sub2Total) / (sub1Dict[key] / sub1Total))
        elif (sub1Dict[key] >= 5):
            diffs[key] = 1/sub1Dict[key]
    
    for key in sub2Dict:
        if (key in sub1Dict and sub2Dict[key] >= 5):
            diffs[key] = ((sub2Dict[key] / sub2Total) / (sub1Dict[key] / sub1Total))  
        elif (sub2Dict[key] >= 5): 
            diffs[key] = sub2Dict[key]
            
    print("Here are the top ten unique words to /r/" + sub2)
    print(sorted(diffs.items(), key=lambda item: item[1], reverse = True)[:10])
    print()
    print("Here are the top ten unique words to /r/" + sub1)
    
    for key in diffs:
        diffs[key] = 1/diffs[key]
    print(sorted(diffs.items(), key=lambda item: item[1], reverse = True)[:10])
    print()
        
    #method to populate the dictionary, while counting the words used in both
#alternate method to be used if we only want to find one sub's data
def SubStats (sub1):
    
    sub1Dict = {} #will be populated with the contents of the csv of sub1
    baseDict = {} #will be populated with the contents of the csv of sub2
    diffs = {}

    sub1Total = 0
    baseTotal = 0
    
    with open(sub1 + '.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            try: 
                if row:
                    if (int(row[1]) >= 5):
                        sub1Dict[row[0]] = int(row[1])
                        sub1Total += int(row[1])
            except UnicodeDecodeError:
                pass
    
    with open('Base.csv') as basefile:
        basereader = csv.reader(basefile, delimiter = ',')
        for row in basereader:
            try:
               if row:
                    if (int(row[1]) >= 5 and row[0] not in baseDict):
                        baseDict[row[0]] = int(row[1])
                        baseTotal += int(row[1])
                    elif(int(row[1]) >= 5):
                        baseDict[row[0]] += int(row[1])
                        baseTotal += int(row[1])
            except UnicodeDecodeError:
                pass
    
    for key in sub1Dict:
        if (key in baseDict and sub1Dict[key] >= 5):
            if (key == 'this'):
                print(baseDict[key])
            diffs[key] = ((sub1Dict[key] / sub1Total) / (baseDict[key] / baseTotal))
        else:
            diffs[key] = sub1Dict[key]
    print("Here are the top ten unique words to the subreddit /r/" + sub1 + ":")
    print(sorted(diffs.items(), key=lambda item: item[1], reverse = True)[:10])
