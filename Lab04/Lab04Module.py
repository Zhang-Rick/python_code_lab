#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/22/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from os import listdir
from os.path  import isfile, join
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('~ee364/DataFolder/Lab04')

def getDifference(provider1,provider2):
    filename1 = provider1 + '.dat'
    filename2 = provider2 + '.dat'
    onlyfiles = [f for f in listdir(DataPath + '/providers/') if isfile(join(DataPath + '/providers/', f))]
    if filename1 not in onlyfiles or filename2 not in onlyfiles:
        raise ValueError("ValueError")
        return  ValueError
    filename1 = os.path.join(DataPath, 'providers/' + filename1)
    filename2 = os.path.join(DataPath, 'providers/' + filename2)
    with open(filename1) as f1:
        line1 = f1.read().splitlines()
    with open(filename2) as f2:
        line2 = f2.read().splitlines()
    #print(line1,'\n',line2)
    array1 = []
    array2 = []
    i = 3
    while i < len(line1):
        board1 = list(filter(None,line1[i].split(' ')))[0] + ' ' + list(filter(None,line1[i].split(' ')))[1]
        array1.append(board1)
        board2 = list(filter(None,line2[i].split(' ')))[0] + ' ' + list(filter(None,line2[i].split(' ')))[1]
        array2.append(board2)
        i += 1
    #print(array1)
    answer = []
    i = 3
    while i < len(array1):
        if array1[i] not in array2:
            answer.append(array1[i])
        i +=1
    #print(answer)
    return answer

def getPriceOf(sbc,provider):
    filename1 = provider + '.dat'
    #filename2 = provider2 + '.dat'
    onlyfiles = [f for f in listdir(DataPath + '/providers/') if isfile(join(DataPath + '/providers/', f))]
    if filename1 not in onlyfiles:
        raise ValueError("ValueError")
        return  ValueError
    filename1 = os.path.join(DataPath, 'providers/' + filename1)
    #filename2 = os.path.join(DataPath, 'providers/' + filename2)
    with open(filename1) as f:
        line1 = f.read().splitlines()
    array1 = []
    i = 3
    while i < len(line1):
        board = list(filter(None,line1[i].split(' ')))[0] + ' ' + list(filter(None,line1[i].split(' ')))[1]
        array1.append(board)
        i +=1
    if sbc not in array1:
        raise ValueError("ValueError")
        return  ValueError
    i = 3
    while i < len(line1):
        board = list(filter(None, line1[i].split(' ')))[0] + ' ' + list(filter(None, line1[i].split(' ')))[1]
        #print(board,sbc,i)
        if board == sbc:
            price = float(list(filter(None, line1[i].split(' ')))[3].split('$')[1])
            #print(123)
            break
        i += 1
    #print(price)
    return  price

def checkAllPrices(sbcSet):
    onlyfiles = [f for f in listdir(DataPath + '/providers/') if isfile(join(DataPath + '/providers/', f))]
    i = 0
    SbcPriceMap = {}
    while i < len(onlyfiles):
        filename = DataPath + '/providers/' + onlyfiles[i]
        with open(filename) as f:
            lines = f.read().splitlines()
        j = 3
        while j < len(lines):
            k = 0#filelines index
            while k < len(sbcSet):
                board = list(filter(None,lines[j].split(' ')))[0] + ' ' + list(filter(None,lines[j].split(' ')))[1]
                price = float(list(filter(None, lines[j].split(' ')))[3].split('$')[1])
                if board == sbcSet[k] :
                    if sbcSet[k] not in SbcPriceMap.keys():
                        tuple1 = [price,onlyfiles[i]]
                        SbcPriceMap[sbcSet[k]] = tuple(tuple1)
                    elif sbcSet[k] in SbcPriceMap.keys() and price < SbcPriceMap[sbcSet[k]][0]:
                        tuple1 = [price, onlyfiles[i].split('.')[0]]
                        SbcPriceMap[sbcSet[k]] = tuple(tuple1)
                k +=1
            j += 1
        i += 1
    #print(SbcPriceMap)
    return SbcPriceMap

def getFilter():
    filename = DataPath + '/phones.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    i = 1
    array =[]
    while i < len(lines):
        phoneNum = list(filter(None,lines[i].split(' ')))[1].split(',')[1] + list(filter(None,lines[i].split(' ')))[2]
        phoneNum1 = phoneNum.split('(')[1].split(')')[0] +phoneNum.split('(')[1].split(')')[1]
        phoneNum2 = phoneNum1.split('-')[0] +phoneNum1.split('-')[1]
        array.append(phoneNum2)
        i += 1
    #print(array,'\n',len(array))
    j = 0
    array1 = []
    array4 =[]
    answerset = []
    while j < len(array):
        k = 0
        while k < 8:
            setanswer = array[j][k]+array[j][k+1]+array[j][k+2]
            #print(str(setanswer))
            array4.append(setanswer)
            answerset.append(setanswer)
            k += 1
        array1.append(answerset)
        answerset = []
        j += 1
    #print(array4,'\n',len(array4))
    i = 0
    array2 = []
    array3 = []
    array2 = array1

    while i < 99:
        k = 0

        print(array2,'\n',len(array2))
        array2.remove(array2[i])
        while k < 800:

            if array4[k-1] not in array2:
                array3.append(array4[k-1])
            k += 1
        array2 = array1
        print(len(array1),array1)
        i += 1
    #print(array2, '\n', len(array2))

if __name__ == "__main__":
    print(getDifference('provider1', 'provider2'))
    print(getPriceOf('Rasp. Pi-4702MQ', 'provider2'))
    sbcSet = ['Rasp. Pi-4810MQ','Rasp. Pi-4960HQ','Rasp. Pi-4710HQ']
    abc = checkAllPrices(sbcSet)
    print(abc)
    #getFilter()