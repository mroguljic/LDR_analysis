import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

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

def getCorrectedRO(inputCSV):
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

  return inverterClk,inverter,nand,nor,doses,temperatures


def getTimeDelays(inputCSV):
  normalization = 1.
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
        clk0      = (normalization*(1/row[3])/(1/nominalRow[3]) - 1)*100
        clk4      = (normalization*(1/row[4])/(1/nominalRow[4]) - 1)*100
        inv0      = (normalization*(1/row[5])/(1/nominalRow[5]) - 1)*100
        inv4      = (normalization*(1/row[6])/(1/nominalRow[6]) - 1)*100
        nand0     = (normalization*(1/row[7])/(1/nominalRow[7]) - 1)*100
        nand4     = (normalization*(1/row[8])/(1/nominalRow[8]) - 1)*100
        nor0      = (normalization*(1/row[9])/(1/nominalRow[9]) - 1)*100
        nor4      = (normalization*(1/row[10])/(1/nominalRow[10]) - 1)*100

        clock0.append(clk0)
        clock4.append(clk4)
        inverter0.append(inv0)
        inverter4.append(inv4)
        notand0.append(nand0)
        notand4.append(nand4)
        notor0.append(nor0)
        notor4.append(nor4)
        temperatures.append(temp)
        doses.append(dose)

  return clock0,clock4,inverter0,inverter4,notand0,notand4,notor0,notor4,doses,temperatures



def getRawRO(inputCSV):
  normalization = 1.
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
        clk0      = normalization*row[3]/nominalRow[3]
        clk4      = normalization*row[4]/nominalRow[4]
        inv0      = normalization*row[5]/nominalRow[5]
        inv4      = normalization*row[6]/nominalRow[6]
        nand0     = normalization*row[7]/nominalRow[7]
        nand4     = normalization*row[8]/nominalRow[8]
        nor0      = normalization*row[9]/nominalRow[9]
        nor4      = normalization*row[10]/nominalRow[10]

        clock0.append(clk0)
        clock4.append(clk4)
        inverter0.append(inv0)
        inverter4.append(inv4)
        notand0.append(nand0)
        notand4.append(nand4)
        notor0.append(nor0)
        notor4.append(nor4)
        temperatures.append(temp)
        doses.append(dose)

  return clock0,clock4,inverter0,inverter4,notand0,notand4,notor0,notor4,doses,temperatures

