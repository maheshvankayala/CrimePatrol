s = open("datasorted.txt","r")   
r = open("reducedfile.txt", "w")   

thisKey = ""
thisValue = 0
#for loop is used to iterate the lines in the file and store only 2 variables here he took weapons and incidents
for line in s:
    data = line.strip().split('\t')
    weapons, incidents = data
    if weapons != thisKey:# for each key value we calculated the count of it
        if thisKey:
            r.write(thisKey + '\t' + str(thisValue)+'\n')

        thisKey = weapons#initialising to default value
        thisValue = 0

    thisValue += int(incidents)

r.write(thisKey + '\t' + str(thisValue)+'\n')#to write the values to reducedfile.txt

s.close()
r.close()





