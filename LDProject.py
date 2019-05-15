import random
OpenedDataFile = open('employees1000.csv')

#What the new csv file will be called.
finalFile = input('What do you want to call the file? ')
final = open(finalFile,'w+')


###Variables

#A variable that will store all the used usernames so that there will be no repeats.
listOfUsernames = list()

#A variable that keeps track of commas so that the position in the line of the file is known.
counterOfCommas = 0

#In case of a tie for usernames, this number will be used.
userNameNumb = int(1)

userName = None

#The username's length will be needed in order to add the numbers incase of a tie.
userNameLength = 'void'

lineLength = 'void'

#The variable that will contain a random integer (between 1-9) for the password.
randomNumber = None

#The variable that will be a sequence of 4 random numbers for the password.
randomSeq = None


for line in OpenedDataFile:
    #Store the length of the line so that we have the position of the final spot in the line (excluding spaces)
    lineLength = len(line.strip())
    #If the line is the header
    if line.startswith('Firstname'):
        final.write(line[:line.find('hire_date,') + 10] + ' username, password')
        final.write('\n')
        continue
    #Store the first letter of the employee's first name to use in the username. 
    if counterOfCommas is 0:
        startFName = line[0]
        endFName= line.find(',')
        counterOfCommas = counterOfCommas + 1
    #Save the last name of the employee to use in the username.
    if counterOfCommas is 1:
        startLName = endFName + 1
        endLName = line.find(',',endFName + 1)
        counterOfCommas = counterOfCommas + 1
        userName = startFName + line[startLName:endLName]
        userNameLength = len(userName)
    #Creating the username. If the first letter of first name + last name is already taken
    #by an employee, add the number 1. If that username is taken, try with 2 and repeat until a new username is found.
    if counterOfCommas is 2:
        for employeesFound in listOfUsernames:
            if not listOfUsernames:
                break
            if userName != employeesFound:
                continue
            if userName == employeesFound:
               userName = userName[:userNameLength]
               userName = userName + str(userNameNumb)
               userNameNumb = int(userNameNumb) + int(1)
        listOfUsernames.append(userName)
        counterOfCommas = counterOfCommas + 1
    if counterOfCommas is 3:
        endOfEmpNumb = line.find(',',endLName + 1)
        counterOfCommas = counterOfCommas + 1
    if counterOfCommas is 4:
        endOfGender = line.find(',',endOfEmpNumb + 1)
        counterOfCommas = counterOfCommas + 1
    if counterOfCommas is 5:
        endOfHireDate = line.find(',',endOfGender + 1)
        counterOfCommas = counterOfCommas + 1
    #Save the employee's title and attact 4 random numbers to it to make their password.
    if counterOfCommas is 6:
        empTitle = line[endOfHireDate + 1: lineLength]
        for i in range(4):
            randomNumber = random.randint(1,9)
            if randomSeq is not None:
                randomSeq = str(randomSeq) + str(randomNumber)
            if randomSeq is None:
                randomSeq = randomNumber
        passWord = randomSeq + empTitle
        randomSeq = None
    #Create the line in the file for each employee.
    final.write(line[:endOfHireDate] + ',' + userName + ',' + passWord)
    final.write('\n')
    #Reset variables for the next employee.
    counterOfCommas = 0
    userNameNumb = 1
