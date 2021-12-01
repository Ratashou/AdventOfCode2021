file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2021\Day1.txt", "r")

depths = []
for line in file:
    depths.append(line)
    
count = 0
previousSum = False

for i in range(len(depths)):
    if i == (len(depths) - 2):
        break
    currentSum = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
    if previousSum != False and currentSum > previousSum:
        count += 1
    previousSum = currentSum

print(count)
file.close()
    
