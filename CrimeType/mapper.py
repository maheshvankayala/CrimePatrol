f = open('nypd.txt','r')
o = open('mapoutput.txt','w')

for data in f:
    input = data.strip().split(',')
    if (len(input) == 24):
        CMPLNT_NUM, CMPLNT_FR_DT, CMPLNT_FR_TM, CMPLNT_TO_DT, CMPLNT_TO_TM, RPT_DT, KY_CD, OFNS_DESC, PD_CD, PD_DESC, CRM_ATPT_CPTD_CD, LAW_CAT_CD, JURIS_DESC, BORO_NM, ADDR_PCT_CD, LOC_OF_OCCUR_DESC, PREM_TYP_DESC, PARKS_NM, HADEVELOPT, X_COORD_CD, Y_COORD_CD, Latitude, Longitude, Lat_Lon = input
        o.write( OFNS_DESC +"\t" + "1\n")
        
f.close()
o.close()