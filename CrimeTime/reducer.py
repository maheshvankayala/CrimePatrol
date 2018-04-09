sortedFile = open("sortedData.txt","r")   
reducedFile = open("reducedData.txt", "w")   

oldKey = None
countTotal = 0


for line in sortedFile:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) !=2:
        continue
    #print data
    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
        reducedFile.write(oldKey + "\t" + str(countTotal) + "\n")
        oldKey= thisKey;
        countTotal = 0
    oldKey = thisKey
    countTotal += int(thisValue)
if oldKey != None:
    reducedFile.write(oldKey + "/t" + str(countTotal) +"\n")

sortedFile.close()
reducedFile.close()