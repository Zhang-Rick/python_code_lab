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
DataPath = os.path.expanduser('~ee364/DataFolder/Lab13')
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
        PackageGroup213(list1[j],count,cost)
        list2.append(PackageGroup213(list1[j],count,cost))
        j += 1

    return list2
class PackageGroup213():
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
        def __init__(self,company, source,destination):
            self.company = company
            self.source = source
            self.destination = destination
            #print(float(source),float(destination))
            source1 = source.split(',')[0].split("(")[1]
            #print(source1)
            source2 = source.split(',')[1].split(")")[0].split(' ')[1]
            #print(source2)
            source3=tuple([float(source1),float(source2)])

            destination1 = destination.split(',')[0].split("(")[1]
            #print(source1)
            destination2 = destination.split(',')[1].split(")")[0].split(' ')[1]
            #print(source2)
            destination3=tuple([float(destination1),float(destination2)])

            self.cost = round(calculateDistance(source3,destination3),2)



        def __str__(self):
            filename = os.path.join(DataPath, 'coordinates.dat')
            with open(filename) as f:
                lines = f.read().splitlines()
            # print(lines)
            i = 1
            while i < len(lines):
                sourceLati = list(filter(None, lines[i].split('"')[5].split(' ')))[0]
                #print(i,lines[i].split(' "')[3].split('"')[1])
                sourceLongti = list(filter(None, lines[i].split('"')[7].split(' ')))[0]
                #print(sourceLati,sourceLongti)
                #print(self.source.split(',')[1].split(")")[0].split(' ')[1],sourceLongti,self.source.split(',')[1].split(")")[0].split(' ')[1]==sourceLongti)
                if(self.source.split(',')[0].split("(")[1]==sourceLati and self.source.split(',')[1].split(")")[0].split(' ')[1]==sourceLongti):
                    zipcode1=lines[i].split('"')[1]
                    #print(zipcode1)
                if (self.destination.split(',')[0].split("(")[1] == sourceLati and self.destination.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    zipcode2 = lines[i].split('"')[1]
                    #print(zipcode2)
                i += 1
            return (f"{zipcode1} => {zipcode1}, Cost = ${self.cost}")

        def __add__(self, other):
            if not isinstance(other, PackageGroup):
                raise TypeError("This is not a package Class!")
            if isinstance(other, Package):
                raise ValueError("They are same Class!")
            if self in other.packages:
                return other
            else:
                packages123 = []
                for elements in other.packages:
                    packages123.append(elements)
                packages123.append(self)
                other.packages = set(packages123)
                other.cost += self.cost


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

class PackageGroup():
    def __init__(self,name,packages,cost=None):
        self.name = name
        self.packages = sorted(packages,reverse=True)
        totalcost = 0
        for element in self.packages:
            totalcost += element.cost
        #print(totalcost)
        self.cost = totalcost

    def __str__(self):
        number=len(self.packages)

        if number < 10:
            number = "00"+str(number)
        elif (number < 100) and (number >= 10):
            number = "0" + str(number)
        return (f"{self.name}, {number} Shipments, Cost = ${self.cost}")

    def getByZip(self,setZipcode):
        if setZipcode == None :
            raise ValueError("it should not be empty")
        listZipcode =[]
        list2=[]
        filename = os.path.join(DataPath, 'coordinates.dat')
        with open(filename) as f:
            lines = f.read().splitlines()
        for element in setZipcode:
            listZipcode.append(element)
        for elements in self.packages:

            # print(lines)
            i = 1
            zipcode1 = 0
            zipcode2 = 1
            while i < len(lines):
                sourceLati = list(filter(None, lines[i].split('"')[5].split(' ')))[0]
                # print(i,lines[i].split(' "')[3].split('"')[1])
                sourceLongti = list(filter(None, lines[i].split('"')[7].split(' ')))[0]
                # print(sourceLati,sourceLongti)
                # print(self.source.split(',')[1].split(")")[0].split(' ')[1],sourceLongti,self.source.split(',')[1].split(")")[0].split(' ')[1]==sourceLongti)
                if (elements.source.split(',')[0].split("(")[1] == sourceLati and
                        elements.source.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    zipcode1 = lines[i].split('"')[1]
                    # print(zipcode1)
                if (elements.destination.split(',')[0].split("(")[1] == sourceLati and
                        elements.destination.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    zipcode2 = lines[i].split('"')[1]
                    # print(zipcode2)
                i += 1
            if zipcode1 in listZipcode and zipcode2 in listZipcode:
                list2.append(elements)
        return  list2

    def getByState(self, setState):
        if setState == None :
            raise ValueError("it should not be empty")
        listState =[]
        list2=[]
        filename = os.path.join(DataPath, 'coordinates.dat')
        with open(filename) as f:
            lines = f.read().splitlines()
        for element in setState:
            listState.append(element)
        for elements in self.packages:

            # print(lines)
            i = 1
            state1 = 0
            state2 = 1
            while i < len(lines):
                sourceLati = list(filter(None, lines[i].split('"')[5].split(' ')))[0]
                # print(i,lines[i].split(' "')[3].split('"')[1])
                sourceLongti = list(filter(None, lines[i].split('"')[7].split(' ')))[0]
                # print(sourceLati,sourceLongti)
                # print(self.source.split(',')[1].split(")")[0].split(' ')[1],sourceLongti,self.source.split(',')[1].split(")")[0].split(' ')[1]==sourceLongti)
                if (elements.source.split(',')[0].split("(")[1] == sourceLati and
                        elements.source.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    state1 = lines[i].split('"')[-2]
                    #print(state1)
                if (elements.destination.split(',')[0].split("(")[1] == sourceLati and
                        elements.destination.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    state2 = lines[i].split('"')[-2]
                    # print(zipcode2)
                i += 1
            if state1 in listState and state2 in listState:
                list2.append(elements)
        return  list2
    def getByCity(self, setCity):
        if setCity == None :
            raise ValueError("it should not be empty")
        listCity =[]
        list2=[]
        filename = os.path.join(DataPath, 'coordinates.dat')
        with open(filename) as f:
            lines = f.read().splitlines()
        for element in setCity:
            listCity.append(element)
        for elements in self.packages:

            # print(lines)
            i = 1
            city1 = 0
            city2 = 1
            while i < len(lines):
                sourceLati = list(filter(None, lines[i].split('"')[5].split(' ')))[0]
                # print(i,lines[i].split(' "')[3].split('"')[1])
                sourceLongti = list(filter(None, lines[i].split('"')[7].split(' ')))[0]
                # print(sourceLati,sourceLongti)
                # print(self.source.split(',')[1].split(")")[0].split(' ')[1],sourceLongti,self.source.split(',')[1].split(")")[0].split(' ')[1]==sourceLongti)
                if (elements.source.split(',')[0].split("(")[1] == sourceLati and
                        elements.source.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    city1 = lines[i].split('"')[-4]
                    print(city1)
                if (elements.destination.split(',')[0].split("(")[1] == sourceLati and
                        elements.destination.split(',')[1].split(")")[0].split(' ')[1] == sourceLongti):
                    city2 = lines[i].split('"')[-4]
                    # print(zipcode2)
                i += 1
            if city1 in listCity and city2 in listCity:
                list2.append(elements)
        return  list2
    def __contains__(self,other):
        if not isinstance(other, Package):
            raise TypeError("This is not a package Class!")
        for elements in self.packages:
            #print(elements.company,elements.source,elements.destination)
            if elements.company == other.company and elements.source == other.source and elements.destination == other.destination:
                return True
        return False

    def __add__(self, other):
        if not isinstance(other,Package):
            raise TypeError("This is not a package Class!")
        if isinstance(other, PackageGroup):
            raise ValueError("They are same Class!")
        if other in self.packages:
            return self
        else:
            packages123=[]
            for elements in self.packages:
                packages123.append(elements)
            packages123.append(other)
            self.packages=set(packages123)
            self.cost += other.cost
if __name__ == "__main__":
    print(getCost("99337", "35115"))
    a=loadpackages()
    b=33.606379
    c=-86.50249
    b = str(tuple([b,c]))

    e = 32.903432
    f = -85.92669
    g=str(tuple([e,f]))
    d = Package('123',b, g)
    print(d)
    a= [12,32,465]
    l=PackageGroup('123',[d,d])
    print(l)
    k=set(['Moody','Alexander City'])
    print(l.getByCity(k)[0])
    print(d in l)