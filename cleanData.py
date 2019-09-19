import csv

def filterData(filename,outlierValue=5):
    lines=[]
    with open(filename+'.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        lines = [row for row in csvreader]
        outlierIndices = []
        for i,line in enumerate(lines):
            if(i<2):
                continue
            roM2= int(lines[i-2][3])
            roM1= int(lines[i-1][3])
            ro  = int(lines[i][3])
            if(abs(ro-roM1)>outlierValue and abs(ro-roM2)>outlierValue):
                print('Outlier on line '+str(i))
                print(lines[i-2])
                print(lines[i-1])
                print(lines[i])
                print('----------')
                outlierIndices.append(i)
        deleteQuestion = input('Delete lines '+str(outlierIndices)+'? y/N\n')
        if(deleteQuestion=='y'):
            for i in outlierIndices[::-1]: #has to go in reverse so the deleting doesn't change the indices of the other outliers
                del lines[i]
        else:
            print('Exiting')
            return
    print('Saving list cleared from outliers to '+filename+'_filtered.csv')
    with open(filename+'_filtered.csv', 'w') as filteredFile:
        wr = csv.writer(filteredFile, quoting=csv.QUOTE_NONE)
        for line in lines:
            wr.writerow(line)



filterData('Chip1',5)
filterData('Chip2',5)
filterData('Chip3',5)
filterData('Chip4',5)
filterData('Chip6',5)
