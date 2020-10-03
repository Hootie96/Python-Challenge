import os
import csv
# import csv file into script
pyBank = r'C:\Users\kaleb\Documents\AirAce Docs\Payroll 2020\Python-Challenge\PyBank\budget_data.csv'

# define the lists to append 
profit = []
monthlyChange = []
date = []
# set starting values for variables I want to count.  
months = 0
totalProfit = 0
totalChange = 0
startingProfit = 0
# open the csv file so computer can begin operating on the data
with open(pyBank) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    csvHeader = next(csvFile)
    # start my for loop to begin running through the data.  I need to count and append the months for further operations
    for row in csvReader:
        months = months + 1
# date will be needed for finding increase and decrease.          
        date.append(row[0])
# find the total profit from the data set
        profit.append(row[1])
        totalProfit = totalProfit + int(row[1])
#Calculate the change between the months
        finalProfit = int(row[1])
        monthlyChangeProfit = finalProfit - startingProfit
#append that monthly change to the monthly change list
        monthlyChange.append(monthlyChangeProfit)

        totalChange = totalChange + monthlyChangeProfit
        startingProfit = finalProfit
# calulate the average change over the dataset to find average change
        averageChangeProfit = (totalChange/months)
#caluculate greatest increase and decrease by using the date to figure it out.
        greatestIncreaseProfits = max(monthlyChange)
        greatestDecreaseProfits = min(monthlyChange)
        increaseDate = date[monthlyChange.index(greatestIncreaseProfits)]
        decreaseDate = date[monthlyChange.index(greatestDecreaseProfits)]
#print these to terminal to see if the data comes out correctly
print("Financial Analysis")
print("-------------------------")
print("Total Months:" + str(months))
print("Total Profits:" + "$" + str(totalProfit))
print("Average Change:" + "$" + str(int(averageChangeProfit)))
print("Greatest Increase in Profits:" + str(increaseDate) +
      "$" + str(int(greatestIncreaseProfits)))
print("Greatest Decrease Profits:" + str(decreaseDate) +
      "$" + str(int(greatestDecreaseProfits)))
# write this information into a text file 
with open("pyBank.txt", 'w') as text:
    text.write("Financial Analysis")
    text.write("---------------------------" + "\n\n")
    text.write("Total Months: " +        str(months) + "\n")
    text.write("Total Profits: "  +        '$' + str(totalProfit) + "\n")
    text.write("Average Change: " +        '$' + str(int(averageChangeProfit)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increaseDate) +        "$" + str(greatestIncreaseProfits) + "\n")
    text.write("Greatest Decrease in Profits: " + str(decreaseDate) +        "$" + str(greatestDecreaseProfits) + "\n")
    #final note...  The print file printed the correct information, but I had a lot of trouble getting it to write in seperate lines
    # I seperated the rows manually so it reads more easily.