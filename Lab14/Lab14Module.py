import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
import re
import os
import copy
import collections
import enum
from enum import Enum
from Lab14.measurement import calculateDistance
import copy
import collections
#from Lab10.measurement import calculateDistance
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Lab14')


class Direction(Enum):
    Incoming = 1
    Outgoing = 2
    Both = 3

class Leg():
    def __init__(self,source,destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        pattern = "[0-9]{5}"
        matchS = re.search(pattern,self.source)
        matchD = re.search(pattern,self.destination)

        return (f"{matchS[0]} => {matchD[0]}")

    def calculateLength(self,locationMap):
        pattern = "[0-9]{5}"
        matchS = re.search(pattern,self.source)
        #print(matchS[0])
        matchD = re.search(pattern,self.destination)
        zip1 = locationMap[matchS[0]]
        zip2 = locationMap[matchD[0]]
        distance = calculateDistance(zip1,zip2)
        return round(distance,2)

    def __add__(self, other):
        #print(self.source,other.legs[-1].destination)
        if not isinstance(other,Trip):
            raise TypeError("invalid input")
        if other.legs[-1].destination != self.source:
            raise  ValueError("not correct")
        x = other.person

        y = other.legs
        y.append(other)
        m = Trip(x, y)
        return m

class Trip():
    def __init__(self,person,legs):
        self.person = person
        self.legs = legs
    def calculateLength(self,locationMap):
        price = 0
        for element in self.legs:
            price += element.calculateLength(locationMap)

        return price
    def getLegsByZip(self,zip,Direction):
        sourceList = []
        destinationList = []
        output = []
        for element in self.legs:
            pattern = "[0-9]{5}"
            matchS = re.search(pattern, element.source)
            matchD = re.search(pattern, element.destination)
            sourceList.append(matchS[0])
            destinationList.append(matchD[0])
        #print(sourceList,destinationList)
        for element in self.legs:
            pattern = "[0-9]{5}"
            matchS = re.search(pattern, element.source)
            matchD = re.search(pattern, element.destination)
            if Direction == Direction.Incoming:
                #print(matchD[0],zip)
                if matchD[0] == zip:
                    output.append(element)
            if Direction == Direction.Outgoing:
                if matchS[0] == zip:
                    output.append(element)
            if Direction == Direction.Both:
                if matchS[0] == zip or matchD[0] == zip:
                    output.append(element)
        #print(output)
        return  output

    def getLegsByState(self,zip,Direction):
        sourceList = []
        destinationList = []
        output = []
        for element in self.legs:
            pattern = "(?P<state>[A-Z]{2})[ \t][0-9]{5}"
            matchS = re.search(pattern, element.source)
            matchD = re.search(pattern, element.destination)
            sourceList.append(matchS['state'])
            destinationList.append(matchD['state'])
        # print(sourceList,destinationList)
        for element in self.legs:
            pattern = "(?P<state>[A-Z]{2})[ \t][0-9]{5}"
            matchS = re.search(pattern, element.source)
            matchD = re.search(pattern, element.destination)
            if Direction == Direction.Incoming:
                # print(matchD[0],zip)
                if matchD['state'] == zip:
                    output.append(element)
            if Direction == Direction.Outgoing:
                if matchS['state'] == zip:
                    output.append(element)
            if Direction == Direction.Both:
                if matchS['state'] == zip or matchD[0] == zip:
                    output.append(element)
        #print(output)
        return output
    def __add__(self, other):
        if not isinstance(other,Leg) and not isinstance(other,Trip):
            raise TypeError("invalid input")
        if isinstance(other,Leg):
            if self.legs[-1].destination != other.source:
                raise  ValueError("not correct")
            x = self.person

            y = self.legs
            y.append(other)
            m = Trip(x,y)
            return m
        else:
            if self.person != other.person:
                raise  ValueError("not correct")
            #z = self.legs
            z= []
            for x in self.legs:
                if x not in z:
                    z.append(x)
            for y in other.legs:
                if y not in z:
                    z.append(y)
            m = self.person
            answer = Trip(m,z)
            return answer

class RoundingTrip(Trip):
     def __init__(self,Trip=None):
         if list == None:
             super().__init__([])
         else:
             if len(Trip.legs) < 2:
                raise ValueError("Input is not a Datum type")
             super(Trip, self).__init__(Trip)
     def getShortestTrip(source,destination,stops):
         filename = os.path.join(DataPath, 'locations.dat')
         with open(filename) as f:
             lines = f.read()
             print(lines)
             match = re.search()


def getClosestIn(sourceState,destinationState):
    filename = os.path.join(DataPath, 'locations.dat')
    with open(filename) as f:
        lines = f.read()
    pattern = "[\"]{sourceState}[\"][,][ \t][\"][ \t](?P<longitude>[0-9]+[.][0-9]+)[\"][,][ \t][\"](?P<Latitude>[-][0-9]+[.][0-9]+)[\"][,]"
    answer = re.findall(pattern,lines)
    #print(answer)

if __name__ == "__main__":
    locationMap = {}
    locationMap["28655"] = (35.742752,-81.71625)
    locationMap["01450"] = (42.609887,-71.55722)
    l1= Leg("Morganton, NC 28655", "Groton, MA 01450")
    l2= Leg("Morganton, NC 28655", "Groton, MA 01450")
    l3= Leg("Groton, MA 01450","Morganton, NC 28655")

    #print(l1.calculateLength(locationMap))
    t=Trip('123',[l1,l2])
    #print(t.calculateLength(locationMap))
    x=(t.getLegsByState("NC",Direction.Both))
    y= t + l3
    #print(len(t.legs))
    #z= l3 + t
    a = ["3","2"]
    b = ["212","2"]
    getClosestIn('ourceState', 'destinationState')
    print(RoundingTrip.getShortestTrip(1,2,3))
    #print(y.legs,z.legs)
