import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

# Loop through csv file and push values to lists

    total_months = []
    net_total = []

    for row in csvreader:
        total_months.append(row[0])
        net_total.append(int(row[1]))

# Find the length of row. Append to that list the (row + 1) minus (the row before it).

    profit_change = []
    for i in range(len(net_total)-1):
        profit_change.append(net_total[i+1] - net_total[i])

# Determine the greatest increase and greatest decrease from the profit/losses_change calculation
increase = max(profit_change)
decrease = min(profit_change)

# Find the month associated with the greatest increase and greatest decrease.
month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1

# Print results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")

# Create txt file
output_path = os.path.join("analysis", "PyBank.txt")

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {len(total_months)}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${sum(net_total)}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")