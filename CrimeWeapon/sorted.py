inputFile = open("keyvalueoutput.txt","r") 
sortedFile = open("datasorted.txt", "w") 

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