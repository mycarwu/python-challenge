# Modules
import os
import csv
import collections

# Set path for file
csvpath = '/Users/MyCar/Desktop/python-challenge/PyPoll/election_data.csv'
text_file = open("election_analysis.txt", "w") 

total_votes = 0

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    count = collections.Counter()

    for vote in csvreader:
        total_votes += 1

        candidate = vote[2]
        count[candidate] += 1

maxt = 0
sum_candidate = {}

for candidate,num_votes in count.items():
    percentage = num_votes/total_votes
    
    
    maxpercentage=float(percentage)
    maxt=max(maxt, maxpercentage)

    if float(percentage) == maxt:
        winner = candidate
     

def printandwrite(message):
    print(message)
    text_file.write(message)

printandwrite(f'Election Results\n')
printandwrite(f'-------------------------\n')
printandwrite(f'Total Votes: {total_votes}\n')
printandwrite(f'-------------------------\n')
for candidate,num_votes in count.items():
    percentage = (num_votes/total_votes)
    percentage = percentage * 100
    printandwrite(f'{candidate}: {percentage:.3f}% ({num_votes})\n')
printandwrite(f'-------------------------\n')
printandwrite(f'Winner: {winner}\n')
printandwrite(f'-------------------------\n')