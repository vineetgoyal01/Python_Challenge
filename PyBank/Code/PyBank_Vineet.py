import os
import csv


# Path to collect data from the Resources folder
bank_csv = os.path.join("..", "Resources", "02-Homework_03-Python_PyBank_Resources_budget_data.csv")

# Read in the CSV file
with open(bank_csv, 'r', encoding="utf-8") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    count = 0
    profit = 0
    loss = 0

    # Loop through the data
    for row in csvreader:
        # total calculation
      
        
        col_as_int = int(row[1])
        total = total + col_as_int
        count = count + 1
        average = float(total/count)


    
        if col_as_int>profit:
    
            profit = col_as_int
            profit_month = row[0]
            print(profit)

        if col_as_int<loss:

            loss = col_as_int
            loss_month = row[0]
            print(loss)


    print(f"Total Months : {count}")
    print(f"Total : ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits : {profit_month} (${profit}) ")
    print(f"Greatest Decrease in Profits : {loss_month} (${loss}) ")

        