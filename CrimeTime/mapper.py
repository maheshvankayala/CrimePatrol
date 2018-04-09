f = open('nypd.txt','r')
o = open('mapoutput.txt','w')

for data in f:
    input = data.strip().split(',')
    if (len(input) == 24):
        CMPLNT_NUM, CMPLNT_FR_DT, CMPLNT_FR_TM, CMPLNT_TO_DT, CMPLNT_TO_TM, RPT_DT, KY_CD, OFNS_DESC, PD_CD, PD_DESC, CRM_ATPT_CPTD_CD, LAW_CAT_CD, JURIS_DESC, BORO_NM, ADDR_PCT_CD, LOC_OF_OCCUR_DESC, PREM_TYP_DESC, PARKS_NM, HADEVELOPT, X_COORD_CD, Y_COORD_CD, Latitude, Longitude, Lat_Lon = input
        for CMPLNT_FR_DT in input:
            dateIn = CMPLNT_FR_DT.strip().split('/')
            if(len(dateIn) == 3):
                MM, DD, YY = dateIn
                if (MM == "1"):
                    o.write("January" + "\t" + "1" + "\n")
                if (MM == "2"):
                    o.write("February" + "\t" + "1" + "\n")
                if (MM == "3"):
                    o.write("March" + "\t" + "1" + "\n")
                if (MM == "4"):
                    o.write("April" + "\t" + "1" + "\n")
                if (MM == "5"):
                    o.write("May" + "\t" + "1" + "\n")
                if (MM == "6"):
                    o.write("June" + "\t" + "1" + "\n")
                if (MM == "7"):
                    o.write("July" + "\t" + "1" + "\n")
                if (MM == "8"):
                    o.write("August" + "\t" + "1" + "\n")
                if (MM == "9"):
                    o.write("September" + "\t" + "1" + "\n")
                if (MM == "10"):
                    o.write("October" + "\t" + "1" + "\n")
                if (MM == "11"):
                    o.write("November" + "\t" + "1" + "\n")
                if (MM == "12"):
                    o.write("December" + "\t" + "1" + "\n")
                
                
                
        
f.close()
o.close()