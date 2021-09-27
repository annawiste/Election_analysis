
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

#Save results to text file  
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    #iterate through candidate list
    for candidate_name in candidate_votes:
        #retrieve vote counts
        votes = candidate_votes[candidate_name]
        #calculate percentage of total
        vote_percentage = float(votes)/float(total_votes)*100

        #Store candidate name and vote results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print candidate name, percentage and vote count
        print(candidate_results)
        #write results to txt file
        txt_file.write(candidate_results)

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
    txt_file.write(winning_candidate_summary)


