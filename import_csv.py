"""
Simple program to ingest sample.csv file with Month on x-axis stored as index
program prints result set of csv file
displays list of months
ask user to input which month they would like to see row data for
simple error handling will ask question again if input not valid
display row from input
"""

import csv

with open('sample1.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #NOTE: ALL data is read in as a string

    months = []  #empty list for month names
    oneRow = []  #empty list for 

    next(readCSV) #skip the first line if it is the header/column names
    
    for row in readCSV:
        print(row[:])                    #print each row
        #print(row[0])                   #print the first element of each row
        #print(row[0],row[1], row[2])    #print first 3 elements of each row
        r = row[:]                       #slice each elements into oneRow
        oneRow.append(r)
        
        month = row[0]
        months.append(month)

print('This is a list of each month in the dataset'        )
print(months)

whatMonth = input('What month do you want to see the row of? ')

#simple error handling to reset whatMonth in case input is not in list months
while whatMonth not in months:
    print('not in list')
    whatMonth = input('What month do you want to see the row of?')
    

monthdex = months.index(whatMonth)

#print(monthdex)     
print(oneRow[monthdex])
