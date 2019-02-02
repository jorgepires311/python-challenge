######################################################### import modules
import os 
import csv #read CSVs
from statistics import mean
######################################################### establish variables
totalMonths = 0
listMonths = []
listProfitLoss = []
totalProfitLoss = 0
changeProfitLoss = []
difProfitLoss = 0
averageProfitLoss = 0
greatestIncrease = 0
greatestIncreaseMonth = ""
greatestDecrease = 0
greatestDecreaseMonth = ""
######################################################### open csv file
with open('budget_data.csv', newline='') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=",") # print(csvReader)
    csvHeader= next(csvReader) # print(f'CSV Header: {csvHeader}')
######################################################### populate list with profit/loss
    for row in csvReader:
        listMonths.append(row[0])
        listProfitLoss.append(row[1])
######################################################### process data
    totalMonths = len(listProfitLoss) # count months
    listProfitLoss = [int(x) for x in listProfitLoss] # convert list items to integers
    totalProfitLoss = sum(listProfitLoss, 0) # sum of all profit/loss
    for x in range(totalMonths-1):  # compile list of change month to month
        difProfitLoss = listProfitLoss[x + 1] - listProfitLoss[x]
        changeProfitLoss.append(difProfitLoss)
        if(difProfitLoss >  greatestIncrease):
            greatestIncrease = difProfitLoss
            greatestIncreaseMonth = listMonths[listProfitLoss.index(listProfitLoss[x + 1])] # get greatest increase month
        if(difProfitLoss <  greatestDecrease):
            greatestDecrease = difProfitLoss
            greatestDecreaseMonth = listMonths[listProfitLoss.index(listProfitLoss[x + 1])] # get greatest decrease month
    averageProfitLoss = float("{0:.2f}".format(mean(changeProfitLoss))) # average change overall
######################################################### output analysis to consle
print('----------------------------------------------------')
print('Financial Analysis')
print('----------------------------------------------------')
print(f'Total Months:                   {totalMonths}')
print(f'Totals:                         ${totalProfitLoss}')
print(f'Average Change:                 ${averageProfitLoss}')
print(f'Greatest Increase in Profits:   {greatestIncreaseMonth} (${greatestIncrease})')
print(f'Greatest Decrease in Profits:   {greatestDecreaseMonth} (${greatestDecrease})')
print('----------------------------------------------------')
######################################################### output analysis to file
resultOutputFile = open("output.txt", "w")
resultOutputFile.write('----------------------------------------------------\n')
resultOutputFile.write('Financial Analysis\n')
resultOutputFile.write('----------------------------------------------------\n')
resultOutputFile.write(f'Total Months:                   {totalMonths}\n')
resultOutputFile.write(f'Totals:                         ${totalProfitLoss}\n')
resultOutputFile.write(f'Average Change:                 ${averageProfitLoss}\n')
resultOutputFile.write(f'Greatest Increase in Profits:   {greatestIncreaseMonth} (${greatestIncrease})\n')
resultOutputFile.write(f'Greatest Decrease in Profits:   {greatestDecreaseMonth} (${greatestDecrease})\n')
resultOutputFile.write('----------------------------------------------------\n')
resultOutputFile.close()