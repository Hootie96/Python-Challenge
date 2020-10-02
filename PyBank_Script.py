import os
import csv
# import csv file into script
pyBank = os.path.join("budget_data.csv")
print(pyBank)
    
profit = []
monthlyChange = []
date = []

count = 0 
totalProfit = 0
totalChange = 0
startingProfit = 0

with open (pyBank) as csvFile:
    csvReader = csv.reader(csvFile, delimiter= ',')
    csvHeader = next(csvFile)
    
