######################################################### import modules
import os 
import csv #read CSVs
from statistics import mean
######################################################### establish variables
totalMonths = 0
listMonths = []
listProfitLoss = []
totalProfitLoss = 0
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
    averageProfitLoss = float("{0:.2f}".format(mean(listProfitLoss))) # average change per month
    greatestIncrease = max(listProfitLoss) # get greatest increase amount
    greatestIncreaseMonth = listMonths[listProfitLoss.index(greatestIncrease)] # get greatest increase month
    greatestDecrease = min(listProfitLoss) # get greatest decrease amount
    greatestDecreaseMonth = listMonths[listProfitLoss.index(greatestDecrease)] # get greatest decrease month

    greatestDif = greatestDecrease - greatestIncrease
######################################################### output analysis
print('---------------------------------------------------------')
print('Financial Analysis')
print('---------------------------------------------------------')
print(f'Total Months:                   {totalMonths}')
print(f'Totals:                         ${totalProfitLoss}')
print(f'Average Change:                 ${averageProfitLoss}')
print(f'Greatest Increase in Profits:   {greatestIncreaseMonth} (${greatestIncrease})')
print(f'Greatest Decrease in Profits:   {greatestDecreaseMonth} (${greatestDecrease})')
print('---------------------------------------------------------')
print(greatestDif)
