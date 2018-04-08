filereader = open('crimeweaponsdata.txt','r')#opened crimeweaponsdata to read
filewriter = open('keyvalueoutput.txt','w')#opened keyvalueoutput to write key value pairs

for input in filereader:
    line = input.strip().split(',')#we split the input with the comma seperator
    if (len(line) == 15):    
       crime_date,crime_time,crime_code,location,description,inside_outside,weapon,post,district,neighborhood,longitude,latitude,location,premise,total_incidents = line
       #Here we write the weapon and incidents into the file
       filewriter.write(weapon + "\t" + total_incidents +"\n")#write the values to the file

filereader.close()#closing the opened file which is in read mode
filewriter.close()#closing the opened file which is in write mode