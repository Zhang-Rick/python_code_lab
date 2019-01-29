#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/29/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from collections import Counter
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('~ee364/DataFolder/Lab03')

def getStateByCounty(countyName):
    filename = os.path.join(DataPath, 'counties.dat')
    with open(filename) as f:
        countyLines = f.read().splitlines()
    CountyPosition = {}
    i = 2
    #print(countyLines)
    while i < len(countyLines):
        county = list(filter(None,countyLines[i].split(' ')))
        if len(county) >= 4:
            county[2] =county[2]+' '+county[3]
            county[3] = None
        #print(county)
        if  county[2] not in CountyPosition.keys():
            CountyPosition[county[2]] = [[county[0],county[1]]]
        else:
            CountyPosition[county[2]].append([county[0],county[1]])
        i += 1
    #print(CountyPosition)
    filename2 = os.path.join(DataPath, 'coordinates.dat')
    with open(filename2) as f:
        coordinateLines = f.read().splitlines()
    statePosition = {}
    i = 2
    while i < len(coordinateLines):
        state = list(filter(None,coordinateLines[i].split(' ')))
        #print(county)
        if state[2] not in statePosition.keys():
            statePosition[state[2]] = [state[0],state[1]]
        else:
            statePosition[state[2]].append([state[0],state[1]])
        i += 1
    #print(' ',statePosition)
    array = []
    j = 0
    #print(list(statePosition.keys())[2])
    while j < len(statePosition.keys()):
        #print(list(statePosition.keys())[j],CountyPosition[countyName])
        if statePosition[list(statePosition.keys())[j]] in CountyPosition[countyName]:
            array.append(list(statePosition.keys())[j])

        j += 1
    #print(array)
    filename3 = os.path.join(DataPath, 'zip.dat')
    with open(filename3) as f:
        zipLines = f.read().splitlines()
    zipState = {}
    i = 2
    while i < len(zipLines):
        zip = list(filter(None,zipLines[i].split(' ')))
        if len(zip) >= 4:
            zip[0] = zip[0] + ' ' + zip[1]
            zip[2] = zip[3]
        # print(county)
        #print(county)
        zipState[zip[2]] = zip[0]
        i += 1
    #print(zipState)
    i = 0
    answer = []
    while i < len(array):
        if zipState[array[i]] not in answer:
            answer.append(zipState[array[i]])
        i += 1
    #print(answer)
    return answer

def getCount(stateName2):
    filename2 = os.path.join(DataPath, 'coordinates.dat')
    with open(filename2) as f:
        coordinateLines = f.read().splitlines()
    statePosition = {}
    i = 2
    while i < len(coordinateLines):
        state = list(filter(None, coordinateLines[i].split(' ')))
        # print(county)
        if state[2] not in statePosition.keys():
            statePosition[state[2]] = [state[0], state[1]]
        else:
            statePosition[state[2]].append([state[0], state[1]])
        i += 1
    #print(statePosition)
    filename = os.path.join(DataPath, 'counties.dat')
    with open(filename) as f:
        countyLines = f.read().splitlines()
    CountyPosition = {}
    i = 2
    # print(countyLines)
    while i < len(countyLines):
        county = list(filter(None, countyLines[i].split(' ')))
        if len(county) >= 4:
            county[2] = county[2] + ' ' + county[3]
            county[3] = None
        # print(county)
        if county[2] not in CountyPosition.keys():
            CountyPosition[county[2]] = [[county[0], county[1]]]
        else:
            CountyPosition[county[2]].append([county[0], county[1]])
        i += 1
    #print(CountyPosition)
    filename3 = os.path.join(DataPath, 'zip.dat')
    with open(filename3) as f:
        zipLines = f.read().splitlines()
    zipState = {}
    i = 2
    while i < len(zipLines):
        zip = list(filter(None,zipLines[i].split(' ')))
        if len(zip) >= 4:
            zip[0] = zip[0] + ' ' + zip[1]
            zip[2] = zip[3]
        # print(county)
        #print(county)
        zipState[zip[2]] = zip[0]
        i += 1
    #print(zipState)
    i = 0
    array5 = []
    while i < len(zipState.keys()):
        if zipState[list(zipState.keys())[i]] == stateName2:
            array5.append(list(zipState.keys())[i])
        i +=1
    #print(array5)
    if array5 == []:
        raise ValueError("ValueError")
        return ValueError
    i = 0
    array6 =[]
    while i < len(array5):
        array6.append(statePosition[array5[i]])
        i += 1
    #print(array6)
    i = 0
    j = 0
    answer= []
    while j < len(array6):
        i = 0
        while i < len(CountyPosition):
            if array6[j] in CountyPosition[list(CountyPosition.keys())[i]]:
                if list(CountyPosition.keys())[i] not in answer:
                    answer.append(list(CountyPosition.keys())[i])
            i += 1
        j += 1
    #print(answer,'\n',len(answer))
    return answer
    #if state not in statePosition.keys():
        #raise ValueError("ValueErroe")
def getReport():
    filename3 = os.path.join(DataPath, 'students.dat')
    with open(filename3) as f:
        studentsLines = f.read().splitlines()
    StudentsExtensionMap = {}
    i = 2
    while i < len(studentsLines):
        extension = list(filter(None,studentsLines[i].split(' ')))[3]
        Name = list(filter(None,studentsLines[i].split(' ')))[0] + ' ' + list(filter(None,studentsLines[i].split(' ')))[1]
        StudentsExtensionMap[Name] = list(filter(None,studentsLines[i].split(' ')))[3].split('x')[1]
        i += 1
    #print(StudentsExtensionMap)
    PhoneDurationMap = {}
    DurationPhoneMap = {}
    filename4 = os.path.join(DataPath, 'calls.dat')
    with open(filename4) as f:
        callsLines = f.read().splitlines()
    i = 2
    while i < len(callsLines):
        Duration = list(filter(None,callsLines[i].split(' ')))[2]
        extension = list(filter(None,callsLines[i].split(' ')))[0].split('-')[2]
        #print(Duration,' ',extension)
        PhoneDurationMap[extension] = Duration
        DurationPhoneMap[Duration] = extension
        i += 1
    ExtensionTimesMap = {}
    i = 0
    while i < len(DurationPhoneMap.keys()):
        if type(ExtensionTimesMap[DurationPhoneMap[list(DurationPhoneMap.keys())[i]]]) == type(1):
            ExtensionTimesMap[DurationPhoneMap[list(DurationPhoneMap.keys())[i]]] += 1
        else:
            ExtensionTimesMap[DurationPhoneMap[list(DurationPhoneMap.keys())[i]]] = 1
        i += 1
    print(ExtensionTimesMap)

#if __name__  == "__main__":
    #getStateByCounty('Coshocton')
    #getCount('Illinois')
    #getReport()
    #find(47906)
    #print(getMinLatitude('Florida'))
    #print(getMaxLongitude('Florida'))
    #print(getSubMatrixSum(1,2,3,4))