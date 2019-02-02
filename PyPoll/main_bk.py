######################################################### import modules
import os 
import csv #read CSVs
from statistics import mode
######################################################### establish variables
listCandidate = []
totalVotes = 0
kahnVotes = 0
kahnVotesPercent = 0
correyVotes = 0
correyVotesPercent = 0
liVotes = 0
liVotesPercent = 0
otooleyVotes = 0
otooleyVotesPercent = 0
winningCount = 0
winner = ""
######################################################### open csv file
with open('election_data.csv', newline='') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=",") # print(csvReader)
    csvHeader= next(csvReader) # print(f'CSV Header: {csvHeader}')
######################################################### populate list with voter
    for row in csvReader:
        listCandidate.append(row[2])
######################################################### process data
totalVotes = len(listCandidate) # get total votes
for x in range(totalVotes): # count each vote per candidate
    if (listCandidate[x] =='Khan'):
        kahnVotes += 1
    elif (listCandidate[x] =='Correy'):
        correyVotes +=  1
    elif (listCandidate[x] =='Li'):
        liVotes +=  1
    elif (listCandidate[x] =='O\'Tooley'):
        otooleyVotes +=  1
######################################################### calculate percentages
kahnVotesPercent = float("{0:.2f}".format((kahnVotes/totalVotes)*100))
correyVotesPercent = float("{0:.2f}".format((correyVotes/totalVotes)*100))
liVotesPercent = float("{0:.2f}".format((liVotes/totalVotes)*100))
otooleyVotesPercent = float("{0:.2f}".format((otooleyVotes/totalVotes)*100))
######################################################### find the winner
# winningCount = max(kahnVotes,correyVotes,liVotes,otooleyVotes)
# if(winningCount == kahnVotes):
#     winner = "Kahn"
# elif(winningCount == correyVotes):
#     winner = "Correy"
# elif(winningCount == liVotes):
#     winner = "Li"
# elif(winningCount == otooleyVotes):
#     winner = "O'Tooley"

winner = mode(listCandidate)
######################################################### output analysis
print('------------------------------------------')
print('Election Results')
print('------------------------------------------')
print(f'Total Votes: {totalVotes}')
print('------------------------------------------')
print(f'Kahn: {kahnVotesPercent}% ({kahnVotes})')
print(f'Correy: {correyVotesPercent}% ({correyVotes})')
print(f'Li: {liVotesPercent}% ({liVotes})')
print(f'O\'Tooley: {otooleyVotesPercent}% ({otooleyVotes})')
print('------------------------------------------')
print(f'Winner:   {winner}')
print('------------------------------------------')