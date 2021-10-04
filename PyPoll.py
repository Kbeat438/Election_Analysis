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



#with open(file_to_save, "w") as txt_file:

    #txt_file.write("Arapahoe\nDenver\nJefferson\n")
    
#outfile = open(file_to_save, "w")

#outfile.write("Hello World")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)