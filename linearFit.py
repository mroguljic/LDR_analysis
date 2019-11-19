import numpy as np
import matplotlib.pyplot as plt
from chipsComparison import *

def linearFitRaw(ROpos,outputFile,title,skipFirstN=400):

    c1Data = getRawRO("Chip1_filtered.csv") #return clock0,clock4,inverter0,inverter4,notand0,notand4,notor0,notor4,doses,temperatures
    c2Data = getRawRO("Chip2_filtered.csv")
    c3Data = getRawRO("Chip3_filtered.csv")
    c4Data = getRawRO("Chip4_filtered.csv")
    c6Data = getRawRO("Chip6_filtered.csv")


    c1x = c1Data[-2]
    c1y = c1Data[ROpos]
    c2x = c2Data[-2]
    c2y = c2Data[ROpos]
    c3x = c3Data[-2]
    c3y = c3Data[ROpos]
    c4x = c4Data[-2]
    c4y = c4Data[ROpos]
    c6x = c6Data[-2]
    c6y = c6Data[ROpos]

    c1Temp = round(np.mean(c1Data[-1]))
    c2Temp = round(np.mean(c2Data[-1]))
    c3Temp = round(np.mean(c3Data[-1]))
    c4Temp = round(np.mean(c4Data[-1]))
    c6Temp = round(np.mean(c6Data[-1]))


    coef1 = np.polyfit(c1x[skipFirstN:],c1y[skipFirstN:],1)
    coef2 = np.polyfit(c2x[skipFirstN:],c2y[skipFirstN:],1)
    coef3 = np.polyfit(c3x[skipFirstN:],c3y[skipFirstN:],1)
    coef4 = np.polyfit(c4x[skipFirstN:],c4y[skipFirstN:],1)
    coef6 = np.polyfit(c6x[skipFirstN:],c6y[skipFirstN:],1)

#    print("Chip 1 at {0} degrees, slope A = {1:.2g}".format(c1Temp,coef1[0]))
#    print("Chip 2 at {0} degrees, slope A = {1:.2g}".format(c2Temp,coef2[0]))
#    print("Chip 3 at {0} degrees, slope A = {1:.2g}".format(c3Temp,coef3[0]))
    print("Chip 4 at {0} degrees, slope A = {1:.2g}".format(c4Temp,coef4[0]))
    print("Chip 6 at {0} degrees, slope A = {1:.2g}".format(c6Temp,coef6[0]))


    fn1 = np.poly1d(coef1) 
    fn2 = np.poly1d(coef2) 
    fn3 = np.poly1d(coef3) 
    fn4 = np.poly1d(coef4) 
    fn6 = np.poly1d(coef6) 
    # poly1d_fn is now a function which takes in x and returns an estimate for y

    plt.cla()
    plt.clf()


    markersize = 10
    markeredgewidth = 1

#    plt.plot(c1x[::50],c1y[::50], 'kv', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef1[0]))
#    plt.plot(c2x[::50],c2y[::50], 'ro', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef2[0]))
#    plt.plot(c3x[::50],c3y[::50], 'gs', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef3[0]))
    plt.plot(c4x[::50],c4y[::50], 'bo', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef4[0]))
    plt.plot(c6x[::50],c6y[::50], 'ko', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef6[0]))

#    plt.plot(c1x, fn1(c1x), '--k')
#    plt.plot(c2x, fn2(c2x), '--r')
#    plt.plot(c3x, fn3(c3x), '--g')
    plt.plot(c4x, fn4(c4x), '--k')
    plt.plot(c6x, fn6(c6x), '--k')
    plt.title(title)
    plt.legend(loc='best')
    plt.savefig(outputFile,dpi=200)



def linearFitCorrected(ROpos,outputFile,title,skipFirstN=400):

    c1Data = getCorrectedRO("Chip1_filtered.csv") #inverterClk,inverter,nand,nor,doses,temperatures
    c2Data = getCorrectedRO("Chip2_filtered.csv")
    c3Data = getCorrectedRO("Chip3_filtered.csv")
    c4Data = getCorrectedRO("Chip4_filtered.csv")
    c6Data = getCorrectedRO("Chip6_filtered.csv")


    c1x = c1Data[-2]
    c1y = c1Data[ROpos]
    c2x = c2Data[-2]
    c2y = c2Data[ROpos]
    c3x = c3Data[-2]
    c3y = c3Data[ROpos]
    c4x = c4Data[-2]
    c4y = c4Data[ROpos]
    c6x = c6Data[-2]
    c6y = c6Data[ROpos]

    c1Temp = round(np.mean(c1Data[-1]))
    c2Temp = round(np.mean(c2Data[-1]))
    c3Temp = round(np.mean(c3Data[-1]))
    c4Temp = round(np.mean(c4Data[-1]))
    c6Temp = round(np.mean(c6Data[-1]))


    coef1 = np.polyfit(c1x[skipFirstN:],c1y[skipFirstN:],1)
    coef2 = np.polyfit(c2x[skipFirstN:],c2y[skipFirstN:],1)
    coef3 = np.polyfit(c3x[skipFirstN:],c3y[skipFirstN:],1)
    coef4 = np.polyfit(c4x[skipFirstN:],c4y[skipFirstN:],1)
    coef6 = np.polyfit(c6x[skipFirstN:],c6y[skipFirstN:],1)

#    print("Chip 1 at {0} degrees, slope A = {1:.2g}".format(c1Temp,coef1[0]))
#    print("Chip 2 at {0} degrees, slope A = {1:.2g}".format(c2Temp,coef2[0]))
#    print("Chip 3 at {0} degrees, slope A = {1:.2g}".format(c3Temp,coef3[0]))
    print("Chip 4 at {0} degrees, slope A = {1:.2g}".format(c4Temp,coef4[0]))
    print("Chip 6 at {0} degrees, slope A = {1:.2g}".format(c6Temp,coef6[0]))


    fn1 = np.poly1d(coef1) 
    fn2 = np.poly1d(coef2) 
    fn3 = np.poly1d(coef3) 
    fn4 = np.poly1d(coef4) 
    fn6 = np.poly1d(coef6) 
    # poly1d_fn is now a function which takes in x and returns an estimate for y

    plt.cla()
    plt.clf()


    markersize = 10
    markeredgewidth = 1

#    plt.plot(c1x[::50],c1y[::50], 'kv', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef1[0]))
#    plt.plot(c2x[::50],c2y[::50], 'ro', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef2[0]))
#    plt.plot(c3x[::50],c3y[::50], 'gs', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef3[0]))
    plt.plot(c4x[::50],c4y[::50], 'bo', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef4[0]))
    plt.plot(c6x[::50],c6y[::50], 'ko', markerfacecolor='none', markersize=markersize, markeredgewidth = markeredgewidth,  label='Slope = {0:.2g}'.format(coef6[0]))

#    plt.plot(c1x, fn1(c1x), '--k')
#    plt.plot(c2x, fn2(c2x), '--r')
#    plt.plot(c3x, fn3(c3x), '--g')
    plt.plot(c4x, fn4(c4x), '--k')
    plt.plot(c6x, fn6(c6x), '--k')
    plt.title(title)
    plt.legend(loc='best')
    plt.savefig(outputFile,dpi=200)


correctedTitles=["clk","inv","nand","nor"]
for i, title in enumerate(correctedTitles):
    linearFitCorrected(i,"fitsRoom/"+title+".png",title)

rawTitles=["clk0","clk4","inv0","inv4","nand0","nand4","nor0","nor4"]
for i, title in enumerate(rawTitles):
    linearFitRaw(i,"fitsRoom/"+title+".png",title)