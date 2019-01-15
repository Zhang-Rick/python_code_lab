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
    array = []
    num = 1
    while num <= 1000000:
        array.append(num)
        if num != 1 and (num - 1) % 3 == 0 and num not in array and ((num - 1) / 3 % 2) == 1:
            num = int((num - 1) / 3)
        else:
            num = num * 2

    array = array[::-1]
   # print(array[0],len(array))
    return array[0]

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

def findProduct():
    l= [[3,9],[4,8]]
    a = [[1,2],[2,1],[4,5]]
    i = 0
    while (i < len(l)):
        l[i]
    print(len(a))
    return
if __name__ == "__main__":
    #findLongest()


    findSmallest()
    findProduct()