import sqlite3
import csv
import numpy as np
import matplotlib.pyplot as plt
from math import floor



with open('/Users/admin/Code/Python/BDNYC/membership.csv') as file: #tells python we will be using the csv file
    

    reader = csv.reader(file) # reads csv file

    conn = sqlite3.connect('/Users/admin/Code/Python/BDNYC/BDNYC.db')  #tells python we will be using this database
    c = conn.cursor() #reads conn
    
    sidtuc = []
    sidab = []
    sidnone = []
    sidbeta = []
    sidargus = []
    sidher = []
    sidursa =[]
    sidambig = []
    sidcolum = []
    sidtw = []
    
    tuc = 'Tuc-Hor'
    ab = 'AB Dor'
    nostar = 'None'
    beta = 'beta Pic'
    argus = 'Argus'
    her = 'Old (Her-Lyr)'
    ursa = 'Old (Ursa Majo'
    ursa2 = 'Old (Ursa Major)'
    ambig = 'Ambiguous'
    colum = 'Columba'
    tw = 'TW Hya'
    
    spectuc = []
    specab = []
    specnone = []
    specbeta = []
    specargus = []
    specher = []
    specursa = []
    specambig = []
    speccolum = []
    spectw = []
    


    for line in reader:
        if len(line[0].strip()) == 9:
            t= (line[0].strip(),)
            
            
            for row in c.execute('SELECT * FROM sources WHERE shortname=?',t):
                linecomp = line[1].strip()
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
                elif linecomp == her:
                    sidher.append(row[0])
                elif linecomp == ursa or linecomp == ursa2:
                    sidursa.append(row[0])
                elif linecomp == ambig:
                    sidambig.append(row[0])
                elif linecomp == colum:
                    sidcolum.append(row[0])
                elif linecomp == tw:
                    sidtw.append(row[0])
            

    for s in sidtuc:
        t=(s,)
        for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
            if not isinstance(row[2], basestring):
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

    for s in sidher:
        t=(s,)
        for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
            if not isinstance(row[2], basestring):
                specher.append(floor(row[2]))

    for s in sidursa:
        t=(s,)
        for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
            if not isinstance(row[2], basestring):
                specursa.append(floor(row[2]))

    for s in sidambig:
        t=(s,)
        for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
            if not isinstance(row[2], basestring):
                specambig.append(floor(row[2]))

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
                
    conn.close()

#spec = [spectuc, specab, specnone, specbeta, specargus, specher, specursa, specambig, speccolum, spectw]

n_bins = 12

fig, axes = plt.subplots(nrows=5, ncols=2)
ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9 = axes.flat

#c = ['Tuc-Hor', 'AB Dor', 'None', 'beta Pic', 'Argus', 'Old (Her-Lyr)', 'Old (Ursa Major)', 'Ambiguous', 'Columba', 'TW Hya']
#color_c= ['b','g','r','y','c','m','k','.5','.75','.9']

spectypes = ["M6",  "M8",  "L0",  "L2",  "L4",  "L6",  "L8"]
plt.setp(axes, xticks = [6,  8,  10,  12,  14,  16,  18], xticklabels = spectypes, yticks = [0, 5, 10, 15, 20])

ax0.hist(spectuc, n_bins, range = [6, 18], histtype='bar', label = 'Tuc-Hor', align = "left", fill = True, color='b')
ax0.legend(prop={'size':10})
ax0.axis([6, 18, 0, 20])
#ax0.set_xticks([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],spectypes)
#ax0.set_title('spectral type vs moving group (Tuc-Hor)')

ax1.hist(specab, n_bins, range = [6, 18], histtype='bar', label = 'AB Dor', align = "left", fill = True, color='g')
#ax1.set_title('spectral type vs moving group (AB Dor)')
ax1.legend(prop={'size':10})
ax1.axis([6, 18, 0, 20])

ax2.hist(specnone, n_bins, range = [6, 18], histtype='bar', label = 'None', align = "left", fill = True, color='r')
ax2.legend(prop={'size':10})
#ax2.set_title('spectral type vs moving group (None)')
ax2.axis([6, 18, 0, 20])

ax3.hist(specbeta, n_bins, range = [6, 18], histtype='bar', label = 'Beta Pic', align = "left", fill = True, color='y')
ax3.legend(prop={'size':10})
#ax3.set_title('spectral type vs moving group (Beta Pic)')
ax3.axis([6, 18, 0, 20])

ax4.hist(specargus, n_bins, range = [6, 18], histtype='bar', label = 'Argus', align = "left", fill = True, color='c')
ax4.legend(prop={'size':10})
#ax4.set_title('spectral type vs moving group (Argus)')
ax4.axis([6, 18, 0, 20])

ax5.hist(specher, n_bins, range = [6, 18], histtype='bar', label = 'Old (Her-Lyr)', align = "left", fill = True, color='m')
ax5.legend(prop={'size':10})
#ax5.set_title('spectral type vs moving group (Old (Her-Lyr)')
ax5.axis([6, 18, 0, 20])

ax6.hist(specursa, n_bins, range = [6, 18], histtype='bar', label = 'Old (Ursa Major)', align = "left", fill = True, color='k')
ax6.legend(prop={'size':10})
#ax6.set_title('spectral type vs moving group (Old (Ursa Major))')
ax6.axis([6, 18, 0, 20])

ax7.hist(specambig, n_bins, range = [6, 18], histtype='bar', label = 'Ambiguous', align = "left", fill = True, color='.5')
ax7.legend(prop={'size':10})
#ax7.set_title('spectral type vs moving group (Ambiguous)')
ax7.axis([6, 18, 0, 20])

ax8.hist(speccolum, n_bins, range = [6, 18], histtype='bar', label = 'Columba', align = "left", fill = True, color='.75')
ax8.legend(prop={'size':10})
#ax8.set_title('spectral type vs moving group (Columba)')
ax8.axis([6, 18, 0, 20])

ax9.hist(spectw, n_bins, range = [6, 18], histtype='bar', label = 'TW Hya', align = "left", fill = True, color='.9')
ax9.legend(prop={'size':10})
#ax9.set_title('spectral type vs moving group (TW Hya)')
ax9.axis([6, 18, 0, 20])

plt.tight_layout()
plt.show()
