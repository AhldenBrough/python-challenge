# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


import os
import csv

# build path for the csv using os module
csvpath = os.path.join("Resources", "election_data.csv")

prev_vote_candidate = ""
votes_by_candidate = {}
total_votes = 0

# open csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header
    next(csvreader, None)

    # for each vote (keeping track of vote count with enumerate)
    for count, vote in enumerate(csvreader, start=1):

        #if current vote is for a different candidate than the previous
        if vote[2] != prev_vote_candidate and prev_vote_candidate != "":

            #if we weren't tracking that candidate yet
            if prev_vote_candidate not in votes_by_candidate:

                #add the candidate and their vote count to the dictionary
                votes_by_candidate[prev_vote_candidate] = total_votes

                #reset total_votes as we are moving on to another candidate
                total_votes = 0
            
            #if we were already tracking that candidate
            else:
                
                #add total_votes to their vote count
                votes_by_candidate[prev_vote_candidate] += total_votes

                #reset total_votes as we are moving on to another candidate
                total_votes = 0

        #increment total votes, whether or not we moved on to a new candidate we just counted a vote
        total_votes+=1
        prev_vote_candidate = vote[2]

print(votes_by_candidate)
print(count)