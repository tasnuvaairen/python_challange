import os
import csv

print ("                                 ")
print ("Financial Analysis")
print ("--------------------------------")

# Set path
csvpath = os.path.join("pybank","Resources","budget_data.csv")
outputpath =  os.path.join("pybank","Resources","budget_data.txt")

# Set Variables
total_months = 1 
total_pl = 0 
total_pl_change = 0 
previous_pl = 0
pl_change = []
average_change = 0 
greatest_increase = ["",0]
greatest_decrease = ["",99999999999999999999]
gincrease = 0
gdecrease = 0
pl_changes = []
months=[]

# Read csv file
with open(csvpath, newline='') as csvfile, open(outputpath, 'w') as outputfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    # Print(f"CSV Header: {csv_header}")
    
    # Reading the first line to initialize 
    row = next(csvreader,None) 
    # Initialize
    previous_pl = int(row[1])   
    total_pl = int(row[1]) 
    
    for row in csvreader:
       total_months= total_months+1
       # Total revenue
       total_pl = int(total_pl) +int(row[1]) 
  
       # The average of the changes in "Profit/Losses" over the entire period 
       # Revenue change      
       pl_change = int(row[1]) - previous_pl 

       total_pl_change = total_pl_change + pl_change 

       # The greatest increase or decrease 
       if (pl_change >= greatest_increase[1]): 
            greatest_increase[1] = pl_change
            greatest_increase[0] = row[0]

       if (pl_change < greatest_decrease[1]):
            greatest_decrease[1] = pl_change
            greatest_decrease[0] = row[0]

       # Add to the revenue_changes list
       pl_changes.append(pl_change)
       previous_pl = int(row[1]) 

    # Set the totalrRevenue average change

    pl_avg_change = float(total_pl_change)/(total_months-1)
    
    print (f"Total Months: {total_months}")
    print (f"Total: $ {total_pl}")  
    print(f"Average Change: ${pl_avg_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]}, (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})") 
    print ("------")

    # Write output to file
    outputfile.write(f"Financial Analysis\n----------------------------\n")
    outputfile.write(f"Total Months: " + str(total_months) + "\n")
    outputfile.write(f"Total: $" + str(total_pl) + "\n")
    outputfile.write(f"Average Change: ${pl_avg_change:.2f})" + "\n")
    outputfile.write(f"Greatest Increase in Profits: " + str(greatest_increase[0]) + ", ($" + str(greatest_increase[1]) + ")\n")
    outputfile.write(f"Greatest Decrease in Profits: " + str(greatest_decrease[0]) + ", ($" + str(greatest_decrease[1]) + ")\n")
    
    

