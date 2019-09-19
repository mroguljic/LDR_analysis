import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def timeToDose(unixSeconds,doseTable="coldDoses.csv"):
  
  date = datetime.utcfromtimestamp(unixSeconds).strftime('%d/%m/%Y')
  hour = datetime.utcfromtimestamp(unixSeconds).strftime('%H')
  ratioOfWorkingDay =(float(hour)-7.)/10.
  if(ratioOfWorkingDay>1.):
    ratioOfWorkingDay=1.
  if(ratioOfWorkingDay<0.):
    ratioOfWorkingDay=0.
  #print(date)
  #print(hour)
  #print(ratioOfWorkingDay)

  previousLine = []
  with open(doseTable, "r") as f:
    reader = csv.reader(f, delimiter=",")
    for i,line in enumerate(reader):
      if(line[0]==date):
        #print(previousLine)
        #print(line)
        #print(float(line[1])-float(previousLine[1]))
        dose = float(previousLine[1])+ratioOfWorkingDay*(float(line[1])-float(previousLine[1]))
        if(dose<float(previousLine[1])):
          print('Dose calculation wrong!')
        return dose
      previousLine = line
  print('----Dose calculation failed for - '+date)
  return 0


def analyzeDirectory(directory,doseTable,outputFile):
  outfile = open(outputFile,"w")
  for root, dirs, files in os.walk('./'+directory, topdown = False):
    for name in files:
      if(name!="output_data.dat"):
        continue
      #print(os.path.join(root, name))
      f = open(os.path.join(root, name), "r")
      lines       = f.readlines()
      temperature = lines[1].strip(' \n')
      timestamp   = lines[2].strip('\n')
      ROvalues    = lines[11].split()
      dose        = timeToDose(float(timestamp),doseTable)
      #csvline     = timestamp+','+temperature+','+str(dose)
      csvline     = '{0:.10},{1},{2:.2f}'.format(timestamp,temperature,dose)
      for ROvalue in ROvalues:
        if(ROvalue=='819.2'):#pulse duration
          continue
        csvline   +=','
        csvline   +=ROvalue
      print(csvline)
      outfile.write(csvline+'\n')

      f.close()

#analyzeDirectory('Chip1','coldDoses.csv','Chip1.csv')
#analyzeDirectory('Chip2','coldDoses.csv','Chip2.csv')
#analyzeDirectory('Chip3','coldDoses.csv','Chip3.csv')
analyzeDirectory('Chip4','roomTempDoses.csv','Chip4.csv')
analyzeDirectory('Chip6','roomTempDoses.csv','Chip6.csv')
