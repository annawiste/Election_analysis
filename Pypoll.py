
#Retrieve Data
    #add dependencies
import csv
import os   
    #assign variable to load file
file_to_load = os.path.join("Resources", "election_results.csv")
    #assign variable for file to save results
file_to_save = os.path.join("Analysis", "election_analysis.txt")
    #set vote counter to 0
total_votes = 0
    #create candidate name list
candidate_options =[]
    #create candidate votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
     #open file
with open(file_to_load) as election_data:
    #read file object
    file_reader = csv.reader(election_data)
    #read header row
    headers = next(file_reader)
  
    #print all rows
    for row in file_reader:
        #Add to vote count
        total_votes +=1
        #get candidate name
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            #add candidate name to list
            candidate_options.append(candidate_name)
            #start vote count for that candidate
            candidate_votes[candidate_name] = 0
        #add votes to tally
        candidate_votes[candidate_name] +=1
    #iterate through candidate list
    for candidate_name in candidate_votes:
        #retrieve vote counts
        votes = candidate_votes[candidate_name]
        #calculate percentage of total
        vote_percentage = float(votes)/float(total_votes)*100

        #print candidate name and percentage
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine if vote count is greater than winning votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Total number of votes cast
#print(total_votes)

# List of candidates who received votes
#print(candidate_options)

# Total number of votes each candidate received
#print(candidate_votes)

# Percentage of votes each candidate won
#print(vote_percentage)

# Winner based on popular vote