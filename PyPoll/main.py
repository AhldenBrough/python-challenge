import os
import csv

# build path for the csv using os module
csvpath = os.path.join("Resources", "election_data.csv")

#initialize dictionary to keep track of candidates and votes, key value pairs will be: candidate, vote count
votes_by_candidate = {}

# open csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header
    next(csvreader, None)

    # for each vote (keeping track of vote count with enumerate)
    for count, vote in enumerate(csvreader, start=1):

        #if the candidate isn't in the dictionary of candidates
        if vote[2] not in votes_by_candidate:

            #set vote count to 0, we will incrememnt outside of if block
            votes_by_candidate[vote[2]] = 0

        #increment vote count for the selected candidate
        votes_by_candidate[vote[2]] += 1

# define path for output
output_path = os.path.join("analysis", "analysis.txt")

# open output file for writing
f_output = open(output_path, "w")

# write output
f_output.write("Election Results\n")
f_output.write("-------------------------\n")
f_output.write(f"Total Votes: {count}\n")
f_output.write("-------------------------\n")

# for each key value pair in our dictionary, calculate the percentage of the total vote
for candidate, votes in votes_by_candidate.items() :
    f_output.write(f"{candidate}: {round( ((votes/count) * 100), 3 )}% ({votes})\n")
f_output.write("-------------------------\n")

# Citation: comment from Atcold https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
f_output.write(f"Winner: {max(votes_by_candidate, key=lambda key: votes_by_candidate[key])}\n")
f_output.write("-------------------------\n")

# print output file to stdout
# Citation David Alber https://stackoverflow.com/questions/8084260/how-to-print-a-file-to-stdout
with open(output_path, 'r') as f_output:
    print(f_output.read())