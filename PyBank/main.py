import csv
import os

#build path for the csv using os module
csvpath = os.path.join("Resources", "budget_data.csv")

#initialize total
total = 0

#initialize variables to track greatest increase and decrease as we step through the csv
greatest_increase = 0
greatest_decrease = 0
inc_month = ""
dec_month = ""

#open csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    next(csvreader, None)

    #step through month by month (row by row)
    for count, month in enumerate(csvreader, start=1):
        total += int(month[1])

print(count)