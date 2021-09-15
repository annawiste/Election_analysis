
#Retrieve Data
    #add dependencies
import csv
import os   
    #assign variable to load file
file_to_load = os.path.join("Resources", "election_results.csv")
    #assign variable for file to save results
file_to_save = os.path.join("Analysis", "election_analysis.txt")
    #open file as object
with open(file_to_load) as election_data:
    #read file object
    file_reader = csv.reader(election_data)
    #read header row
    headers = next(file_reader)
    print(headers)
# Total number of votes cast


# List of candidates who received votes


# Total number of votes each candidate received


# Percentage of votes each candidate won


# Winner based on popular vote