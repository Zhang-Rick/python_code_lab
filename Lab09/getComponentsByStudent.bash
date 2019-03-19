#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Lab09
studentName=$1
studentID=$(grep -E "$studentName" $DataPath"/maps/students.dat" | cut -f2 -d '|' | cut -f16 -d ' ')
#echo $studentID
circuitFiles=$(ls $DataPath"/circuits")

for circuitFile in $circuitFiles
do
 student=$(grep -E $studentID $DataPath"/circuits/"$circuitFile)
 #echo [ "$student" == "$studentID" ]
 if [ "$student" == "$studentID" ]
 then
  grep -E "[A-Z]{3}[-][0-9]{3}" $DataPath"/circuits/"$circuitFile
 fi
done | sort -u
#echo $components
