import os
import csv

#path for csv import and output text file
csvpath = os.path.join('/Users/devanshimathur/Module-3/PyBank', 'Resources', 'budget_data.csv')
output_path = os.path.join('/Users/devanshimathur/Module-3/PyBank', 'analysis', 'file.txt')

#variavle defined
total_month = 0
net_PL = 0
change_PL = 0
avg = 0
i = 0
maxval = 0
minval = 0
date1 = " "
date2 = " "
month = 0

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        val = int(row[1])
        # The total number of months included in the dataset
        total_month = total_month + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        net_PL = net_PL + val
        
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        change_PL = val - int(i)

        #the first month won't have a change as no older value than this
        if month == 0:
            change_PL = 0
        avg = avg + change_PL
        
        # The greatest increase in profits (date and amount) over the entire period
        if maxval <= change_PL:
            maxval = change_PL
            date1 = row[0]
            
        # The greatest decrease in profits (date and amount) over the entire period
        if minval >= change_PL:
            minval = change_PL
            date2 = row[0]
        
        # old profit/loss value is saved as i
        i = val
        month = month +1
        
    avg_change = round(avg/(total_month-1),2)

    #print the analysis to the terminal 
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(total_month))
    print("Total: $"+str(net_PL))
    print("Average Change: $"+str(avg_change))
    print("Greatest Increase in Profits:",date1,"($"+str(maxval)+")")
    print("Greatest Decrease in Profits:",date2,"($"+str(minval)+")")


    #export a text file with the results
    f = open(output_path, "w")
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print("Total Months: "+str(total_month), file=f)
    print("Total: $"+str(net_PL), file=f)
    print("Average Change: $"+str(avg_change), file=f)
    print("Greatest Increase in Profits:",date1,"($"+str(maxval)+")", file=f)
    print("Greatest Decrease in Profits:",date2,"($"+str(minval)+")", file=f)
    f.close()
   