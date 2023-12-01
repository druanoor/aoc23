sum = 0
import re

with open("input.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        print(line.rstrip())
        firstNumber = -1
        lastNumber = -1
        for character in line:
            numberFound = re.match('[0-9]', character)
            if numberFound:
                if firstNumber == -1:
                    firstNumber = int(character) 
                else:
                    lastNumber = int(character)
        
        if lastNumber == -1:
            lastNumber = firstNumber
        calibrationValue = (firstNumber * 10) + lastNumber
        print(calibrationValue)
        sum = sum + calibrationValue
        print(sum)


print(sum)


                


