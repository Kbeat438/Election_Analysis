# Data we need
# 1. total number of votes cast
# 2. A list of candidates who recieved votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes won by each candidate
# 5. The winner of the election based on popular vote 
import csv
import os


#file_to_load = 'election_results.csv'
#election_data = open(file_to_load, 'r')

#election_data.close()

file_to_load = os.path.join("resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#with open(file_to_save, "w") as txt_file:

    #txt_file.write("Arapahoe\nDenver\nJefferson\n")
    
#outfile = open(file_to_save, "w")

#outfile.write("Hello World")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:

        total_votes += 1


        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]   

        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    winning_candidate_summary = (
         f"-----------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"-----------------------\n")
    print(winning_candidate_summary)        

        #print(f"{candidate_name}: received {round(vote_percentage, 1)}% of the vote.")


print(candidate_votes)