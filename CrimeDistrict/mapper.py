f = open('crimedata.txt','r') #Opening crimedata.txt in read mode and storing it in file f
o = open('output.txt','w') #Opening output.txt in write mode and storing it in file o

for data in f:
    input = data.strip().split(',') #Striping the data and splitting the data columns with comma(,) separated
    if (len(input) == 15):    
       crimeDate,crimeTime,crimeCode,location,description,inside_outside,weapon,post,district,neighborhood,longitude,latitude,location,premise,total_incidents = input
       o.write(district + "\t" + total_incidents +"\n") #From the data columns taking out the district and total_incidents and writing it into file o

f.close() #Closes file f
o.close() #Closes file o