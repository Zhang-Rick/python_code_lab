#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Lab09
b=200
circuitIDs=$(ls $DataPath"/circuits/")
for circuitID in $circuitIDs
do

 a=$(cat -eT $DataPath"/circuits/"$circuitID)
 if ['$a' -ge '$b']
 then
     echo circuitID | sort -u

 fi
done

