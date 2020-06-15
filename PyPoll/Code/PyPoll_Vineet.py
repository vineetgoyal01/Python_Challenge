import os
import csv


# Path to collect data from the Resources folder
poll_csv = os.path.join("..", "Resources", "02-Homework_03-Python_PyPoll_Resources_election_data.csv")

# Read in the CSV file
with open(poll_csv, 'r', encoding="utf-8") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    count = 0
    candidate_list = []
    candidate_name = ""
    candidate_name_check = ""
    candidate_count_name = str()
    candidate_count = int()
    candidate_Percentile = int()
    

    # Loop through the data
    for row in csvreader:
        # total Votes
        count = count + 1
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

    candidate_count = len(candidate_list) 
    
    print("Election results")
    print("---------------------------------------")
    print(f"Total number of Votes Cast : {count}")
    
    print("---------------------------------------")
   

    for i in range(candidate_count):
        csvfile.seek(1)
        candidate_vote_count = 0
        for row in csvreader:
            candidate_name_check = row[2]
            if candidate_name_check == candidate_list[i]:
                candidate_vote_count = candidate_vote_count + 1

        candidate_Percentile = (candidate_vote_count/count)*100
        formatted_percnetile = "{:.2f}".format(candidate_Percentile)
        print(f"{candidate_list[i]} = {formatted_percnetile} %")
    

