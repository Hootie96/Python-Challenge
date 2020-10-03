import os
import csv

pyPoll = r'C:\Users\Kaleb\Python-Challenge\pyPoll\election_data.csv'
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
   # calculate winner by finding the max voteCount
    winningCount = max(voteCount)
    winner = candidateName[voteCount.index(winningCount)]
# print out results into terminal
print("Election Results")
print('-----------------')
print("Total Votes:" + str(voteCount))
# I need to set up a for loop to iterate through the candidate list
for i in range(len(candidateName)):
    print(candidateName[i] + ": " + str(votePercentage[i]) + "% ("+ str(voteCount[i])+ ")")
print("winner is: " + winner)

with open('electionResults.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------\n")
    text.write("Total VOtes: " + str(voteCount) + "\n")
    for i in range(len(candidateName)):
        text.write(candidateName[i] + ": " + str(votePercentage[i]) + "% ("+ str(voteCount[i])+ ")\n")
    text.write("The Winner is: " + winner + "\n")
    text.write("-----------------------")


    