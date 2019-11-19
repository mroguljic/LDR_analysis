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
  normalization = 1.
  with open(inputCSV) as csv_file:
    inverterClk =[]
    inverter    =[]
    nand        =[]
    nor         =[]
    doses       =[]
    temperatures=[]
    nominalRow  = findNominalValues(inputCSV)
    csv_reader  = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        timestamp = row[0]
        temp      = row[1]
        dose      = row[2]
        clk0      = normalization*row[3]/nominalRow[3]
        clk4      = normalization*row[4]/nominalRow[4]
        inv0      = normalization*row[5]/nominalRow[5]
        inv4      = normalization*row[6]/nominalRow[6]
        nand0     = normalization*row[7]/nominalRow[7]
        nand4     = normalization*row[8]/nominalRow[8]
        nor0      = normalization*row[9]/nominalRow[9]
        nor4      = normalization*row[10]/nominalRow[10]

        inverterClk.append(clk0 - clk4)
        inverter.append(inv0 - inv4)
        nand.append(nand0- nand4)
        nor.append(nor0 - nor4)
        doses.append(dose)
        temperatures.append(temp)


  f = plt.figure(1,[20,12])
  plt.suptitle(title, fontsize=30)
  

  # ax = plt.subplot(221)
  # inverterClk = np.convolve(inverterClk, np.ones(windowLength)/windowLength,mode='same')
  # temperatures = np.convolve(temperatures, np.ones(windowLength)/windowLength,mode='same')
  # ax1, ax2 = two_scales(ax, doses, inverterClk, temperatures, 'r', 'b', 'RO','Temperature')

  # ax = plt.subplot(222)
  # inverter = np.convolve(inverter, np.ones(windowLength)/windowLength,mode='same')
  # ax1, ax2 = two_scales(ax, doses, inverter, temperatures, 'r', 'b', 'RO','Temperature',marker='s')

  # ax = plt.subplot(223)
  # nand = np.convolve(nand, np.ones(windowLength)/windowLength,mode='same')
  # ax1, ax2 = two_scales(ax, doses, nand, temperatures, 'r', 'b', 'RO','Temperature',marker='v') 
  
  # ax = plt.subplot(224)
  # nor = np.convolve(nor, np.ones(windowLength)/windowLength,mode='same')
  # ax1, ax2 = two_scales(ax, doses, nor, temperatures, 'r', 'b', 'RO','Temperature',marker='*')

  plt.subplot(221)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=1),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference in %', fontsize = 20)
  inverterClk = np.convolve(inverterClk, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, inverterClk,'ro',markersize=5, label='Inverter Clock')
  plt.legend(fontsize=20)
  plt.grid(which='major',color='black')
  plt.grid(which='minor')

  plt.subplot(222)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=1),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference in %', fontsize = 20)
  inverter = np.convolve(inverter, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, inverter,'b*',markersize=5, label='Inverter')
  plt.legend(fontsize=20)
  plt.grid(which='major',color='black')
  plt.grid(which='minor')

  plt.subplot(223)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=1),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference in %', fontsize = 20)
  nand = np.convolve(nand, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, nand,'cv',markersize=5, label='NAND')
  plt.legend(fontsize=20)
  plt.grid(which='major',color='black')
  plt.grid(which='minor')

  plt.subplot(224)
  plt.ylim(top=yup)  # adjust the top leaving bottom unchanged
  plt.minorticks_on()
  plt.xticks(fontsize=16)
  plt.yticks(np.arange(ylow, yup, step=1),fontsize=16)
  plt.ylim(bottom=ylow)
  plt.xlabel('Dose [MRad]', fontsize = 20)
  plt.ylabel('Relative difference in %', fontsize = 20)
  nor = np.convolve(nor, np.ones(windowLength)/windowLength,mode='same')
  plt.plot(doses, nor,'ms',markersize=5, label='NOR')
  plt.legend(fontsize=20)
  plt.grid(which='major',color='black')
  plt.grid(which='minor')
  
  figName = inputCSV[:-4]+'.png'
  plt.savefig(figName)
  print('Saved figure '+figName)
  f.clear()
  plt.close(f )


plot("Chip1.csv",title="Chip 1 ring oscillator response to radiation",ylow=-2,yup=1.5,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip2.csv",title="Chip 2 ring oscillator response to radiation",ylow=-2,yup=1.5,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip3.csv",title="Chip 3 ring oscillator response to radiation",ylow=-2,yup=1.5,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip4.csv",title="Chip 4 ring oscillator response to radiation",ylow=-5,yup=2,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
plot("Chip6.csv",title="Chip 6 ring oscillator response to radiation",ylow=-5,yup=2,windowLength=5) #inputCSV,title="Title",ylow=-0.5,yup=1.5
