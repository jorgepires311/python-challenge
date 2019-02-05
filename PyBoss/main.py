######################################################### import modules
import os 
import csv #read CSVs
######################################################### establish variables
empID = []
empName = []
empFirstName = []
empLastName = []
dobTemp = []
dob = []
ssntemp = []
ssn = []
state = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
######################################################### open csv file
with open('employee_data.csv', newline='') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=",") # print(csvReader)
    csvHeader= next(csvReader) # print(f'CSV Header: {csvHeader}')
######################################################### populate list with candidate votes
    for row in csvReader:
        empID.append(row[0]) # set employee ID column
        empName = split(" ",row[1])
        empFirstName.append(empName[0]) # set employee first name
        empFirstName.append(empName[1]) # set employee last name
        dobTemp = split("/",row[2])
        dob.append(dobTemp[2],"-",dobTemp[0],"-",dobTemp[1])  # set dob format
        #dob.append(dobTemp[0],"/",dobTemp[1],"/",dobTemp[2])  # set dob format
        ssnTemp = split("-",row[3])
        ssn.append("***-**-",ssnTemp[2]) # format SSN
        state.append(us_state_abbrev[row[4]]) # abreviate state
######################################################### join results
empTable = zip(empID,empFirstName,empLastName,dob,ssn,state)
######################################################### output results as csv file
output_file = os.path.join("output.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(empTable )