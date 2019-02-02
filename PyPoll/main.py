######################################################### import modules
import os 
import csv #read CSVs
######################################################### establish variables
listCandidate = []
totalVotes = 0
candidates = []
candidateVotes = []
candidatePercent = []
winner = ""
######################################################### open csv file
with open('election_data.csv', newline='') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=",") # print(csvReader)
    csvHeader= next(csvReader) # print(f'CSV Header: {csvHeader}')
######################################################### populate list with candidate votes
    for row in csvReader:
        listCandidate.append(row[2])
######################################################### process data
    totalVotes = len(listCandidate) # get total votes
    for x in range(len(listCandidate)):
        current = listCandidate[x]
        if(current not in candidates):
            candidates.append(current)
            candidateVotes.append(0) # initial vote count list for number of candidates
            candidatePercent.append(0) # initial vote percentage list for number of candidates
        candidateVotes[candidates.index(listCandidate[x])] += 1 # count votes per candidate
    for x in range(len(candidates)): # calculate percentages
        candidatePercent[candidates.index(candidates[x])] = float("{0:.2f}".format((candidateVotes[candidates.index(candidates[x])]/totalVotes)*100))
    winner = candidates[candidateVotes.index(max(candidateVotes))] # find the winner
######################################################### output analysis to console
print('------------------------------------------')
print('Election Results')
print('------------------------------------------')
print(f'Total Votes: {totalVotes}')
print('------------------------------------------')
for x in range(len(candidates)):
    print(f'{candidates[x]}: {candidatePercent[x]}% ({candidateVotes[x]})')
print('------------------------------------------')
print(f'Winner:   {winner}')
print('------------------------------------------')
######################################################### output analysis to file
resultOutputFile = open("output.txt", "w")
resultOutputFile.write('------------------------------------------\n')
resultOutputFile.write('Election Results\n')
resultOutputFile.write('------------------------------------------\n')
resultOutputFile.write(f'Total Votes: {totalVotes}\n')
resultOutputFile.write('------------------------------------------\n')
for x in range(len(candidates)):
    resultOutputFile.write(f'{candidates[x]}: {candidatePercent[x]}% ({candidateVotes[x]})\n')
resultOutputFile.write('------------------------------------------\n')
resultOutputFile.write(f'Winner:   {winner}\n')
resultOutputFile.write('------------------------------------------\n')
resultOutputFile.close()