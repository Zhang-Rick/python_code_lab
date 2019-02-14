#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <02/13/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from os import listdir
from os.path  import isfile, join
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

DataPath = os.path.expanduser('~ee364/DataFolder/Lab05')

def peopleToID():
    filename = DataPath + '/people.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    #print(lines)
    i = 2
    peopleToIDMap = {}
    while i < len(lines):
        name = list(filter(None,lines[i].split(' ')))[0] + ' ' + list(filter(None,lines[i].split(' ')))[1]
        ID = list(filter(None,lines[i].split(' ')))[-1]
        peopleToIDMap[name] = ID
        #print(name,ID)
        i += 1
    #print(peopleToIDMap)
    return peopleToIDMap

def IDToPin():
    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    #ID = []
    IDToPinMap ={}
    i = 3
    while i < len(lines):
        ID = list(filter(None,lines[i].split(' ')))[0]
        pins = list(filter(None,lines[i].split(' ')))
        pins.remove(list(filter(None,lines[i].split(' ')))[0])
        IDToPinMap[ID] = pins
        i += 1
    #print(ID,'\n',len(ID))
    #print(IDToPinMap)
    return  IDToPinMap

def DataArray():
    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    date = list(filter(None, lines[1].split(' ')))
    date.remove('ID')
    #print(date)
    return date

def getPinFor(name,date):
    peopleToIDMap =peopleToID()
    IDToPinMap = IDToPin()
    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    date1 = list(filter(None, lines[1].split(' ')))
    date1.remove('ID')
    #print(date)
    #print(peopleToIDMap,'\n',IDToPinMap)
    if date not in date1 or name not in  peopleToIDMap.keys():
        raise ValueError("ValueError!")
        return  ValueError
    ID = peopleToIDMap[name]
    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    #ID = []
    i = 3
    while i < len(lines):
        ID1 = list(filter(None,lines[i].split(' ')))[0]
        if ID1 == ID:
            Code = IDToPinMap[ID]
        i += 1
    #print(Code)
    i = 0
    while i < len(Code):
        if date1[i] == date:
            answer = Code[i]
        i += 1
    return answer

def getUserOf(pin,date):
    peopleToIDMap =peopleToID()
    IDToPinMap = IDToPin()
    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    date1 = list(filter(None, lines[1].split(' ')))
    date1.remove('ID')
    pinsset = sum(IDToPinMap.values(),[])
    #print(pinsset)
    if date not in date1 or pin not in  pinsset:
        raise ValueError("ValueError!")
        return  ValueError
    i = 0
    while i < len(date1):
        if date1[i] == date:
            index = i
            break
        i += 1
    #print(index)


    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    #ID = []
    ID1ToPinMap ={}
    i = 3
    while i < len(lines):
        PIN = list(filter(None,lines[i].split(' ')))[index+1]
        ID = list(filter(None, lines[i].split(' ')))[0]
        ID1ToPinMap[ID] = PIN
        i += 1
    #print(ID1ToPinMap)
    inverseID1Map = dict(zip(ID1ToPinMap.values(),ID1ToPinMap.keys()))
    print(inverseID1Map.keys())
    answer = inverseID1Map[pin]
    inversePeopletoIDMap =dict(zip(peopleToIDMap.values(),peopleToIDMap.keys()))
    print(inversePeopletoIDMap[answer])
    return inversePeopletoIDMap[answer]

def getUsersOn(date):
    peopleToIDMap =peopleToID()
    IDToPinMap = IDToPin()
    filename = DataPath + '/pins.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    date1 = list(filter(None, lines[1].split(' ')))
    date1.remove('ID')
    pinsset = sum(IDToPinMap.values(),[])
    #print(pinsset)
    if date not in date1:
        raise ValueError("ValueError!")
        return  ValueError
    filename = DataPath + "/log.dat"
    with open(filename) as f:
        lines = f.read().splitlines()
    #print(lines[3])
    pinlist =[]
    i = 3
    while i < len(lines):
        date12 = list(filter(None,lines[i].split(' ')))[0]
        Pin = list(filter(None,lines[i].split(' ')))[-1]
        #print(date)
        if date == date12:
            pinlist.append(Pin)
        i += 1
    #print(len(pinlist),pinlist)
    Name = []
    i = 0
    #print(date1)
    while i < len(pinlist):
        j = 0
        while j < len(date1):
            Name.append(getUserOf(pinlist[i],date1[j]))
            print(Name)
            j += 1
        i += 1
    return Name

