filereader = open('crimeweaponsdata.txt','r')
filewriter = open('keyvalueoutput.txt','w')

for input in filereader:
    line = input.strip().split(',')
    if (len(line) == 15):    
       crime_date,crime_time,crime_code,location,description,inside_outside,weapon,post,district,neighborhood,longitude,latitude,location,premise,total_incidents = line
       filewriter.write(weapon + "\t" + total_incidents +"\n")

filereader.close()
filewriter.close()