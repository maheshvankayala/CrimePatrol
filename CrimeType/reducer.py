sortedFile = open("sortedData.txt","r")   
reducedFile = open("reducedData.txt", "w")   

oldKey = None
crimeTotal = 0


for line in sortedFile:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) !=2:
        continue
    #print data
    thisKey, thisValue = data_mapped
    if oldKey and oldKey != thisKey:
        reducedFile.write(oldKey + "\t" + str(crimeTotal) + "\n")
        oldKey= thisKey;
        crimeTotal = 0
    oldKey = thisKey
    crimeTotal += int(thisValue)
if oldKey != None:
    reducedFile.write(oldKey + "/t" + str(crimeTotal))

sortedFile.close()
reducedFile.close()