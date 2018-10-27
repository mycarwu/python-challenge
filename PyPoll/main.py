# Modules
import os
import csv
import collections

# Set path for file
csvpath = '/Users/MyCar/Desktop/python-challenge/PyPoll/election_data.csv'
file_to_output = os.path.join("..", "PyPoll", "election_analysis.txt")

total_votes = 0

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    count = collections.Counter()

    for vote in csvreader:
        total_votes += 1

        candidate = vote[2]
        count[candidate] += 1

total_dups = 0
maxt = 0

for candidate,num_votes in count.items():
    percentage = (num_votes/total_votes)*100.00
    printlater = (f'{candidate}: {(percentage)}% ({num_votes})')
    

    maxpercentage=int(percentage)
    maxt=max(maxt, maxpercentage)

    if int(percentage) == maxt:
        winner = candidate

    output = (
    f'Election Results\n'
    f'-------------------------\n'
    f'Total Votes:{total_votes}\n'
    f'{printlater}\n'
    f'-------------------------\n'
    f'Winner: {winner}\n'
    f'-------------------------\n'
    )

    print(output)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)