sortedFile = open("reduced.txt","r")   
reducedFile = open("reducedData.txt", "w")   

thisKey = ""
thisValue = 0
values = []
value = []
valuesnums = []
stri = " "
#for loop iterates the sorted file and takes out the district,crimes out of it and separates them with tab space
for line in sortedFile:
    data = line.strip().split('\t')
    #print data
    district, crimes = data
    if district != thisKey:
        if thisKey !="":
            reducedFile.write(thisKey + '\t' + str(thisValue)+'\n')

        thisKey = district
        thisValue = 0
    # valuesnums.append(district+" "+str(crimes))
    values.append(crimes)
    value.append(district+": "+str(crimes))
    # print values
minimum=min(values)
maximum=max(values)

# print "min number of crimes: "+minimum
# print "max number of crimes: "+maximum
#For loop checks the value range based on maximum and minimum
for x in range(len(value)):
    # print value[x]
    if value[x].endswith(minimum):
        print "Minimum number of crimes in the district "+value[x]
    if value[x].endswith(maximum):
        print "Maximum number of crimes in the district "+value[x]

sortedFile.close()
reducedFile.close()






