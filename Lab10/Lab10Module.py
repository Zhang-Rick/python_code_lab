#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/22/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
from Lab10.measurement import calculateDistance


# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Lab10')
def getCost(sourceZip,destinationZip):
    filename = os.path.join(DataPath, 'coordinates.dat')
    with open(filename) as f:
        lines = f.read().splitlines()
    #print(lines)
    i = 1
    while i < len(lines):
        #print(lines[i].split('"')[5],lines[i].split('"')[7],lines[i].split('"')[9])
        zipcode = lines[i].split('"')[1]
        #print(zipcode)
        #print((lines[i].split(' ')[3].split('"')[0]))
        #print(lines[i].split(' ')[4].split('"')[1])
        if zipcode == sourceZip:
            sourceLati = float(lines[i].split('"')[5])
            #print(i,lines[i].split(' "')[3].split('"')[1])
            sourceLongti = float(lines[i].split('"')[7])
            #print(1,sourceLati,sourceLongti)
        if zipcode == destinationZip:
            destLati = float(lines[i].split('"')[5])
            destLongti = float(lines[i].split('"')[7])
            #print(2,destLati,destLongti)
        i += 1
    #distance = (sourceLati-destLati)**2.0+(sourceLongti-destLongti)**2.0
    #cost=distance**0.5
    #print(sourcelongti)
    cost = calculateDistance(tuple([sourceLati,sourceLongti]),tuple([destLati,destLongti]))
    return round(cost*0.01,2)
#countyLines = f.read().splitlines()
def loadpackages():
    filename = os.path.join(DataPath, 'packages.dat')
    with open(filename) as f:
        lines = f.read().splitlines()

    filename1 = os.path.join(DataPath, 'coordinates.dat')
    with open(filename1) as f:
        lines1 = f.read().splitlines()
    i = 1
    zipcode213 = []
    while i < len(lines1):
        zipcode213.append(lines1[i].split('"')[1])
        i += 1
    #print(zipcode213)
    i = 1
    list1=[]
    while i < len(lines):
        companyName = lines[i].split(' ')[0].split('"')[1]
        #print(companyName)
        if companyName not in list1:
            list1.append(companyName)
        i += 1
    #print(list1)
    j = 0
    list2=[]
    list1=sorted(list1)
    while j < len(list1):
        i = 1
        count = 0
        cost = 0
        while i < len(lines):
            if list1[j] == lines[i].split(' ')[0].split('"')[1]:
                count += 1
                source = lines[i].split('"')[3].split(' ')[-1]
                dest = lines[i].split('"')[-2].split(' ')[-1]
                #print(source,dest)
                if source in zipcode213 and dest in zipcode213:
                    cost+=getCost(source,dest)
                #print(cost)
            i += 1
        cost=round(cost,2)
        PackageGroup(list1[j],count,cost)
        list2.append(PackageGroup(list1[j],count,cost))
        j += 1

    return list2
class PackageGroup():
    def __init__(self,name,number,cost):
        self.name = name
        self.number = number
        self.cost = cost

    def __str__(self):
        if self.number < 10:
            number = "00"+str(self.number)
        elif (self.number < 100) and (self.number >= 10):
            number = "0" + str(self.number)
        return (f"{self.name}, {number} Shipments, Cost = ${self.cost}")

class Package():
        def __init__(self, source,destination):
            self.source = str(source)
            self.destination = str(destination)

            self.cost = round(calculateDistance(source,destination),2)



        def __str__(self):
            filename = os.path.join(DataPath, 'coordinates.dat')
            with open(filename) as f:
                lines = f.read().splitlines()
            # print(lines)
            i = 1
            while i < len(lines):
                sourceLati = float(lines[i].split('"')[5])
                #print(i,lines[i].split(' "')[3].split('"')[1])
                sourceLongti = float(lines[i].split('"')[7])
                if(self.source.split(',')[0]==sourceLati,self.source.split(',')[1]==sourceLongti):
                    zipcode1=lines[i].split('"')[1]
                if (self.destination.split(',')[0] == sourceLati, self.destination.split(',')[1] == sourceLongti):
                    zipcode2 = lines[i].split('"')[1]
                i += 1
            return (f"{zipcode1} => {zipcode1}, Cost = ${self.cost}")

        def __lt__(self, other):
                if not isinstance(other, Package):
                    raise TypeError("Comparison is not a valid TimeSpan class!")
                total1 = self.cost
                total2 = other.cost
                if total1 < total2:
                    return True
                return False

        def __le__(self, other):
                if not isinstance(other, Package):
                    raise TypeError("Comparison is not a valid TimeSpan class!")
                total1 = self.cost
                total2 = other.cost
                if total1 <= total2:
                    return True
                return False

        def __eq__(self, other):
                if not isinstance(other, Package):
                    raise TypeError("Comparison is not a valid TimeSpan class!")
                total1 = self.cost
                total2 = other.cost
                if total1 == total2:
                    return True
                return False

        def __ne__(self, other):
                if not isinstance(other, Package):
                    raise TypeError("Comparison is not a valid TimeSpan class!")
                total1 = self.cost
                total2 = other.cost
                if total1 != total2:
                    return True
                return False

        def __gt__(self, other):
                if not isinstance(other, Package):
                    raise TypeError("Comparison is not a valid TimeSpan class!")
                total1 = self.cost
                total2 = other.cost
                if total1 > total2:
                    return True
                return False

        def __ge__(self, other):
                if not isinstance(other, Package):
                    raise TypeError("Comparison is not a valid TimeSpan class!")
                total1 = self.cost
                total2 = other.cost
                if total1 >= total2:
                    return True

                return False



if __name__ == "__main__":
    print(getCost("99337", "35115"))
    loadpackages()
    print(tuple([1,2])[1])