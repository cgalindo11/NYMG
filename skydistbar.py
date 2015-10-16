
import csv
import sqlite3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import ascii
from math import floor
from matplotlib.colors import Normalize


# TELLS PYTHON WE WILL BE USING THE CSV FILE

with open('groupcbar.csv', 'rU') as file:

    with open ('nogroupcbar1.csv', 'rU') as filenm:
        
        # READS MEMBERSHIPADHIST.CSV FILE FOR OBJECTS WITH MEMBERSHIP
        reader = csv.reader(file)
        # READS MEMBERSHIPADHIST.CSV FILE FOR OBJECTS WITH NO MEMBERSHIP
        readernm = csv.reader(filenm)
        # TELLS PYTHON WE WILL BE USING THE BDNYC DATABASE
        conn = sqlite3.connect('BDNYC.db')
        # MAKES SHORTCUT FOR ENTERING SQL COMMANDS
        c = conn.cursor() 
        
        # THIS CREATES ARRAYS TO HOLD THE IDS FOR EACH OBJECT
        sidtuc = []
        sidab = []
        sidnone = []
        sidbeta = []
        sidargus = []
        sidcolum = []
        sidtw = []

        # THIS CREATES ARRAYS TO HOLD THE RA's FOR EACH OBJECT
        ratuc = []
        raab = []
        rabeta = []
        raargus = []
        racolum = []
        ratw = []
        ranone = []

        # SHORTCUT TO CHECK IN THE CSV FILE WHICH MOVING GROUP EACH OF THEM ARE IN (TO AVOID SCREWING UP)
        tuc = 'Tuc-Hor'
        ab = 'AB Dor'
        nostar = 'None'
        beta = 'beta Pic'
        argus = 'Argus'
        colum = 'Columba'
        tw = 'TW Hya'

        # THIS CREATES ARRAYS TO HOLD DECLINATIONS FOR EACH OBJECT
        dtuc = []
        dab = []
        dbeta = []
        dargus = []
        dcolum = []
        dtw = []
        dnone = []

        # THIS RECORDS NAME(SHORTNAME, LONGNAME, ETC) OF EACH OBJECT        
        nametuc = []
        nameab = []
        namenone = []
        namebeta = []
        nameargus = []
        namecolum = []
        nametw = []

         # THIS CREATES ARRAYS TO HOLD SPECTRAL TYPES FOR EACH MOVING GROUP
        spectuc = []
        specab = []
        specnone = []
        specbeta = []
        specargus = []
        speccolum = []
        spectw = []

        # THIS CREATES ARRAY TO RECORD OBJECTS WITH NO ADOPTED SPECTRAL TYPES
        noadoptuc = []
        noadopab = []
        noadopnone = []
        noadopbeta = []
        noadopargus = []
        noadopcolum = []
        noadoptw = []

        # THIS SECTION EXTRACTS THE SPECTRAL TYPES
        
        ##########################################
        
        # GOES THROUGH READERNM FILE LINE BY LINE
        
        for line in readernm:
            # THIS GETS OBJECTS THAT HAVE SHORTNAME WITH 9 CHARACTERS. STRIP IGNORES ANY BLANK SPACES IN FRONT OR AFTER THE SHORTNAME
            if len(line[0].strip()) == 9:
                # IF SHORTNAME IS 9 CHARACTERS LONG IT GETS STORED IN t
                t = (line[0].strip(),)

                # MATCHES SHORTNAME TO ID IN THE DATABASE IN THE SOURCES TABLE
                for row in c.execute('SELECT * FROM sources WHERE shortname=?',t):
                    # STORES THE ID IN SIDNONE ARRAY
                    sidnone.append(row[0])

            # THIS GETS THE OBJECTS WITH NAMES THAT ARE NOT SHORTNAMES (SUCH AS TWA 27). >1 JUST MEANS THAT WE IGNORE CELLS WITH NOTHING IN THEM
            ### WARNING: ONE OBJECT IS SKIPPED.  J01231125-6921379 HAS NO SPECTRAL TYPE ###
            elif len(line[0].strip())>1:
                # WHEN IT FINDS AN OBJECT THAT MATCHES THE CRITERIA, IT GETS STORED IN t. THE % ALLOWS US TO IGNORE THE REST OF THE NAME IF NECESSARY
                t = ('%' + line[0].strip()+'%',)

                # MATCHES NAME TO ID IN THE DATABASE IN THE SOURCES TABLE
                for row in c.execute('SELECT * FROM sources WHERE names LIKE ?',t):
                    # STORES THE ID IN SIDNONE ARRAY
                    sidnone.append(row[0])

       
        # GOES THROUGH READER FILE LINE BY LINE
        for line in reader:
            # THIS GETS OBJECTS THAT HAVE SHORTNAME WITH 9 CHARACTERS
            if len(line[0].strip()) == 9:
                t= (line[0].strip(),)

                # MATCHES SHORTNAME TO ID IN THE DATABASE IN THE SOURCES TABLE
                for row in c.execute('SELECT * FROM sources WHERE shortname=?',t):
                    # MAKES A STRING TO CHECK WHAT GROUP EACH OBJECT BELONGS TO
                    linecomp = line[47].strip()
                    # IF THE OBJECT MATCHES THE GROUP IT GETS WRITTEN IN THE SIDTUC ARRAY OR ANY OF THE OTHER ONES THAT MATCH
                    if linecomp == tuc:
                        sidtuc.append(row[0])
                    elif linecomp == ab:
                        sidab.append(row[0])
                    elif linecomp == nostar:
                        sidnone.append(row[0])
                    elif linecomp == beta:
                        sidbeta.append(row[0])
                    elif linecomp== argus:
                        sidargus.append(row[0])
                    elif linecomp == colum:
                        sidcolum.append(row[0])
                    elif linecomp == tw:
                        sidtw.append(row[0])



            # THIS WILL DO THE SAME AS ABOVE FOR OBJECTS WITH NO SHORTNAME, SUCH AS TWA 27. 
            elif len(line[0].strip()) > 1:
                # THIS DEFINES t AS THE SHORTNAME GIVEN IN THE FIRST COLUMN OF THE CSV FILE.
                t = ('%'+line[0].strip()+'%',)
                # MATCHES SHORTNAME TO ID IN THE DATABASE IN THE SOURCES TABLE
                for row in c.execute('SELECT * FROM sources WHERE names LIKE ?', t):
                    # MAKES A STRING TO CHECK WHAT GROUP EACH OBJECT BELONGS TO
                    linecomp = line[47].strip()
                    # IF THE OBJECT MATCHES THE GROUP IT GETS WRITTEN IN THE SIDTUC ARRAY OR ANY OF THE OTHER ONES THAT MATCH
                    if linecomp == tuc:
                        sidtuc.append(row[0])
                    elif linecomp == ab:
                        sidab.append(row[0])
                    elif linecomp == nostar:
                        sidnone.append(row[0])
                    elif linecomp == beta:
                        sidbeta.append(row[0])
                    elif linecomp== argus:
                        sidargus.append(row[0])
                    elif linecomp == colum:
                        sidcolum.append(row[0])
                    elif linecomp == tw:
                        sidtw.append(row[0])

        x = 0
        # GOES THROUGH EVERY OBJECT IN SIDTUC
        for s in sidtuc:
            # t STORES EACH ID
            t=(s,)
            # GOES BACK TO DATABASE IN THE SPRECTRAL TYPES TABLE AND PULLS THE SPECTRAL TYPE FOR THAT OBJECT
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                # COUNTS HOW MANY DIFFERENT SPECTRAL TYPES THERE ARE FOR A GIVEN SOURCE ID
                x = x+1
            # IF THERE IS MORE THAN ONE SPECTRAL TYPE    
            if x > 1:
                y = 0
                # USE THE ONE THAT HAS ADOPTED = 1
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                    y = y+1
                if y ==0:
                    noadoptuc.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            spectuc.append(floor(row[2]))
            # IF THERE IS JUST ONE SPECTRAL TYPE, USE THAT
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
              # NEED TO FIND OUT WHY I DID THIS                
                    if not isinstance(row[2], basestring):
                    # STORES THE SPECTRAL TYPES IN THIS ARRAY
                        spectuc.append(floor(row[2]))

            x = 0

        for s in sidab:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                x = x+1
            if x > 1:
                y = 0
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                    y = y+1
                if y == 0:
                    noadopab.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            specab.append(floor(row[2]))
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
                    if not isinstance(row[2], basestring):
                        specab.append(floor(row[2]))

            x = 0


        for s in sidnone:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                x = x+1
            if x > 1:
                y = 0
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                    y = y+1
                if y == 0:
                    noadopnone.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            specnone.append(floor(row[2]))
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
                    if not isinstance(row[2], basestring):
                        specnone.append(floor(row[2]))

            x = 0            

            
        for s in sidbeta:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                x = x+1
            if x > 1:
                y = 0
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                     y = y+1
                if y == 0:
                    noadopbeta.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            specbeta.append(floor(row[2]))
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
                    if not isinstance(row[2], basestring):
                        specbeta.append(floor(row[2]))

            x = 0                


        for s in sidargus:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                x = x+1
            if x > 1:
                y = 0
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                     y = y+1
                if y == 0:
                    noadopargus.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            specargus.append(floor(row[2]))
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
                    if not isinstance(row[2], basestring):
                        specargus.append(floor(row[2]))

            x = 0


        for s in sidcolum:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                x = x+1
            if x > 1:
                y = 0
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                     y = y+1
                if y == 0:
                    noadopcolum.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            speccolum.append(floor(row[2]))
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
                    if not isinstance(row[2], basestring):
                        speccolum.append(floor(row[2]))

            x = 0

        for s in sidtw:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                x = x+1
            if x > 1:
                y = 0
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                     y = y+1
                if y == 0:
                    noadoptw.append(row[1])
                else:
                    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =? AND adopted = 1',t):
                        if not isinstance(row[2], basestring):
                            spectw.append(floor(row[2]))
            else:
                for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?',t):
                    if not isinstance(row[2], basestring):
                        spectw.append(floor(row[2]))

            x = 0

        

        # STOPS USING BDNYC DATABASE
        conn.close()

        
        ###########################################
        
        # THAT SECTION EXTRACTED THE SPECTRAL TYPES
    
        # THIS SECTION WILL EXTRACT THE RIGHT ASCENSION AND DECLINATION FROM THE CSV FILES

        ###########################################
        
        # GOES THROUGH READERNM FILE LINE BY LINE

        # THESE TWO LINES RESET PYTHON'S POSITION IN THE CSV FILES, SO IT CAN READ THEM AGAIN FROM THE BEGINNING
        file.seek(0,0)
        filenm.seek(0,0)
        
        for line in readernm:

            ranone.append(float(line[9]))        
            dnone.append(float(line[10]))         
            namenone.append(str(line[0]))
        # GOES THROUGH READER FILE LINE BY LINE    
        for line in reader:

