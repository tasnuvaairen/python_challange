import os
import csv

print("                                          ")
print ("Election Results")
print ("-----------------------------------------")
# Set Value
total_votes = 0
candidates=[]
vote_count = []

# Set file path
csvpath = os.path.join("pypoll\Resources\election_data.csv") 

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader, None)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # For each row, update the total vote by adding the next  
        total_votes = total_votes + 1

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            # Print (f"Candidate Index: {candidate_index}")
            vote_count.insert(candidate_index,1)
        else:
            candidate_index = candidates.index(row[2])
            vote_count[candidate_index] = vote_count[candidate_index] +1

    print(f"Total Votes : {total_votes}")
    print ("-----------------------------------------")
    for candidate in candidates:
        candidate_index = candidates.index(candidate)
        percent_won = vote_count[candidate_index]/total_votes * 100
        print(f"{candidates[candidate_index]}: {percent_won:.3f}%, ({vote_count[candidate_index]})")

    
max=max(vote_count)
max_index = vote_count.index(max)
print ("---------------------------------")
print(f"Winner : {candidates[max_index ]}")
print ("---------------------------------")
