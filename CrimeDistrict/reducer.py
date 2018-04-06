sortedFile = open("reduced.txt","r")   
reducedFile = open("reducedData.txt", "w")   

thisKey = ""
thisValue = 0
values = []
valuesnums = []
stri = " "

for line in sortedFile:
    data = line.strip().split('\t')
    #print data
    district, crimes = data
    if district != thisKey:
        if thisKey:
            reducedFile.write(thisKey + '\t' + str(thisValue)+'\n')

        thisKey = district
        thisValue = 0
    # valuesnums.append(district+" "+str(crimes))
    values.append(crimes)
    # print values
minimum=min(values)
maximum=max(values)

print "min number of crimes: "+minimum
print "max number of crimes: "+maximum

sortedFile.close()
reducedFile.close()






