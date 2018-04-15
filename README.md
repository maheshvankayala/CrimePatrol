# 1.Team name - Crime Patrol
Course Number: 44-564
### Project Group 2F

     Karunakar Reddy Katasani(s530472@nwmissouri.edu)
     Course: MS-ACS
     Semester:02

     Naga Sai Meghana Mayaluri(s530475@nwmissouri.edu)
     Course: MS-ACS
     Semester:02

     Nagateja Seetharama Srinivas Prakash Pakala(s530715@nwmissouri.edu)
     Course: MS-ACS
     Semester:02

     Venkata Naga Mahesh Kumar Vankayala(s528870@nwmissouri.edu)
     Course: MS-ACS
     Semester:04
### Project Pair 2-11

     Karunakar Reddy Katasani
     Naga Sai Meghana Mayaluri

### Project Pair 2-12

     Nagateja Seetharama Srinivas Prakash Pakala
     Venkata Naga Mahesh Kumar Vankayala

### 2. Link to the public repository
     https://github.com/maheshvankayala/CrimePatrol

#### Issues
     1. https://github.com/maheshvankayala/CrimePatrol/issues/1
     2. https://github.com/maheshvankayala/CrimePatrol/issues/2
     3. https://github.com/maheshvankayala/CrimePatrol/issues/3
     4. https://github.com/maheshvankayala/CrimePatrol/issues/4  


**3. Introduction**
    The project mainly focuses on crimes took over in 2 cities new york and baltimore.
    The structured data provides the time of a particular time occured at a particular location, type of weapon used,
    type of crime the location provides latitude and longitude and also provides the district where the crime took place.

### 4. Dataset 1(Pair 2-11)
        Crime in Baltimore:
        Dataset size: 40MB
        Values: 276530 Rows
        File type: Excel
        Format: Structured

#### DataSet 2(Pair 2-12)
        NewYork City Crimes:
        Dataset Size: 250MB
        Values: 1048576 Rows
        File type: Excel
        Format: Structured

### 5.Link for the dataset
    Link for dataset1 (Crime in Baltimore)- https://www.kaggle.com/sohier/crime-in-baltimore
    Link for dataset2 (Newyork City Crimes)- https://www.kaggle.com/adamschroeder/crimes-new-york-city/version/1#_=_

### 6. Big data Qualifications
    VOLUME: The size of our data set is 253.42 MB,40 MB.
    VARIETY: The data set used for the project is structured data.
    VELOCITY: Since we are using data at rest the velocity is 0.
    VERACITY: The data set is cleaned data and the data is taken from trustworthy sources.
    VALUE: Looking with the criminal data we can improve police protection at required spots, times in cities.

### 7. Big data Questions
    For each district, what is the highest count of crimes that took place?- Karunakar Reddy Katasani
    For each type of crime, which took place the most? - Venkata Naga Mahesh Kumar Vankayala
    For each crime, at what time the most crimes took place? - Nagateja Seetharama Srinivas Prakash Pakala
    For each crime, which weapon is used most in the crime? -  Naga Sai Meghana Mayaluri

