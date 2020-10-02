import os
import csv
# import csv file into script
pyBank = r'C:\Users\kaleb\Documents\AirAce Docs\Payroll 2020\Python-Challenge\PyBank\budget_data.csv'

    
profit = []
monthlyChange = []
date = []

months = 0 
totalProfit = 0
totalChange = 0
startingProfit = 0

with open (pyBank) as csvFile:
    csvReader = csv.reader(csvFile, delimiter= ',')
    csvHeader = next(csvFile)
for row in csvReader:    
    months = months + 1
date.append(row[0])

profit.append(row[1])
totalProfit = totalProfit + int(row[1])

finalProfit = int(row[1])
monthlyChangeProfit = totalProfit - startingProfit

monthlyChange.append(monthlyChangeProfit)




    
