#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/22/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('~ee364/DataFolder/Lab02')

def getCodeFor(stateName):
    filename = os.path.join(DataPath,'zip.dat')
    with open(filename,'r') as f:
        line = f.read().splitlines()
    #print(line[3].split(' '))
    i = 2
    array = []
    while i < len(line):
        state = line[i].split(' ')
        if stateName == state[0]:
            while stateName == state[0]:
                array.append(state[15])
                i += 1
                state = line[i].split(' ')
            break
        i += 1
    return sorted(array)

def getMinLatitude(stateName):
    array = getCodeFor(stateName)
    filename = os.path.join(DataPath,'coordinates.dat')
    with open(filename,'r') as f:
        line = f.read().splitlines()
    start =find(array[0])
    finish = find(array[len(array) - 1])
    #print(line[start].split(' '))
    min = float(line[start].split(' ')[0])
    while (start <= finish):
        if float(line[start].split(' ')[0]) < min:
            min = float(line[start].split(' ')[0])
        start += 1
    return min

def getMaxLongitude(stateName):
    array = getCodeFor(stateName)
    filename = os.path.join(DataPath,'coordinates.dat')
    with open(filename,'r') as f:
        line = f.read().splitlines()
    start =find(array[0])
    finish = find(array[len(array) - 1])
    max = float(line[start].split(' ')[9])
    while (start <= finish):
        if float(line[start].split(' ')[9]) > max:
            max = float(line[start].split(' ')[9])
        start += 1
    return max



def find(zipcode):
    filename = os.path.join(DataPath,'coordinates.dat')
    with open(filename,'r') as f:
        line = f.read().splitlines()
    i = 2
    while i < len(line):
        zip = line[i].split(' ')
        if (zip[len(zip) - 1] == zipcode):
            return i
        i += 1

def getSubMatrixSum(startRowIndex,endRowIndex,startColumnIndex,endColumnIndex):
    filename = os.path.join(DataPath,'matrix.dat')
    with open(filename,'r') as f:
        line = f.read().splitlines()
    #print(line[0],'\n')
    #print(line[1],'\n')
    sum = 0
    i = 1
    startColumnIndex -= 1
    startRowIndex -= 1
    j = startColumnIndex
    while startRowIndex < endRowIndex:
        array = line[startRowIndex]
        #print(startRowIndex)
        #print(endRowIndex)
        #print(array)
        while j < endColumnIndex:
            #print(array.split(' '))
            #print(startColumnIndex)
            #print(endColumnIndex)
            num = int(array.split(' ')[j])
            #print(num)
            sum += num
            j += 1
        j =startColumnIndex
        startRowIndex += 1
    return sum



#if __name__  == "__main__":
    #print(getCodeFor('Florida'))
    #find(47906)
    #print(getMinLatitude('Florida'))
    #print(getMaxLongitude('Florida'))
    #print(getSubMatrixSum(1,2,3,4))