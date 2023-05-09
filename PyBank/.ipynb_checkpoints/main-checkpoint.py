import os
import csv

csvpath = os.path.join('/Users/devanshimathur/Module-3/PyBank', 'Resources', 'budget_data.csv')

total_month = 0
net_PL = 0
change_PL = 0
avg = 0
i = 0
maxval = 0
minval = 0
date1 = "a"
date2 = "a"

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        val = int(row[1])
        # The total number of months included in the dataset
        total_month = total_month + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        net_PL = net_PL + val
        
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_PL = val - int(i)
        avg = avg + change_PL
        
        # The greatest increase in profits (date and amount) over the entire period
        if maxval <= change_PL:
            maxval = change_PL
            date1 = row[0]
            
        # The greatest decrease in profits (date and amount) over the entire period
        if minval >= change_PL:
            minval = change_PL
            date2 = row[0]
        
        # old profit/loss value
        i = val
    
    #print the analysis to the terminal 
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(total_month))
    print("Total: $"+str(net_PL))
    print("Average Change: $"+str(avg/total_month))
    print("Greatest Increase in Profits:",date1,"($"+str(maxval)+")")
    print("Greatest Decrease in Profits:",date2,"($"+str(minval)+")")


    #export a text file with the results
    f = open("file.txt", "w")
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print("Total Months: "+str(total_month), file=f)
    print("Total: $"+str(net_PL), file=f)
    print("Average Change: $"+str(avg/total_month), file=f)
    print("Greatest Increase in Profits:",date1,"($"+str(maxval)+")", file=f)
    print("Greatest Decrease in Profits:",date2,"($"+str(minval)+")", file=f)
    f.close()