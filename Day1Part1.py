file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2021\Day1.txt", "r")

previous = False
count = 0
for line in file:
    current = int(line)
    if previous != False and current > previous:
        count += 1
    previous = current

print(count)

file.close()
