#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <02/13/2019 >
#######################################################
import os      # List of  module  import  statements
import re
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################


class Rectangle():
    def __init__(self,lowerLeft,upperRight):
        self.lowerLeft = lowerLeft
        self.upperRight = upperRight
        xll = lowerLeft[0]
        yll = lowerLeft[1]
        xur = upperRight[0]
        yur = upperRight[1]
        if xll >= xur or yll >= yur:
            raise ValueError("lowerLeft of x or y is bigger or equal to the upperRight of x or y")

    def isSquare(self):
        if self.upperRight[0] - self.lowerLeft[0] == self.upperRight[1] - self.lowerLeft[1]:
            return True
        return False

    def intersectsWith(self,rect):
        if rect.lowerLeft[0] < self.upperRight[0] and rect.lowerLeft[0] > self.lowerLeft[0]:
            return True
        if rect.upperRight[0] < self.upperRight[0] and rect.upperRight[0] > self.lowerLeft[0]:
            return True
        if rect.upperRight[1] < self.upperRight[1] and rect.upperRight[1] > self.lowerLeft[1]:
            return True
        if rect.lowerLeft[1] < self.upperRight[1] and rect.lowerLeft[1] > self.lowerLeft[1]:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other,Rectangle):
            raise TypeError("The input is not a valid Rectangle class")

        if other.lowerLeft[0] == self.lowerLeft[0] and  other.upperRight[0] == self.upperRight[0] and other.upperRight[1] == self.upperRight[1] and other.lowerLeft[1] == self.lowerLeft[1]:
            return True
        return False

class Circle():
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
        if radius <= 0.0:
            raise ValueError("Radius should be bigger than 0")
    def intersectsWith(self,other):
        if isinstance(other,Circle):
            circle = other
            a = (circle[0]-self.center[0])**2
            b = (circle[1]-self.center[1])**2
            c = ( a + b)**(1.0/2)
            if c < self.radius:
                return True
            return False
        if isinstance(other,Rectangle):
            rect = other
            dis1 = (self.center[0] - rect.lowerLeft[0])**2
            dis2 = (self.center[1] - rect.lowerLeft[1])**2
            total = (dis1 + dis2)**(1.0/2)
            if total < self.radius:
                return True
            rect = other
            dis1 = (self.center[0] - rect.upperRight[0])**2
            dis2 = (self.center[1] - rect.upperRight[1])**2
            total = (dis1 + dis2)**(1.0/2)
            if total < self.radius:
                return True
            rect = other
            dis1 = (self.center[0] - rect.lowerLeft[0]) ** 2
            dis2 = (self.center[1] - rect.upperRight[1]) ** 2
            total = (dis1 + dis2) ** (1.0 / 2)
            if total < self.radius:
                return True
            rect = other
            dis1 = (self.center[0] - rect.upperRight[0]) ** 2
            dis2 = (self.center[1] - rect.lowerLeft[1]) ** 2
            total = (dis1 + dis2) ** (1.0 / 2)
            if total < self.radius:
                return True
            if self.center[0] > rect.lowerLeft[0] - self.radius:
                return True
            if self.center[0] < rect.upperRight[0] + self.radius:
                return True
            if self.center[1] < rect.upperRight[1] + self.radius:
                return True
            if self.center[1] > rect.lowerLeft[1] - self.radius:
                return True
            return False