# MAKES A STRING TO CHECK WHAT 
            linecomp = line[47].strip()

            ### WARNING: ONE OBJECT IN TUCANA HAS NO SPECTRAL TYPE IN BDNYC. WE MANUALLY SKIP IT HERE
            if (linecomp == tuc  and "J" not in line[0]):
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
                  
         ######################################

         #THAT SECTION EXTRACTED THE RIGHT ASCENSIONS AND DECLINATIONS

### TEST SECTION ###
# THE NUMBER SHOWN IS THE SOURCE ID 
print ("Objects in AB Doradus with ambiguous spectral type:", noadopab)
print ("Objects with no group with ambiguous spectral type:", noadopnone)
print ("Objects in Tuc-Hor with ambiguous spectral type:", noadoptuc)
print ("Objects in Beta-Pic with ambiguous spectral type:", noadopbeta)
print ("Objects in Argus with ambiguous spectral type:", noadopargus)
print ("Objects in Columba with ambiguous spectral type:", noadopcolum)
print ("Objects in TW Hya with ambiguous spectral type:", noadoptw)

print (len(rabeta))
print (len(dbeta))
print (len(specbeta))
print (spectuc)
### END TEST SECTION ###

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

### Steph's suggestion
# replace cubehelix with whichever colormap you want, 
# it looks like you're using autumn
cmap = plt.cm.hot


