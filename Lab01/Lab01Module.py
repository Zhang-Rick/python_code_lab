#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642 >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/15/2019 >
#######################################################
import os
import math
import sys

def findLongest():

##try to find StartingInteger backwards
#we need to slow down the number to become bigger
#therfore we try to make it smaller if it can be smaller
#BUT the number in this array cannot exist twice
#in addition it should return an integer and it is an odd!
#first case is exclusive
    array = [1,2,4,8,16,32,64,128,256]
    array3 = []
    num = 1
    while num <= 1000000:

        if num != 1 and (num - 1) % 3 == 0 and num not in array and ((num - 1) / 3 % 2) == 1:
            num = int((num - 1) / 3)
        else:
            num = num * 2
        array3.append(num)
    array3 = array3[::-1]
    return array3[1]

def findSmallest():
   n = 1
   while n >= 1:
       n2 = 2 * n
       n3 = 3 * n
       n4 = 4 * n
       n5 = 5 * n
       n6 = 6 * n
       if sorted(str(n)) == sorted(str(n2)) == sorted(str(n3)) == sorted(str(n4)) == sorted(str(n5)) == sorted(str(n6)):
           break
       n += 1
   #print(n)
   #print(n2)
   #print(n3)
   #print(n4)
   #print(n5)
   #print(n6)
   return n

def sortInt(num):
    array = map(int,str(num))
    array = sorted(array)
    n = ''
    n.join(array)
    return n

def findProduct(M1,M2):
    i = 0
    j = 0
    k = 0
    z = 0
    array = []
    array2 = []
    while (z < len(M1)):
        while (i < len(M2)):
            while (j < len(M1[1])):
                while (k < len(M2[1])):
                    a = M1[z][j]*M2[i][k]
                    array.append(a)
                    k += 1
                j += 1
            array2.append(array)
            i += 1
        z += 1
    print(array2)
    return
if __name__ == "__main__":
    findLongest()

    #M1 = [[1,2],[3,4]]
    #M2 = [[0 ,5],[6,7]]
    #findSmallest()
    #findProduct(M1,M2)