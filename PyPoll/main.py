import os
import csv

pyPoll = r'C:\Users\kaleb\Documents\AirAce Docs\Payroll 2020\Python-Challenge\PyPoll\election_data.csv'
# set up count and lists
count = 0
# of all candidates
candidateList = []
# list of candidate names 
candidateName = []
# list of percentage vote
votePercentage = []
# list of total vote count
voteCount = []
# open the csv file
with open(pyPoll, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    csvHeader = next(csvReader)
# start for loop to process through the data
    for row in csvReader:
# count rows
        count = count + 1
# append the candidates
        candidateList.append(row[2])
# find the individual candidates in the list as it itterates
    for x in set(candidateList):
        candidateName.append(x)
    # count how many votes each candidate got
        y = candidateList.count(x)
        voteCount.append(y)
    #z percentage of votes won
        z = (y/count)*100
        votePercentage.append(z)
    winningCount = max(voteCount)
    winner = candidateName[voteCount.index(winningCount)]


# percentage of votes each candidate won (percent of votes = % won / total)
# count how many votes each candidate won
# max votes from count = winner

# make a table that displays top 4 candidates, their percentage of votes, and total votes

# display winner at the bottom

