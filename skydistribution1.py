import sqlite3
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import ascii




with open('membershipad.csv', 'rU') as file: #tells python we will be using the csv file
    

    reader = csv.reader(file) # reads csv file

 #   conn = sqlite3.connect('bdnyc.db')  #tells python we will be using this database
 #   c = conn.cursor() #reads conn
    
    ratuc = []
    raab = []
  #  ranone = []
    rabeta = []
    raargus = []
 #   raher = []
 #   raursa =[]
 #   raambig = []
    racolum = []
    ratw = []
    
    tuc = 'tucana'
    ab = 'abdora'
   # nostar = 'None'
    beta = 'betapic'
    argus = 'argus'
   # her = 'Old (Her-Lyr)'
   # ursa = 'Old (Ursa Majo'
   # ursa2 = 'Old (Ursa Major)'
   # ambig = 'Ambiguous'
    colum = 'columba'
    tw = 'twhydra'
    
    dtuc = []
    dab = []
  #  dnone = []
    dbeta = []
    dargus = []
  #  dher = []
  #  dursa = []
  #  dambig = []
    dcolum = []
    dtw = []

    nametuc = []
    nameab = []
  #  namenone = []
    namebeta = []
    nameargus = []
  #  nameher = []
  #  nameursa = []
  #  nameambig = []
    namecolum = []
    nametw = []
    


    for line in reader:
     #   if len(line[0].strip()) == 9:
          #  t= (line[0].strip(),)
            
            
            #for row in reader:
            linecomp = line[24].strip()
            if linecomp == tuc:
                ratuc.append(float(line[9]))
                dtuc.append(float(line[10]))
                nametuc.append(line[0])
            elif linecomp == ab:
                raab.append(float(line[9]))
                dab.append(float(line[10]))
                 #   nameab.append(row[7])
              #  elif linecomp == nostar:
               #     ranone.append(row[9])
                #    dnone.append(row[10])
                 #   namenone.append(row[7])
            elif linecomp == beta:
                rabeta.append(float(line[9]))
                dbeta.append(float(line[10]))
                 #   namebeta.append(row[7])
            elif linecomp== argus:
                raargus.append(float(line[9]))
                dargus.append(float(line[10]))
                  #  nameargus.append(row[7])
              #  elif linecomp == her:
               #     raher.append(row[9])
                #    dher.append(row[10])
                  #  nameher.append(row[7])
              #  elif linecomp == ursa or linecomp == ursa2:
               #     raursa.append(row[9])
                #    dursa.append(row[10])
                 #   nameursa.append(row[7])
              #  elif linecomp == ambig:
               #     raambig.append(row[9])
                #    dambig.append(row[10])
                  #  nameambig.append(row[7])
            elif linecomp == colum:
                racolum.append(float(line[9]))
                dcolum.append(float(line[10]))
                 #   namecolum.append(row[7])
            elif linecomp == tw:
                ratw.append(float(line[9]))
                dtw.append(float(line[10]))
                  #  nametw.append(row[7])
            

    #for s in sidtuc:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            spectuc.append(row[2])

    #for s in sidab:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specab.append(row[2])

    #for s in sidnone:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specnone.append(row[2])

    #for s in sidbeta:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specbeta.append(row[2])

    #for s in sidargus:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specargus.append(row[2])

    #for s in sidher:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specher.append(row[2])

    #for s in sidursa:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specursa.append(row[2])

    #for s in sidambig:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            specambig.append(row[2])

    #for s in sidcolum:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            speccolum.append(row[2])

    #for s in sidtw:
    #    t=(s,)
    #    for row in c.execute('SELECT * FROM spectral_types WHERE source_id =?', t):
    #        if not isinstance(row[2], basestring):
    #            spectw.append(row[2])
                
    #conn.close()

    #print ratuc
    
ascii.write([ratuc, dtuc, nametuc], 'tucdata1.csv', delimiter = ',')
    

ratuc = coord.Angle(ratuc*u.degree)
ratuc = ratuc.wrap_at(180*u.degree)
dtuc = coord.Angle(dtuc*u.degree)

raab = coord.Angle(raab*u.degree)
raab = raab.wrap_at(180*u.degree)
dab = coord.Angle(dab*u.degree)

#ranone = coord.Angle(ranone*u.degree)
#ranone = ranone.wrap_at(180*u.degree)
#dnone = coord.Angle(dnone*u.degree)

rabeta = coord.Angle(rabeta*u.degree)
rabeta = rabeta.wrap_at(180*u.degree)
dbeta = coord.Angle(dbeta*u.degree)

raargus = coord.Angle(raargus*u.degree)
raargus = raargus.wrap_at(180*u.degree)
dargus = coord.Angle(dargus*u.degree)

#raher = coord.Angle(raher*u.degree)
#raher = raher.wrap_at(180*u.degree)
#dher = coord.Angle(dher*u.degree)

#raursa = coord.Angle(raursa*u.degree)
#raursa = raursa.wrap_at(180*u.degree)
#dursa = coord.Angle(dursa*u.degree)

#raambig = coord.Angle(raambig*u.degree)
#raambig = raambig.wrap_at(180*u.degree)
#dambig = coord.Angle(dambig*u.degree)

racolum = coord.Angle(racolum*u.degree)
racolum = racolum.wrap_at(180*u.degree)
dcolum = coord.Angle(dcolum*u.degree)

ratw = coord.Angle(ratw*u.degree)
ratw = ratw.wrap_at(180*u.degree)
dtw = coord.Angle(dtw*u.degree)

ascii.write([ratuc, dtuc, nametuc], 'tucdata2.csv', delimiter = ',')


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")

ax.scatter(ratuc.radian, dtuc.radian, c = "b", label = "Tuc-Hor")
ax.scatter(raab.radian,dab.radian, c = "g", label = "AB Doradus")
#ax.scatter(ranone.radian,dnone.radian, c = "r", label = "None")
ax.scatter(rabeta.radian,dbeta.radian, c = "y", label = "Beta Pictorus")
ax.scatter(raargus.radian,dargus.radian, c = "c", label = "Argus")
#ax.scatter(raher.radian,dher.radian, c = "m", label = "Old (Her-Lyr)")
#ax.scatter(raursa.radian,dursa.radian, c = "k", label = "Old (Ursa Major)")
#ax.scatter(raambig.radian,dambig.radian, c = ".5", label = "Ambiguous")
ax.scatter(racolum.radian,dcolum.radian, c = "m", label = "Columba")
ax.scatter(ratw.radian,dtw.radian, c = "r", label = "TW Hya")

ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1.25), loc = 1, borderaxespad=0., prop={'size': 7})
fig.savefig("map.pdf")

#spec = [spectuc, specab, specnone, specbeta, specargus, specher, specursa, specambig, speccolum, spectw]

#n_bins = 24

#fig, axes = plt.subplots(nrows=1, ncols=1)
#ax0 = axes

#c = ['Tuc-Hor', 'AB Dor', 'None', 'beta Pic', 'Argus', 'Old (Her-Lyr)', 'Old (Ursa Major)', 'Ambiguous', 'Columba', 'TW Hya']
#color_c= ['b','g','r','y','c','m','k','.5','.75','.9']
#ax0.hist(spec, n_bins, histtype='bar', label = c, stacked = True, color=color_c)
#ax0.legend(prop={'size':10})
#ax0.set_title('spectral type vs moving group')

#plt.show()
