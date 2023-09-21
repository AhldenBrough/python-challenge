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

    prev_month = ""
    prev_value = 0
    #step through month by month (row by row)
    for count, month in enumerate(csvreader, start=1):
        
        #set current month and value (just to abstract for ease of understanding)
        curr_month = month[0]
        curr_value = int(month[1])

        #if it is the first time through set previous profit value to the current profit value
        if count ==1:
            #print("first time")
            prev_value = curr_value
            #print(f"current value is {curr_value}")

        #add current profit/loss to total
        total += curr_value

        #calculate the change in profit/loss from prev month to current
        change = curr_value - prev_value

        print("-------------")
        print(f"current month is {curr_month}")
        print(f"current value is {curr_value}")
        print(f"Previous months value is {prev_value}")
        print(f"change is {change}")
        print(f"is the previous value larger than the current? {curr_value < prev_value}")
        print(f"is the greatest decrease smaller than the current change? {change > greatest_decrease}")
        print(f"is python being super annoying {(prev_value > curr_value) and (change > greatest_decrease)}")
        print("-------------")

        #if the change is positive and is greater than the previously recorded greatest increase
        if (prev_value < curr_value) and (change > greatest_increase):
            
            greatest_increase = change
            
            inc_month = curr_month
            print(f"found new greatest increase at {curr_month}")

        #if the change is negative and is greater than the previously recorded greatest decrease
        elif (prev_value > curr_value) and (change < greatest_decrease):
            
            greatest_decrease = change
            
            dec_month = curr_month
            print(f"found new greatest decrease at {curr_month}")
        print("--end---")


        #set prev month to be current month for next iteration
        prev_month = curr_month
        prev_value = curr_value
print("---------")
print(count)
print("---------")
print(total)
print("---------")
print(greatest_decrease)
print(dec_month)
print("---------")
print(greatest_increase)
print(inc_month)