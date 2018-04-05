f = open('crimedata.txt','r')
o = open('output.txt','w')

for data in f:
    input = data.strip().split(',')
    if (len(input) == 15):    
       crimeDate,crimeTime,crimeCode,location,description,inside_outside,weapon,post,district,neighborhood,longitude,latitude,location,premise,total_incidents = input
       o.write(district + "\t" + total_incidents +"\n")

f.close()
o.close()