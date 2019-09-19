import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def findNominalValues(inputCSV):
  firstTimestamp = 99999999999999
  firstRow = []
  with open(inputCSV) as csv_file:
    csv_reader  = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        timestamp = row[0]
        if(timestamp<firstTimestamp):
          firstTimestamp=timestamp
          firstRow = row

  print("Found earliest timestamp {0} with row:".format(firstTimestamp))
  print(firstRow)
  return firstRow

def two_scales(ax1, xData, data1, data2, c1, c2,titleOne,titleTwo,marker='o'):
    ax2 = ax1.twinx()
    ax1.plot(xData, data1, color=c1,marker=marker,markersize=5,ls='none')
    ax1.set_xlabel('Dose[MRad]')
    ax1.set_ylabel(titleOne)
    ax2.plot(xData, data2, color=c2,marker=marker,markersize=5,ls='none')
    ax2.set_ylabel(titleTwo)
    return ax1, ax2


def plot(inputCSV,title="Title",ylow=-0.5,yup=1.5,windowLength=1):
  with open(inputCSV) as csv_file:
    clk0        =[]
    clk4        =[]
    inv0        =[]
    inv4        =[]
    nand0       =[]
    nand4       =[]
    nor0        =[]
    nor4        =[]
    doses       =[]
    temperatures=[]
    nominalRow  = findNominalValues(inputCSV)
    csv_reader  = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        timestamp = row[0]
        temp      = row[1]
        dose      = row[2]
        clk0.append(row[3]/nominalRow[3])
        clk4.append(row[4]/nominalRow[4])
        inv0.append(row[5]/nominalRow[5])
        inv4.append(row[6]/nominalRow[6])
        nand0.append(row[7]/nominalRow[7])
        nand4.append(row[8]/nominalRow[8])
        nor0.append(row[9]/nominalRow[9])
        nor4.append(row[10]/nominalRow[10])
        doses.append(dose)
        temperatures.append(temp)


  f = plt.figure(1,[20,12])
  plt.suptitle(title, fontsize=30)
  

  plt.subplot(241)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  clk0 = np.convolve(clk0, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, clk0,'ro',markersize=5, label='CLK0')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')


  plt.subplot(242)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  clk4 = np.convolve(clk4, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, clk4,'ro',markersize=5, label='CLK4')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')


  plt.subplot(243)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  inv0 = np.convolve(inv0, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, inv0,'ro',markersize=5, label='INV0')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')


  plt.subplot(244)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  inv4 = np.convolve(inv4, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, inv4,'ro',markersize=5, label='INV4')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')


  plt.subplot(245)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  nand0 = np.convolve(nand0, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, nand0,'ro',markersize=5, label='NAND0')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')


  plt.subplot(246)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  nand4 = np.convolve(nand4, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, nand4,'ro',markersize=5, label='NAND4')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')



  plt.subplot(247)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  nor0 = np.convolve(nor0, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, nor0,'ro',markersize=5, label='NOR0')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')

  plt.subplot(248)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=0.01),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference', fontsize = 20)
  nor4 = np.convolve(nor4, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, nor4,'ro',markersize=5, label='NOR4')
  plt.legend(fontsize=20)
  plt.grid(which='major',axis='both')



  figName = inputCSV[:-4]+'_drivers.png'
  plt.savefig(figName)
  print('Saved figure '+figName)
  f.clear()
  plt.close(f )


plot("Chip1.csv",title="Chip 1 ring oscillator response to radiation",ylow=0.95,yup=1.05,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip2.csv",title="Chip 2 ring oscillator response to radiation",ylow=0.95,yup=1.05,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip3.csv",title="Chip 3 ring oscillator response to radiation",ylow=0.95,yup=1.05,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip4.csv",title="Chip 4 ring oscillator response to radiation",ylow=0.9,yup=1.05,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip6.csv",title="Chip 6 ring oscillator response to radiation",ylow=0.9,yup=1.05,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
