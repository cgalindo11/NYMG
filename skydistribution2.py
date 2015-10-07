
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import ascii


# TELLS PYTHON WE WILL BE USING THE CSV FILE

with open('membershipad.csv', 'rU') as file:

    with open ('nomembershipad.csv', 'rU') as filenm:
        
        # READS MEMBERSHIPADHIST.CSV FILE FOR OBJECTS WITH MEMBERSHIP
        reader = csv.reader(file)
        # READS MEMBERSHIPADHIST.CSV FILE FOR OBJECTS WITH NO MEMBERSHIP
        readernm = csv.reader(filenm)


        # THIS CREATES ARRAYS TO HOLD THE RA's FOR EACH OBJECT
        ratuc = []
        raab = []
        rabeta = []
        raargus = []
        racolum = []
        ratw = []
        ranone = []

        # SHORTCUT TO CHECK IN THE CSV FILE WHICH MOVING GROUP EACH OF THEM ARE IN (TO AVOID SCREWING UP)
        tuc = 'tucana'
        ab = 'abdora'
        beta = 'betapic'
        argus = 'argus'
        colum = 'columba'
        tw = 'twhydra'

        # THIS CREATES ARRAYS TO HOLD DECLINATIONS FOR EACH OBJECT
        dtuc = []
        dab = []
        dbeta = []
        dargus = []
        dcolum = []
        dtw = []
        dnone = []

# WHAT DOES THIS DO?        
        nametuc = []
        nameab = []
        namenone = []
        namebeta = []
        nameargus = []
        namecolum = []
        nametw = []
    

        # GOES THROUGH READERNM FILE LINE BY LINE
        for line in readernm:

            ranone.append(float(line[9]))        
            dnone.append(float(line[10]))         
            namenone.append(str(line[0]))
        # GOES THROUGH READER FILE LINE BY LINE    
        for line in reader:

            # MAKES A STRING TO CHECK WHAT 
            linecomp = line[24].strip()
            if linecomp == tuc:
                ratuc.append(float(line[9]))
                dtuc.append(float(line[10]))
                
            elif linecomp == ab:
                raab.append(float(line[9]))
                dab.append(float(line[10]))
                 
            elif linecomp == beta:
                rabeta.append(float(line[9]))
                dbeta.append(float(line[10]))
                 
            elif linecomp== argus:
                raargus.append(float(line[9]))
                dargus.append(float(line[10]))
                  
            elif linecomp == colum:
                racolum.append(float(line[9]))
                dcolum.append(float(line[10]))
                 
            elif linecomp == tw:
                ratw.append(float(line[9]))
                dtw.append(float(line[10]))
                  
              
    

ratuc = coord.Angle(ratuc*u.degree)
ratuc = ratuc.wrap_at(180*u.degree)
dtuc = coord.Angle(dtuc*u.degree)

raab = coord.Angle(raab*u.degree)
raab = raab.wrap_at(180*u.degree)
dab = coord.Angle(dab*u.degree)

ranone = coord.Angle(ranone*u.degree)
ranone = ranone.wrap_at(180*u.degree)
dnone = coord.Angle(dnone*u.degree)

rabeta = coord.Angle(rabeta*u.degree)
rabeta = rabeta.wrap_at(180*u.degree)
dbeta = coord.Angle(dbeta*u.degree)

raargus = coord.Angle(raargus*u.degree)
raargus = raargus.wrap_at(180*u.degree)
dargus = coord.Angle(dargus*u.degree)

racolum = coord.Angle(racolum*u.degree)
racolum = racolum.wrap_at(180*u.degree)
dcolum = coord.Angle(dcolum*u.degree)

ratw = coord.Angle(ratw*u.degree)
ratw = ratw.wrap_at(180*u.degree)
dtw = coord.Angle(dtw*u.degree)


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="hammer")

ax.scatter(ratuc.radian, dtuc.radian, c = "b", label = "Tuc-Hor")
ax.scatter(raab.radian,dab.radian, c = "g", label = "AB Doradus")
ax.scatter(ranone.radian,dnone.radian, c = ".96", label = "None")
ax.scatter(rabeta.radian,dbeta.radian, c = "y", label = "Beta Pictorus")
ax.scatter(raargus.radian,dargus.radian, c = "c", label = "Argus")
ax.scatter(racolum.radian,dcolum.radian, c = "m", label = "Columba")
ax.scatter(ratw.radian,dtw.radian, c = "r", label = "TW Hya")

ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1.25), loc = 1, borderaxespad=0., prop={'size': 7})
fig.savefig("map.pdf")