### 8. Big data Solutions  
**Crime District(Karunakar Reddy Katasani)**  
        **1.Mapper Input**-9/2/2017 23:30:00 3JK 4200 AUDREY AVE,ROBBERY - RESIDENCE I KNIFE 913 SOUTHERN Brooklyn -76.60541 39.22951 (39.2295100000, -76.6054100000) ROW/TOWNHO 1  
        **2.Mapper Output**-9/2/2017,23:30:00,3JK,4200 AUDREY AVE,ROBBERY,RESIDENCE,I,KNIFE,913,SOUTHERN,Brooklyn,-76.60541,39.22951,(39.2295100000, -76.6054100000),ROW/TOWNHO,1  
        **3.Reducer output**-SOUTHERN,1  
        **4.Language**- Python  
        **5.Kind of Chart**- Bar Graph 
       ![screenshot 240](https://user-images.githubusercontent.com/31742996/38780308-2dc19e58-409a-11e8-9d73-14e776ea79e7.png)
        **Mapper output screenshot:**
         ![screenshot 237](https://user-images.githubusercontent.com/31742996/38780254-2d51073e-4099-11e8-8f61-829d40950009.png)
        **Reducer output screenshot:**
        ![screenshot 238](https://user-images.githubusercontent.com/31742996/38780313-45fc9374-409a-11e8-99e1-49c947f5c17e.png)
**Crime Weapon(Naga Sai Meghana Mayaluri)**  
        **1.Mapper Input**-9/2/2017 23:30:00 3JK 4200 AUDREY AVE,ROBBERY - RESIDENCE I KNIFE 913 SOUTHERN Brooklyn -76.60541 39.22951 (39.2295100000, -76.6054100000) ROW/TOWNHO 1  
        **2.Mapper Output**-9/2/2017,23:30:00,3JK,4200 AUDREY AVE,ROBBERY,RESIDENCE,I,KNIFE,913,SOUTHERN,Brooklyn,-76.60541,39.22951,(39.2295100000, -76.6054100000),ROW/TOWNHO,1  
        **3.Reducer output**-Knife,1  
        **4.Language**- Python  
        **5.Kind of Chart**-Sorted Bar Chart 
        ![screenshot 146](https://user-images.githubusercontent.com/31742996/38780388-0d402fc2-409b-11e8-9003-df9855dbb6ec.png)
        **Mapper output screenshot:**
        ![screenshot 142](https://user-images.githubusercontent.com/31742996/38780393-21169f0e-409b-11e8-8ae2-9cd0b0fade91.png)
        **Reducer output screenshot:**
        ![screenshot 143](https://user-images.githubusercontent.com/31742996/38780398-321e3f50-409b-11e8-9e49-ea0bba6d6960.png)

**Crime Time(Nagateja Seetharama Srinivas Prakash Pakala)**  
        **1.Mapper Input**-9/2/2017 23:30:00 3JK 4200 AUDREY AVE,ROBBERY - RESIDENCE I KNIFE 913 SOUTHERN Brooklyn -76.60541 39.22951 (39.2295100000, -76.6054100000) ROW/TOWNHO 1  
        **2.Mapper Output**-9/2/2017,23:30:00,3JK,4200 AUDREY AVE,ROBBERY,RESIDENCE,I,KNIFE,913,SOUTHERN,Brooklyn,-76.60541,39.22951,(39.2295100000, -76.6054100000),ROW/TOWNHO,1  
        **3.Reducer output**-23:30:00,1  
        **4.Language**-Python  
         **5.Kind of Chart**-Sorted Bar Chart
         [Pakala_Output.xlsx](https://github.com/maheshvankayala/CrimePatrol/files/1913499/Pakala_Output.xlsx)
         **Mapper output screenshot:**
         ![pakala_mapperoutput](https://user-images.githubusercontent.com/31742996/38784604-df20c25c-40d9-11e8-8899-725dfb52ad8c.png)
         **Reducer output screenshot:**
         ![pakala_reduceroutput](https://user-images.githubusercontent.com/31742996/38784609-f03f21dc-40d9-11e8-9081-cd2c25ace6c2.png)
         
**Crime Type(Venkata Naga Mahesh Kumar Vankayala)**  
        **1.Mapper Input**-9/2/2017 23:30:00 3JK 4200 AUDREY AVE,ROBBERY - RESIDENCE I KNIFE 913 SOUTHERN Brooklyn -76.60541 39.22951 (39.2295100000, -76.6054100000) ROW/TOWNHO 1  
        **2.Mapper Output**-9/2/2017,23:30:00,3JK,4200 AUDREY AVE,ROBBERY,RESIDENCE,I,KNIFE,913,SOUTHERN,Brooklyn,-76.60541,39.22951,(39.2295100000, -76.6054100000),ROW/TOWNHO,1  
        **3.Reducer output**-ROBBERY,1  
        **4.Language**-Python  
        **5.Kind of Chart**-Pie Chart 
        [Vankayala_Output.xlsx](https://github.com/maheshvankayala/CrimePatrol/files/1913501/Vankayala_Output.xlsx)
        **Mapper output screenshot:**
        ![vankayala_mapperoutput](https://user-images.githubusercontent.com/31742996/38784626-3f2d0d0e-40da-11e8-9437-657d5ff0f00a.png)
        **Reducer output screenshot:**
        ![vankayala_reduceroutput](https://user-images.githubusercontent.com/31742996/38784631-469d837a-40da-11e8-8d22-902fc581c975.png)
