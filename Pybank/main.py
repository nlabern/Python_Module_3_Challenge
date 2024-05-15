#python data 

#import os module
import os
#import csv module
import csv
#make variable for total months in dataset
#make variable for total profits/losses in dataset
#make variable for average change in dataset
total_months = []
total_amount = []
average_change = []

#read in csv module
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

#open csv for use & enter encoding (windows)
with open(csvpath,encoding="utf-8") as csvfile:
    #delimited by commas
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #ignore headers
    csv_header = next(csvreader)
   #append rows for month count & sum total 
    for row in csvreader:

        total_months.append(row[0])
        total_amount.append(int(row[1]))
        #loop through each profit change to calculate average change
    for i in range(len(total_amount)-1):
        average_change.append(total_amount[i+1]-total_amount[i])
#make variables for greatest increase & greatest decrease in dataset
greatest_increase = max(average_change)
greatest_decrease = min(average_change)   
#attach greatest increase & greatest decrease to corresponding months
#add 1 to designate max & min to month following the calculation
greatest_increase_month = average_change.index(max(average_change)) + 1
greatest_decrease_month = average_change.index(min(average_change)) + 1

#print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {len(total_months)}" )
print(f"Total: ${sum(total_amount)}")
#calculate average change and round to two decimal points; (sum of changes/amount of changes)
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
#make greatest increase/decrease values a string, add dollar sign, and attach corresponding months
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
        
#export results in text file
analysis = os.path.join("Analysis", "Financial_Analysis.txt")
with open(analysis,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months : {len(total_months)}" )
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")
        
 #Cantu, G(2018) GitHub source code [Python]. https://github.com/cantugabriela/Python-Challenge/blob/master/PyBank/main.py
 #referenced this code to help write out text file & do greatest increase/greatest decrease calculations


