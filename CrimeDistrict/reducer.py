sortedFile = open("reduced.txt","r")   
reducedFile = open("reducedData.txt", "w")   

thisKey = ""
thisValue = 0
count = 0
minimum=0
maximum=0
maxDistrict=""
minDistrict=""
#for loop iterates the sorted file and takes out the district,crimes out of it and separates them with tab space
for line in sortedFile:
    data = line.strip().split('\t')
    district, crimes = data
    if district != thisKey:
        if thisKey !="" and thisKey:
            #reducedFile.write(thisKey + '\t' + str(minimum)+'\t' + str(maximum)+'\n')
            count = count + 1
        thisKey = district
        thisValue = 0
        minValue=0
        maxValue=0
    # Comparing each of the crimes with previous value if it is greater then the maximum value is set the present value
    # And also the district is stored into the string
    if(crimes>maximum):
        maximum=crimes
        maxDistrict=district
    # In the below step we are initializing the minimum value for the first time with one of the values in the records
    # Since minimum value cannot be initialized to zero for comparision purpose
    if count == 0:
        minimum = crimes
    # After initializing the minimum value we start comparing the present values with the minimum value
    # and if it less than the previous value then minimum value is assigned with present value
    elif (crimes<minimum):
        minimum=crimes
        minDistrict=district
print 'Minimum number of crimes are found in '+minDistrict+' district with a count of '+str(minimum)+' crimes'
print 'Maximum number of crimes are found in '+maxDistrict+' district with a count of '+str(maximum)+' crimes'
reducedFile.write(minDistrict + '\t' + str(minimum)+'\n')
reducedFile.write(maxDistrict + '\t' + str(maximum)+'\n')


sortedFile.close()
reducedFile.close()






