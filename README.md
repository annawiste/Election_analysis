# Board of Elections Audit

## Overview of Election Audit
An election audit was requested by a Colorado Board of Elections employee. There were three candidates in this election. The precinct includes three counties (Jefferson, Denver and Arapahoe). The goal is to provide a simple script which can process raw election results quickly, and can be readily used or adapted for auditing other election results. 
The input file includes the full election results, with the ballot ID, county, and chosen candidate. 
[election_results.csv](Resources/election_results.csv)

The analysis includes an overview of votes cast, with county of origin, and number/percentage cast for each candidate.

## Election-Audit Results
- There were 369,711 total votes cast:

      # For each row in the CSV file.
      for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
        
- The votes were cast in three counties:        
  - Jefferson County: 38,855 votes (10.5%)
  - Denver County: 306,055 votes (82.8%)
  - Arapahoe County: 24,801 votes (6.7%)

     First county names were extracted into a list, and a dictionary was initialized for the number of votes. Trackers for each county are set to 0. 
     A for loop then extracts the number of votes.

        for county_name in county_votes:
          # 6b: Retrieve the county vote count.
          votes = county_votes.get(county_name)
          # 6c: Calculate the percentage of votes for the county.
          votes_percentage = float(votes)/float(total_votes)*100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {votes_percentage:.1f}% ({votes:,})\n")
        
- The county from which the highest number of votes originated is Denver County.
     
     First set trackers for the largest county and county voter turnout.
       
        largest_county = ""
        largest_count = 0
 
     In the last step of the for loop from above, county results are checked against the trackers to identify the county with the largest number of votes. 
 
        if (votes > largest_count):
            largest_count = votes
            largest_county = county_name

- There were three candidates who received votes in the election, with the following results: 
  - Charles Casper Stockham received 23.0% of the vote (85,213 votes).
  - Diana DeGette received 73.8% of the vote (272,892 votes).
  - Raymon Anthony Doane received 3.1% of the vote (11,606 votes).

      First candidate names were extracted into a list, and a dictionary initialized for linking votes to candidates. Trackers for each candidate were set to 0.
      A for loop then extracts the votes for each candidate.
      
        for candidate_name in candidate_votes:

          # Retrieve vote count and percentage
          votes = candidate_votes.get(candidate_name)
          vote_percentage = float(votes) / float(total_votes) * 100
          candidate_results = (
              f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

- The winner of this election is:
  - Diana DeGette, who received 73.8% of the votes (272,892).
      
     First trackers were set for the winning candidate, vote count and percentage
      
          winning_candidate = ""
          winning_count = 0
          winning_percentage = 0


       In the last step of the for loop from above, the results are checked against the trackers to determine the winner.
       
            if (votes > winning_count) and (vote_percentage > winning_percentage):
              winning_count = votes
              winning_candidate = candidate_name
              winning_percentage = vote_percentage
              
## Election-Audit Summary
This script can be used to audit any election results which are available in the same format as this input file. Namely, there is one row in the file for each vote, the county name is the second item in each row, and the candidate is the third. If the datafile is set up differently, two lines would need to be changed to reflect the setup of the new file. The candidate_name and county_name might need to be extracted from a different element of the row, rather than 2 and 1, respectively.

      # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

The script is currently set to read in a .csv file, which is a very common file type for data like this. The script includes importing the library 'csv' to handle the file. There are similar libraries available in python to read in other data formats. Therefore if election results are available in another format, the script can be easily adapted by updating the library and the line in which the file is read. 

      with open(file_to_load) as election_data:
            reader = csv.reader(election_data)
 
These are two ways in which the script could be easily adapted to work with different types of results files, as long as the data has one vote for each row and includes the county and candidate information in that row. 