# Use the minimum and maximum SpT values you have here
# colormaps usually use values 0->1, so you're telling it the range of values you need it to cover
# And if the later types are too light, increase vmax or change your colormap
color_norm = Normalize(vmin=6, vmax=18)
### end Steph's suggestions


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")

### Steph's suggestion
# then, your plot call should look like this (plug in your values):
### ax.scatter(ra, dec, c=spectral_types, cmap=cmap, marker="o", markersize=30, label="label", norm=color_norm)
# c=spectral_types means it will color the points according to the spectral types
# cmap=cmap tells it what colormap to use
# norm=color_norm sets the normalization
### Steph's suggestion

spectypes = ["M6",  "M8",  "L0",  "L2",  "L4",  "L6",  "L8"]
cax1 = ax.scatter(ratuc.radian, dtuc.radian, c = spectuc, cmap = cmap, marker = "s", label = "Tuc-Hor", norm=color_norm)
#cax2 = ax.scatter(raab.radian,dab.radian, c = "g", label = "AB Doradus")
#cax3 = ax.scatter(ranone.radian,dnone.radian, c = ".96", label = "None")
#cax4 = ax.scatter(rabeta.radian, dbeta.radian, c = specbeta, cmap = cmap1, label = "Beta Pictoris", norm=color_norm)
#cax5 = ax.scatter(raargus.radian,dargus.radian, c = "c", label = "Argus")
cax6 = ax.scatter(racolum.radian,dcolum.radian, c = speccolum, cmap = cmap, marker = "o", label = "Columba", norm=color_norm)
#cax = ax.scatter(ratw.radian,dtw.radian, c="r", label = "TW Hya") #c = "r"

ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1.25), loc = 1, borderaxespad=0., prop={'size': 7})

axo = plt.gca()
legend = axo.get_legend()
legend.legendHandles[0].set_color('white')
legend.legendHandles[0].set_edgecolor('black')
legend.legendHandles[1].set_color('white')
legend.legendHandles[1].set_edgecolor('black')

m=cm.ScalarMappable(cmap=cm.hot)
#m.set_array([0, .25,.5,.75, 1])
m.set_array([-3, -2, -1, 0, 1, 2, 3])
cbar = fig.colorbar(m, orientation='horizontal', ticks=[-3, -2, -1, 0, 1, 2, 3], spacing=u'uniform')
cbar.ax.set_xticklabels(spectypes)

fig.savefig("map3.pdf")


