import csv
import os

# build path for the csv using os module
csvpath = os.path.join("Resources", "budget_data.csv")

# initialize total
total = 0
total_change = 0

# initialize variables to track greatest increase and decrease as we step through the csv
greatest_increase = 0
greatest_decrease = 0
inc_month = ""
dec_month = ""

# open csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header
    next(csvreader, None)

    prev_month = ""
    prev_value = 0
    # step through month by month (row by row)
    for count, month in enumerate(csvreader, start=1):
        
        # set current month and value (just to abstract for ease of understanding)
        curr_month = month[0]
        curr_value = int(month[1])

        # if it is the first time through set previous profit value to the current profit value
        if count ==1:

            prev_value = curr_value

        # add current profit/loss to total
        total += curr_value

        # calculate the change in profit/loss from prev month to current
        change = curr_value - prev_value

        # if the change is positive and is greater than the previously recorded greatest increase
        if (prev_value < curr_value) and (change > greatest_increase):
            
            greatest_increase = change
            
            inc_month = curr_month

        # if the change is negative and is greater than the previously recorded greatest decrease
        elif (prev_value > curr_value) and (change < greatest_decrease):
            
            greatest_decrease = change
            
            dec_month = curr_month

        # add change to total change
        total_change += change

        # set prev month to be current month for next iteration
        prev_month = curr_month
        prev_value = curr_value

# calculate average change, subtracting 1 from count because there is 1 less change than there are values
avg_change = round(total_change/(count-1), 2)

# create output file
output_path = os.path.join("analysis", "analysis.txt")

# build output file contents
f_output = open(output_path, "w")
f_output.write("Financial Analysis\n")
f_output.write("----------------------------\n")
f_output.write(f"Total Months: {count}\n")
f_output.write(f"Total ${total}\n")
f_output.write(f"Average Change: ${avg_change}\n")
f_output.write(f"Greatest Increase in Profits: {inc_month} (${greatest_increase})\n")
f_output.write(f"Greatest Decrease in Profits: {dec_month} (${greatest_decrease})\n")

# print output file to stdout
# Citation David Alber https://stackoverflow.com/questions/8084260/how-to-print-a-file-to-stdout
with open(output_path, 'r') as f_output:
    print(f_output.read())