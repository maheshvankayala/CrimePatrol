s = open("datasorted.txt","r")   
r = open("reducedfile.txt", "w")   

thisKey = ""
thisValue = 0

for line in s:
    data = line.strip().split('\t')
    weapons, incidents = data
    if weapons != thisKey:
        if thisKey:
            r.write(thisKey + '\t' + str(thisValue)+'\n')

        thisKey = weapons
        thisValue = 0

    thisValue += int(incidents)

r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()





