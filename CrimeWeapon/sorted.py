inputFile = open("keyvalueoutput.txt","r") 
sortedFile = open("datasorted.txt", "w") 

lines = inputFile.readlines()
lines.sort()#here we read each line in file and sort them based on key values

for line in lines:
    data = line.strip().split('\t')
    if len(data) != 2:  
        continue
    else:
	    sortedFile.write(line)#we write sorted lines into datasorted.txt

inputFile.close()
sortedFile.close()