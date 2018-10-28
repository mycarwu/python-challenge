# Modules
import os
import csv

# Set path for file
csvpath = '/Users/MyCar/Desktop/python-challenge/PyBank/budget_data.csv'
file_to_output = os.path.join("..", "PyBank", "budget_analysis.txt")

num_months = 0

Total = 0

change_list = []

month_change = []

max_increase = ["",0]

max_decrease = ["", 9999999999]

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    firstmonth = next(csvreader)
    num_months = num_months + 1
    Total = Total + int(firstmonth [1])
    prev_change = int(firstmonth[1])

    for months in csvreader:
        
        #Track Total
        num_months = num_months + 1

        Total = Total + int(months[1])

        #The change
        change = int(months[1]) - prev_change
        prev_change = int(months[1])
        change_list = change_list + [change]
        month_change = month_change + [months[0]]
        
        if change > max_increase[1]:
            max_increase[1] = change
            max_increase[0] = months[0]

        if change < max_decrease[1]:
            max_decrease[1] = change
            max_decrease[0] = months[0]

total_change = sum(change_list)/len(change_list)

output= (

    f"Financial Analysis\n"

    f"----------------------------\n"

    f'Total Months: {num_months}\n'

    f'Total: ${Total}\n'

    f'Average Change: ${total_change:.2f}\n'

    f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n'

    f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n')

print(output)

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)