sortedFile = open("sortedData.txt","r")   
reducedFile = open("reduced.txt", "w")   

thisKey = ""
thisValue = 0
calculatedValue = []
minValue=0
maxValue=0

for line in sortedFile:
    data = line.strip().split('\t')
    # print data
    district, crimes = data
    if district != thisKey:
        if thisKey:
            reducedFile.write(thisKey + '\t' + str(thisValue)+'\n')

        thisKey = district
        thisValue = 0

    thisValue += int(crimes)

reducedFile.write(thisKey + '\t' + str(thisValue)+'\n')

sortedFile.close()
reducedFile.close()