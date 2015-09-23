
import sqlite3
import csv
import numpy as np
import matplotlib.pyplot as plt
from math import floor


#TELLS PYTHON WE WILL BE USING THE CSV FILE

with open('membershipadhist.csv', 'rU') as file:
    
    with open('nomembershipadhist.csv', 'rU') as filenm:

        # READS MEMBERSHIPADHIST.CSV FILE FOR OBJECTS WITH MEMBERSHIP
        reader = csv.reader(file)
        # READS NOMEMBERSHIPADHIST.CSV FOR OBJECTS WITH NO MEMBERSHIP
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

        # SHORTCUT TO CHECK IN THE CSV FILE WHICH MOVING GROUP EACH OF THEM ARE IN (TO AVOID SCREWING UP)
        tuc = 'tucana'
        ab = 'abdora'
        nostar = 'None'
        beta = 'betapic'
        argus = 'argus'
        colum = 'columba'
        tw = 'twhydra'

        # THIS CREATES ARRAYS TO HOLD SPECTRAL TYPES FOR EACH MOVING GROUP
        spectuc = []
        specab = []
        specnone = []
        specbeta = []
        specargus = []
        speccolum = []
        spectw = []


        # GOES THROUGH READERNM FILE LINE BY LINE
        for line in readernm:
            # THIS GETS OBJECTS THAT HAVE SHORTNAME WITH 9 CHARACTERS. STRIP IGNORES ANY BLANK SPACES IN FRONT OR AFTER THE SHORTNAME
            if len(line[0].strip()) ==9:
                # IF SHORTNAME IS 9 CHARACTERS LONG IT GETS STORED IN t
                t = (line[0].strip(),)

                # MATCHES SHORTNAME TO ID IN THE DATABASE IN THE SOURCES TABLE
                for row in c.execute('SELECT * FROM sources WHERE shortname=?',t):
                    # STORES THE ID IN SIDNONE ARRAY
                    sidnone.append(row[0])

            # THIS GETS THE OBJECTS WITH NAMES THAT ARE NOT SHORTNAMES (SUCH AS TWA 27). >1 JUST MEANS THAT WE IGNORE CELLS WITH NOTHING IN THEM
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
                    linecomp = line[24].strip()
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
                    linecomp = line[24].strip()
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


        # GOES THROUGH EVERY OBJECT IN SIDTUC
        for s in sidtuc:
            # t STORES EACH ID
            t=(s,)
            # GOES BACK TO DATABASE IN THE SPRECTRAL TYPES TABLE AND PULLS THE SPECTRAL TYPE FOR THAT OBJECT
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
# NEED TO FIND OUT WHY I DID THIS                
                if not isinstance(row[2], basestring):
                    # STORES THE SPECTRAL TYPES IN THIS ARRAY
                    spectuc.append(floor(row[2]))

        for s in sidab:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                if not isinstance(row[2], basestring):
                    specab.append(floor(row[2]))

        for s in sidnone:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                if not isinstance(row[2], basestring):
                    specnone.append(floor(row[2]))

        for s in sidbeta:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                if not isinstance(row[2], basestring):
                    specbeta.append(floor(row[2]))

        for s in sidargus:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                if not isinstance(row[2], basestring):
                    specargus.append(floor(row[2]))

        for s in sidcolum:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                if not isinstance(row[2], basestring):
                    speccolum.append(floor(row[2]))

        for s in sidtw:
            t=(s,)
            for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
                if not isinstance(row[2], basestring):
                    spectw.append(floor(row[2]))

        # STOPS USING BDNYC DATABASE
        conn.close()


# 12 DIFFERENT SPECTRAL TYPES 
n_bins = 12

# EACH OF THESE TELLS PYTHON THE POSITION OF EACH SUB PLOT FOR EACH MOVING GROUP
ax0 = plt.subplot2grid((4,4),(0,0), colspan=2)
ax1 = plt.subplot2grid((4,4),(0,2), colspan=2)
ax2 = plt.subplot2grid((4,4),(1,0), colspan=2)
ax3 = plt.subplot2grid((4,4),(1,2), colspan=2)
ax4 = plt.subplot2grid((4,4),(2,0), colspan=2)
ax8 = plt.subplot2grid((4,4),(2,2), colspan=2)
ax9 = plt.subplot2grid((4,4),(3,1), colspan=2)


# CREATES LABELS THE GRAPHS DISPLAY
spectypes = ["M6",  "M8",  "L0",  "L2",  "L4",  "L6",  "L8"]
# EACH OF THESE SET PARAMETERS FOR THE PLOTS, PLT.SETP = SETS PARAMETERS, XTICKS = SETS RANGE OF SPECTRAL TYPE, XTICKLABELS = TELLS PYTHON TO DISPLAY SPECTYPES INSTEAD OF NUMBERS, YTICKS = SETS RANGE OF NUMBERS
plt.setp(ax0, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])
plt.setp(ax1, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])
plt.setp(ax2, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])
plt.setp(ax3, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])
plt.setp(ax4, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])
plt.setp(ax8, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])
plt.setp(ax9, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])

# THESE CREATE THE PLOTS. 
ax0.hist(spectuc, n_bins, range = [6, 18], histtype='bar', label = 'Tuc-Hor', align = "left", fill = True, color='b')
ax0.legend(prop={'size':10})
ax0.axis([6, 18, 0, 20])

ax1.hist(specab, n_bins, range = [6, 18], histtype='bar', label = 'AB Dor', align = "left", fill = True, color='g')
ax1.legend(prop={'size':10})
ax1.axis([6, 18, 0, 20])

ax2.hist(specnone, n_bins, range = [6, 18], histtype='bar', label = 'None', align = "left", fill = True, color='r')
ax2.legend(prop={'size':10})
ax2.axis([6, 18, 0, 20])

ax3.hist(specbeta, n_bins, range = [6, 18], histtype='bar', label = 'Beta Pic', align = "left", fill = True, color='y')
ax3.legend(prop={'size':10})
ax3.axis([6, 18, 0, 20])

ax4.hist(specargus, n_bins, range = [6, 18], histtype='bar', label = 'Argus', align = "left", fill = True, color='c')
ax4.legend(prop={'size':10})
ax4.axis([6, 18, 0, 20])


ax8.hist(speccolum, n_bins, range = [6, 18], histtype='bar', label = 'Columba', align = "left", fill = True, color='.75')
ax8.legend(prop={'size':10})
ax8.axis([6, 18, 0, 20])

ax9.hist(spectw, n_bins, range = [6, 18], histtype='bar', label = 'TW Hya', align = "left", fill = True, color='.9')
ax9.legend(prop={'size':10})
ax9.axis([6, 18, 0, 20])

# KEEPS THE PLOTS ORGANIZED
plt.tight_layout()
# PRINTS THE PLOT
plt.show()
