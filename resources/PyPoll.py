# Data we need
# 1. total number of votes cast
# 2. A list of candidates who recieved votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes won by each candidate
# 5. The winner of the election based on popular vote 

#add dependencies
import csv
import os

#assigns a variable to load a file from the path
file_to_load = os.path.join("resources", "election_results.csv")
#assigns a variable to save the file from the path 
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize a total vote counter
total_votes = 0
# canidate options and votes
candidate_options = []
candidate_votes = {}
#tracking the winner 
winning_candidate = ""
winning_count = 0
winning_percentage = 0 
#open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
    #print each row in the CSV file 
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #get candidate name
        candidate_name = row[2]
        # only if the candidate name isn't already added
        if candidate_name not in candidate_options:
            #add the candidate name to the list
            candidate_options.append(candidate_name)
            #trackining candidate voter count
            candidate_votes[candidate_name] = 0
        #adds a vote to the candidates vote count
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        #retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]   

        vote_percentage = float(votes) / float(total_votes) * 100

        #prints each candidate, their voter count, and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #determines the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name
    #prints the winning candidates results
    winning_candidate_summary = (
         f"-----------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"-----------------------\n")
    print(winning_candidate_summary)        
