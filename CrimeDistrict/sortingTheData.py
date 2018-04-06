inputFile = open("output.txt","r") 
sortedFile = open("sortedData.txt", "w") 

lines = inputFile.readlines()
lines.sort()

for line in lines:
    data = line.strip().split('\t')
    if len(data) != 2:  
        continue
    else:
	    sortedFile.write(line)

inputFile.close()
sortedFile.close()
