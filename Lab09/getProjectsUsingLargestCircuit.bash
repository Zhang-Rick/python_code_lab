#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Lab09

projectID=$(grep -E "[0-9A-Z]{8}[-][0-9A-Z]{4}[-][0-9A-Z]{4}[-][0-9A-Z]{4}[-][0-9A-Z]{12}" $DataPath"/maps/projects.dat" | cut -f15 -d ' ' | sort -u)
#echo $projectID
for projectIDLine in $projectID
do
    circuitIDs=$(grep -E $projectIDLine $DataPath"/maps/projects.dat" | cut -f5 -d ' ')
    #echo $circuitID
    for circuitID in $circuitIDs
    do
    	a+=$(cat -eT $DataPath"/circuits/circuit_"$circuitID".dat")
    done
  
    b=$(echo $a | wc -c)
    echo $b
done
