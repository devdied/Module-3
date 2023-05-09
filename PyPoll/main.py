import os
import csv

#path for csv import and output text file
csvpath = os.path.join('/Users/devanshimathur/Module-3/PyPoll', 'Resources', 'election_data.csv')
output_path = os.path.join('/Users/devanshimathur/Module-3/PyPoll', 'analysis', 'file.txt')


with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #variavle defined
    count = 0
    total = 0
    votes = []
    cnd = " "
    candidate = []
    unique_candidate = []
    
    # Read each row of data after the header and make a save candidate column as list
    for row in csvreader:
        candidate.append(row[2])
        
    #sort the candidate list
    candidate.sort()
    
    #count the votes until candidate is changed
    for i in candidate:
        if i != cnd:
            cnd = i
            #counting votes of each candidate
            votes.append(count+1)
            #saving unique candidates
            unique_candidate.append(cnd)
            #zero count everytime candidate changes
            count = 0
        else:
            #keep counting until the candidate changes
            count = count+1
            
        #total number of votes
        total = total +1
        
    #appending the last candiidate vote value 
    votes.append(total-sum(votes)+1)
    #removing the first value in votes as its always zero
    votes.pop(0)
    
    #printing all the asked values
    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+ str(total))
    print("-------------------------")
    for j in range(len(votes)):     
        print(unique_candidate[j]+": "+str(round(votes[j]*100/total,3))+"% ("+ str(votes[j])+")")
    print("-------------------------")
    print("Winner: "+ unique_candidate[votes.index(max(votes))])
    print("-------------------------")
    
    #export a text file with the results
    f = open(output_path, "w") 
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes: "+ str(total), file=f)
    print("-------------------------", file=f)
    for j in range(len(votes)):     
        print(unique_candidate[j]+": "+str(round(votes[j]*100/total,3))+"% ("+ str(votes[j])+")", file=f)        
    print("-------------------------", file=f)
    print("Winner: "+ unique_candidate[votes.index(max(votes))], file=f)
    print("-------------------------", file=f)
    f.close()