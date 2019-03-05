#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/22/2019 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
class TimeSpan():
    def __init__(self,weeks,days,hours):
        self.weeks = weeks
        self.days = days
        self.hours = hours
        if weeks < 0 or days < 0 or hours < 0:
            raise ValueError("These inputs cannot be less than zero!")
        if hours >= 24:
            self.hours = hours % 24
            self.days += int((hours-self.hours) / 24)
        if self.days >= 7:
            days = self.days
            self.days = days % 7
            self.weeks += int((days-self.days)/7)

    def __str__(self):
        if self.weeks < 10:
            weeks = '0'+str(self.weeks)
        else:
            weeks = self.weeks
        days = self.days
        if self.hours < 10:
            hours = '0' + str(self.hours)
        else:
            hours = self.hours
        return f"{weeks}W {days}D {hours}H"

    def getTotalHours(self):
        total = self.weeks *(7*24) + self.days * 24 + self.hours
        return total
    def __add__(self, other):
        if not isinstance(other,TimeSpan):
            raise TypeError("The input is not TimeSpan class!")
        a = TimeSpan(self.weeks+other.weeks,self.days+other.days,self.hours+other.hours)
        return a
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if type(other) != type(1) and type(other) != type(1.0):
            raise TypeError("The input is not an integer or float!")

        if type(other) == type(1):
            if other <= 0:
                raise ValueError("The input is less and equal to zero!")
            #a = TimeSpan(self.weeks*other, self.days*other, self.days*other)#123
            result = other * self.getTotalHours()

            hours = result % 24
            days = int(((result - hours) / 24)) % 7
            weeks = int(((result - hours) / 24 - days) / 7)
            a = TimeSpan(weeks, days, hours)
            return a
        if type(other) == type(1.0):
            if other <= 0.0:
                raise ValueError("The input is less and equal to zero!")
            result = int(other * self.getTotalHours())

            hours = result % 24
            days = int(((result - hours) / 24)) % 7
            weeks = int(((result - hours) / 24 - days) / 7)
            a = TimeSpan(weeks,days,hours)
            return a
    def __rmul__(self, other):
        return self.__mul__(other)


    def __lt__(self, other):
        total1 = self.getTotalHours()
        total2 = other.getTotalHours()
        if total1 < total2:
            return True
        return False

    def __le__(self, other):
        total1 = self.getTotalHours()
        total2 = other.getTotalHours()
        if total1 <= total2:
            return True
        return False

    def __eq__(self, other):
        total1 = self.getTotalHours()
        total2 = other.getTotalHours()
        if total1 == total2:
            return True
        return False

    def __ne__(self, other):
        total1 = self.getTotalHours()
        total2 = other.getTotalHours()
        if total1 != total2:
            return True
        return False

    def __gt__(self, other):
        total1 = self.getTotalHours()
        total2 = other.getTotalHours()
        if total1 > total2:
            return True
        return False

    def __ge__(self, other):
        total1 = self.getTotalHours()
        total2 = other.getTotalHours()
        if total1 >= total2:
            return True
        return False





