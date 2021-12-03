file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2021\Day3.txt", "r")

#Create a list of the input data
diagnostics = []
for line in file:
    diagnostics.append(line)

gammaRate = ''
epsilonRate = ''
#Loop through each column
for i in range(0,(len(diagnostics[0]) - 1)):
    oneCounter = 0
    zeroCounter = 0
    #Loop through each line/row counting 1s and zeros in the designated column
    for line in diagnostics:
        if line[i] == '1':
            oneCounter += 1
        elif line[i] == '0':
            zeroCounter += 1

    if oneCounter > zeroCounter:
        gammaRate += '1'
        epsilonRate += '0'
    elif zeroCounter > oneCounter:
        gammaRate += '0'
        epsilonRate += '1'

#Convert from binary to decimal
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)

print(gammaRate * epsilonRate)

file.close()
