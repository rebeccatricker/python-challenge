import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Read in the CSV file
with open(election_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


# Defining Variables
    total_votes = 0
    voter_id = []
    candidate_list = []
    unique_list = []
    unique_vote_count = []
    candidate_votes = {}

# Loop through csv file and push values to variable lists
    for row in csvreader:
        voter_id.append(row[0])
        candidate_list.append(str(row[2]))

# The total number of votes cast 
    total_votes = len(voter_id)
    # print(total_votes)
  
# Create a complete list of candidates who received a vote in addition to how many votes
for row in candidate_list: 
    if row not in unique_list:
        unique_vote_count = candidate_list.count(row)
        unique_list.append(row)
        candidate_votes[row] = unique_vote_count

# print(candidate_votes)

# The winner of the election based on popular vote 
winner = max(candidate_votes, key=candidate_votes.get)
# print(winner)

# Print all results
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for candidate_list in candidate_votes:
    percent = round(candidate_votes[candidate_list]/total_votes * 100,2)
    print(f"{candidate_list} : {percent}00% ({(candidate_votes[candidate_list])})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

# Create txt file
output_path = os.path.join("analysis", "PyPoll.txt")

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("----------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("\n")
    txtfile.write(f"---------------------")
    txtfile.write("\n")
    for candidate_list in candidate_votes:
        percent = round(candidate_votes[candidate_list]/total_votes * 100,2)
        txtfile.write(f"{candidate_list} : {percent}00% ({(candidate_votes[candidate_list])})\n")
    txtfile.write("----------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("\n")
    txtfile.write("----------------------")