def getTempAndTime(inputCSV):
  with open(inputCSV) as csv_file:
    timestamps  =[]
    temperatures=[]
    nominalRow  = findNominalValues(inputCSV)
    csv_reader  = csv.reader(csv_file, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        timestamp = datetime.fromtimestamp(row[0])
        temp      = row[1]


        temperatures.append(temp)
        timestamps.append(timestamp)

  return timestamps,temperatures

def plotTempAndTime():
  C1Data = getTempAndTime("Chip1.csv")
  C2Data = getTempAndTime("Chip2.csv")
  C3Data = getTempAndTime("Chip3.csv")
  C4Data = getTempAndTime("Chip4.csv")
  C6Data = getTempAndTime("Chip6.csv")

  plt.plot(C1Data[0],C1Data[1],'o',label='Chip 1')
  plt.plot(C2Data[0],C2Data[1],'x',label='Chip 2')
  plt.plot(C3Data[0],C3Data[1],'v',label='Chip 3')
  plt.plot(C4Data[0],C4Data[1],'s',label='Chip 4')
  plt.plot(C6Data[0],C6Data[1],'D',label='Chip 6')
  plt.xlabel("Date", weight='bold',fontsize=20)
  plt.ylabel("Temperature [$^\circ$C]",weight='bold',fontsize=20)
  plt.gcf().autofmt_xdate()
  ax=plt.gca()
  ax.xaxis.set_major_locator(ticker.MultipleLocator(7))
  ax.tick_params(axis="x", labelsize=12)
  ax.tick_params(axis="y", labelsize=15)
  plt.legend(loc='upper right',fontsize='16',markerscale=2.0,framealpha=1.0)
  plt.show()




def plotCorrectedRO(driverPosition=0, outputFile='rawPlot.png',windowLength=5,markersize=9):
  c1Data = getCorrectedRO("Chip1_filtered.csv") #inverterClk,inverter,nand,nor,doses,temperatures
  c2Data = getCorrectedRO("Chip2_filtered.csv")
  c3Data = getCorrectedRO("Chip3_filtered.csv")
  c4Data = getCorrectedRO("Chip4_filtered.csv")
  c6Data = getCorrectedRO("Chip6_filtered.csv")



  c1Temp=round(np.average(c1Data[-1]))
  c2Temp=round(np.average(c2Data[-1]))
  c3Temp=round(np.average(c3Data[-1]))
  c4Temp=round(np.average(c4Data[-1]))
  c6Temp=round(np.average(c6Data[-1]))

  plt.xlabel("Dose[Mrad(SiO2)]",weight='bold',fontsize=12)
  plt.ylabel("RO pair difference change in relative frequency",weight='bold',fontsize=12)

  axes = plt.gca()
  #axes.set_xlim([xmin,xmax])
  #axes.set_ylim([-2.0,2.0])
  axes.set_xlim([-0.5,35])
  plt.grid(b=True, which='major', axis='both')
  plt.plot(c1Data[-2][windowLength:-windowLength:], np.convolve(c1Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'x',markersize=markersize, label=str(c1Temp)+str(' deg C'))
  plt.plot(c2Data[-2][windowLength:-windowLength:], np.convolve(c2Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'o',markersize=markersize, label=str(c2Temp)+str(' deg C'))
  plt.plot(c3Data[-2][windowLength:-windowLength:], np.convolve(c3Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, label=str(c3Temp)+str(' deg C'))
  #plt.plot(c4Data[-2][windowLength:-windowLength:], np.convolve(c4Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 's',markersize=markersize, label=str(c4Temp)+str(' deg C'))
  #plt.plot(c6Data[-2][windowLength:-windowLength:], np.convolve(c6Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], '*',markersize=markersize, label=str(c6Temp)+str(' deg C'))
  plt.legend(loc='best')
  plt.savefig(outputFile,dpi=200)
  plt.close()


def plotRawRO(driverPosition=0, outputFile='rawPlot.png',windowLength=5,markersize=9):
  rawC1Data = getRawRO("Chip1_filtered.csv")
  rawC2Data = getRawRO("Chip2_filtered.csv")
  rawC3Data = getRawRO("Chip3_filtered.csv")
  rawC4Data = getRawRO("Chip4_filtered.csv")
  rawC6Data = getRawRO("Chip6_filtered.csv")

  c1Temp=round(np.average(rawC1Data[-1]))
  c2Temp=round(np.average(rawC2Data[-1]))
  c3Temp=round(np.average(rawC3Data[-1]))
  c4Temp=round(np.average(rawC4Data[-1]))
  c6Temp=round(np.average(rawC6Data[-1]))


  markersize=9

  axes = plt.gca()
  plt.xlabel("Dose[Mrad(SiO2)]", weight='bold',fontsize=12)
  plt.ylabel("Normalized RO frequency",weight='bold',fontsize=12)
  #axes.set_xlim([xmin,xmax])
  #axes.set_ylim([98,105])
  axes.set_xlim([-0.5,35])
  plt.grid(b=True, which='major', axis='both')
  plt.text(3.,99.,'Average chip temperature\n in the legend label',fontsize=12, weight='bold')
  plt.plot(rawC1Data[-2][windowLength:-windowLength:], np.convolve(rawC1Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'd',markersize=markersize, markerfacecolor='none', label=str(c1Temp)+str(' deg C'))
  plt.plot(rawC2Data[-2][windowLength:-windowLength:], np.convolve(rawC2Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'o',markersize=markersize, markerfacecolor='none', label=str(c2Temp)+str(' deg C'))
  plt.plot(rawC3Data[-2][windowLength:-windowLength:], np.convolve(rawC3Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, markerfacecolor='none', label=str(c3Temp)+str(' deg C'))
  #plt.plot(rawC4Data[-2][windowLength:-windowLength:], np.convolve(rawC4Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, label=str(c4Temp)+str(' deg C'))
  #plt.plot(rawC6Data[-2][windowLength:-windowLength:], np.convolve(rawC6Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, label=str(c6Temp)+str(' deg C'))
  plt.legend(loc='best')
  plt.savefig(outputFile,dpi=200)
  plt.close()


def plotTimeDelays(driverPosition=0, outputFile='rawPlot.png',windowLength=5,markersize=9):
  rawC1Data = getTimeDelays("Chip1_filtered.csv")
  rawC2Data = getTimeDelays("Chip2_filtered.csv")
  rawC3Data = getTimeDelays("Chip3_filtered.csv")
  rawC4Data = getTimeDelays("Chip4_filtered.csv")
  rawC6Data = getTimeDelays("Chip6_filtered.csv")

  c1Temp=round(np.average(rawC1Data[-1]))
  c2Temp=round(np.average(rawC2Data[-1]))
  c3Temp=round(np.average(rawC3Data[-1]))
  c4Temp=round(np.average(rawC4Data[-1]))
  c6Temp=round(np.average(rawC6Data[-1]))


  markersize=9

  axes = plt.gca()
  plt.xlabel("Dose[Mrad(SiO2)]", weight='bold',fontsize=12)
  plt.ylabel("Normalized RO time delay percentage change",weight='bold',fontsize=12)
  #axes.set_xlim([xmin,xmax])
  #axes.set_ylim([98,105])
  axes.set_xlim([-0.5,35])
  plt.grid(b=True, which='major', axis='both')
  plt.text(3.,99.,'Average chip temperature\n in the legend label',fontsize=12, weight='bold')
  plt.plot(rawC1Data[-2][windowLength:-windowLength:], np.convolve(rawC1Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'd',markersize=markersize, markerfacecolor='none', label=str(c1Temp)+str(' deg C'))
  plt.plot(rawC2Data[-2][windowLength:-windowLength:], np.convolve(rawC2Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'o',markersize=markersize, markerfacecolor='none', label=str(c2Temp)+str(' deg C'))
  plt.plot(rawC3Data[-2][windowLength:-windowLength:], np.convolve(rawC3Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, markerfacecolor='none', label=str(c3Temp)+str(' deg C'))
  #plt.plot(rawC4Data[-2][windowLength:-windowLength:], np.convolve(rawC4Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, label=str(c4Temp)+str(' deg C'))
  #plt.plot(rawC6Data[-2][windowLength:-windowLength:], np.convolve(rawC6Data[driverPosition],np.ones(windowLength)/windowLength,mode='same')[windowLength:-windowLength:], 'v',markersize=markersize, label=str(c6Temp)+str(' deg C'))
  plt.legend(loc='best')
  plt.savefig(outputFile,dpi=200)
  plt.close()


# plotRawRO(0,'clk0.png')
# plotRawRO(1,'clk4.png')
# plotRawRO(2,'inv0.png')
# plotRawRO(3,'inv4.png')
# plotRawRO(4,'not0.png')
# plotRawRO(5,'not4.png')
# plotRawRO(6,'nor0.png')
# plotRawRO(7,'nor4.png')

# plotCorrectedRO(0,'clk.png')
# plotCorrectedRO(1,'inv.png')
# plotCorrectedRO(2,'nand.png')
# plotCorrectedRO(3,'nor.png')

plotTimeDelays(0,'clk0.png')


#plotCorrectedRO(0,'clk0.png')

#plotTempAndTime()