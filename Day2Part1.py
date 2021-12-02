file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2021\Day2.txt", "r")

directions = []
#Create a list with alternating direction and distance
for line in file:
    temp = line.split()
    directions.append(temp[0])
    directions.append(temp[1])

horizontalPosition = 0
depth = 0
for i in range(0,len(directions),2):
    match directions[i]:
        case 'forward':
            horizontalPosition += int(directions[i+1])
        case 'down':
            depth += int(directions[i+1])
        case 'up':
            depth -= int(directions[i+1])

solution = horizontalPosition * depth

print(solution)
    

file.close()
