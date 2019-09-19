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

def getCorrectedRO(inputCSV):
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
        clk0      = 100*row[3]/nominalRow[3]
        clk4      = 100*row[4]/nominalRow[4]
        inv0      = 100*row[5]/nominalRow[5]
        inv4      = 100*row[6]/nominalRow[6]
        nand0     = 100*row[7]/nominalRow[7]
        nand4     = 100*row[8]/nominalRow[8]
        nor0      = 100*row[9]/nominalRow[9]
        nor4      = 100*row[10]/nominalRow[10]

        inverterClk.append(clk0 - clk4)
        inverter.append(inv0 - inv4)
        nand.append(nand0- nand4)
        nor.append(nor0 - nor4)
        doses.append(dose)
        temperatures.append(temp)

  return inverterClk,inverter,nand,nor,doses,temperatures

def getRawRO(inputCSV):
  with open(inputCSV) as csv_file:
    inverter0   =[]
    inverter4   =[]
    clock0      =[]
    clock4      =[]
    notand0     =[]
    notand4     =[]
    notor0      =[]
    notor4      =[]
    doses       =[]
    temperatures=[]
    nominalRow  = findNominalValues(inputCSV)
    csv_reader  = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        timestamp = row[0]
        temp      = row[1]
        dose      = row[2]
        clk0      = 100*row[3]/nominalRow[3]
        clk4      = 100*row[4]/nominalRow[4]
        inv0      = 100*row[5]/nominalRow[5]
        inv4      = 100*row[6]/nominalRow[6]
        nand0     = 100*row[7]/nominalRow[7]
        nand4     = 100*row[8]/nominalRow[8]
        nor0      = 100*row[9]/nominalRow[9]
        nor4      = 100*row[10]/nominalRow[10]

        clock0.append(clk0)
        clock4.append(clk0)
        inverter0.append(inv0)
        inverter4.append(inv4)
        notand0.append(nand0)
        notand4.append(nand4)
        notor0.append(nor0)
        notor4.append(nor4)
        temperatures.append(temp)
        doses.append(dose)

  return clock0,clock4,inverter0,inverter4,notand0,notand4,notor0,notor4,doses,temperatures

def plotCorrectedRO():
  c1Data = getCorrectedRO("Chip1.csv") #inverterClk,inverter,nand,nor,doses,temperatures
  c2Data = getCorrectedRO("Chip2.csv")
  c3Data = getCorrectedRO("Chip3.csv")
  c4Data = getCorrectedRO("Chip4.csv")
  c6Data = getCorrectedRO("Chip6.csv")



  c1Temp=np.average(c1Data[-1])
  c2Temp=np.average(c2Data[-1])
  c3Temp=np.average(c3Data[-1])
  c4Temp=np.average(c4Data[-1])
  c6Temp=np.average(c6Data[-1])


  #inverterClk = np.convolve(inverterClk, np.ones(windowLength)/windowLength,mode='same')
  windowLength=5
  everyNth    =1
  markersize=9

  axes = plt.gca()
  #axes.set_xlim([xmin,xmax])
  axes.set_ylim([-2,2])
  axes.set_xlim([0,50])
  plt.plot(c1Data[4][::everyNth], np.convolve(c1Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 'x',markersize=markersize, label=c1Temp)
  plt.plot(c2Data[4][::everyNth], np.convolve(c2Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 'o',markersize=markersize, label=c2Temp)
  plt.plot(c3Data[4][::everyNth], np.convolve(c3Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 'v',markersize=markersize, label=c3Temp)
  plt.plot(c4Data[4][::everyNth], np.convolve(c4Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 's',markersize=markersize, label=c4Temp)
  plt.plot(c6Data[4][::everyNth], np.convolve(c6Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], '*',markersize=markersize, label=c6Temp)
  plt.legend(loc='best')
  plt.show()


def plotRawRO():
  rawC1Data = getRawRO("Chip1.csv")
  rawC2Data = getRawRO("Chip2.csv")
  rawC3Data = getRawRO("Chip3.csv")
  rawC4Data = getRawRO("Chip4.csv")
  rawC6Data = getRawRO("Chip6.csv")

  c1Temp=np.average(rawC1Data[-1])
  c2Temp=np.average(rawC2Data[-1])
  c3Temp=np.average(rawC3Data[-1])
  c4Temp=np.average(rawC4Data[-1])
  c6Temp=np.average(rawC6Data[-1])


  #inverterClk = np.convolve(inverterClk, np.ones(windowLength)/windowLength,mode='same')
  windowLength=5
  everyNth    =1
  markersize=9

  axes = plt.gca()
  #axes.set_xlim([xmin,xmax])
  axes.set_ylim([90,110])
 # axes.set_xlim([0,50])
  plt.plot(rawC1Data[-2][::everyNth], np.convolve(rawC1Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 'x',markersize=markersize, label=c1Temp)
  plt.plot(rawC2Data[-2][::everyNth], np.convolve(rawC2Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 'o',markersize=markersize, label=c2Temp)
  plt.plot(rawC3Data[-2][::everyNth], np.convolve(rawC3Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 'v',markersize=markersize, label=c3Temp)
  plt.plot(rawC4Data[-2][::everyNth], np.convolve(rawC4Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], 's',markersize=markersize, label=c4Temp)
  plt.plot(rawC6Data[-2][::everyNth], np.convolve(rawC6Data[0],np.ones(windowLength)/windowLength,mode='same')[::everyNth], '*',markersize=markersize, label=c6Temp)
  plt.legend(loc='best')
  plt.show()


plotRawRO()
plotCorrectedRO()