def getDifference(slot1,slot2):
    filename = DataPath + '/slots.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    slots = list(filter(None,lines[1].split(' ')))
    slots.remove('ID')
    #print(slots)
    i = 3
    array1 =[]
    array2 =[]
    array3 =[]
    array4 =[]
    array5 =[]
    while i < len(lines):
        if list(filter(None,lines[i].split(' ')))[1] == '1':
            array1.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[2] == '1':
            array2.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[3] == '1':
            array3.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[4] == '1':
            array4.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[5] == '1':
            array5.append(list(filter(None,lines[i].split(' ')))[0])
        i += 1
    slotMap ={}
    bigarray =[array1,array2,array3,array4,array5]
    i = 0
    while i < 5:
        slotMap[slots[i]] = bigarray[i]
        i +=1
    #print(slotMap(slot1))
    answer = set(slotMap[slot1]) - set(slotMap[slot2])
    return len(answer)
def getCommon(slot1,slot2):
    filename = DataPath + '/slots.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    slots = list(filter(None,lines[1].split(' ')))
    slots.remove('ID')
    #print(slots)
    i = 3
    array1 =[]
    array2 =[]
    array3 =[]
    array4 =[]
    array5 =[]
    while i < len(lines):
        if list(filter(None,lines[i].split(' ')))[1] == '1':
            array1.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[2] == '1':
            array2.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[3] == '1':
            array3.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[4] == '1':
            array4.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[5] == '1':
            array5.append(list(filter(None,lines[i].split(' ')))[0])
        i += 1
    slotMap ={}
    bigarray =[array1,array2,array3,array4,array5]
    i = 0
    while i < 5:
        slotMap[slots[i]] = bigarray[i]
        i += 1
    # print(slotMap(slot1))
    answer = set(slotMap[slot1]).intersection(set(slotMap[slot2]))
    return len(answer)
def getMissing(slots):
    filename = DataPath + '/slots.dat'
    with open(filename) as f:
        lines = f.read().splitlines()
    slots = list(filter(None,lines[1].split(' ')))
    slots.remove('ID')
    #print(slots)
    i = 3
    array1 =[]
    array2 =[]
    array3 =[]
    array4 =[]
    array5 =[]
    while i < len(lines):
        if list(filter(None,lines[i].split(' ')))[1] == '1':
            array1.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[2] == '1':
            array2.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[3] == '1':
            array3.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[4] == '1':
            array4.append(list(filter(None,lines[i].split(' ')))[0])
        if list(filter(None, lines[i].split(' ')))[5] == '1':
            array5.append(list(filter(None,lines[i].split(' ')))[0])
        i += 1
    slotMap ={}
    bigarray =[array1,array2,array3,array4,array5]
    i = 0
    while i < 5:
        slotMap[slots[i]] = bigarray[i]
        i += 1
    i = 0
    answer = []
    while i < len(slots):
        answer.append(slotMap[slots[i]])
        i += 1
    answer = sum(answer,[])
    #print(len(set(answer)))
    num = len(lines) - 3
    #print(num- len(set(answer)))
    return num- len(set(answer))
if __name__ == "__main__":
    #peopleToID()
    #IDToPin()
    #DataArray()
    #DataArray()
    #a = getPinFor('Bailey, Catherine','03/18')
    #print(type(a))
    #print(getUserOf('710','03/18'))
    #getUsersOn('04/15')
    #getDifference('11:30AM-01:20PM', '01:30PM-03:20PM')
    #getCommon('01:30PM-03:20PM', '03:30PM-05:20PM')
    getMissing(['11:30AM-01:20PM', '01:30PM-03:20PM', '03:30PM-05:20PM'])