#Will need to import random to use the random integer function.
import random
#Open the employee file.
OpenedDataFile = open('employees1000.csv')
#What the new csv file will be called.
finalFile = input('What do you want to call the file? ')
final = open(finalFile,'w+')


#Variables
#A list containing all usernames that have been used
listOfUsernames = list()
#A counter that keeps track of the number of commas that have been pasted in a line
counterOfCommas = 0
#The number that may be added to the username if the username consisting of one's first letter of their
#first name and last name is already in use
userNameNumb = int(0)
#The variable that will contain the username
userName = None
#The variable that will contain the length of the given username
userNameLength = 'void'
#The variable that will contain the length of the given line
lineLength = 'void'
#The variable that will contain a random integer between 1 and 9
randomNumber = None
#The variable that will be a sequence of 4 random numbers
randomSeq = None

#Step through each line in the original file
for line in OpenedDataFile:
    #Keep the length of the line without the spaces to the right of it
    lineLength = len(line.strip())
    #If the line is the header, use it's information to build the header of our new file
    if line.startswith('Firstname'):
        final.write(line[:line.find('hire_date,') + 10] + ' username, password')
        final.write('\n')
        continue
    #If a comma has not been passed, then this is the first name of the employee. Store the first letter.
    if counterOfCommas is 0:
        startFName = line[0]
        endFName= line.find(',')
        counterOfCommas = counterOfCommas + 1
    #If 1 comma has been passed, store the following text as the last name up until the next comma.
    if counterOfCommas is 1:
        startLName = endFName + 1
        endLName = line.find(',',endFName + 1)
        counterOfCommas = counterOfCommas + 1
        userName = startFName + line[startLName:endLName]
        userNameLength = len(userName)
    #If 2 commas have been passed, create a username for the employee. If the first letter of first name + last name is already taken
    #by an employee, add the number 0. If that username is taken, try with 1 ... ect.
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
    #If 3 commas have been passed, take note of your position, but the employee number is not important for this program.
    if counterOfCommas is 3:
        endOfEmpNumb = line.find(',',endLName + 1)
        counterOfCommas = counterOfCommas + 1
    #If 4 commas have been passed, take note of your position, but the gender of the employee is not important for this program.
    if counterOfCommas is 4:
        endOfGender = line.find(',',endOfEmpNumb + 1)
        counterOfCommas = counterOfCommas + 1
    #If 5 commas have been passed, take note of your position, but the hiredate is not important for this program.
    if counterOfCommas is 5:
        endOfHireDate = line.find(',',endOfGender + 1)
        counterOfCommas = counterOfCommas + 1
    #If 6 commas have been passed, save the employee's title as a variable. Then add a seqeuence of 4 random numbers to it and Make
    #this your password.
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
    #Create the line for the employee, with their Firstname, Lastname, Employee Number, Gender, Hiredate, Username, and Password.
    final.write(line[:endOfHireDate] + ',' + userName + ',' + passWord)
    final.write('\n')
    #Reset variables for the next employee.
    counterOfCommas = 0
    userNameNumb = 0
