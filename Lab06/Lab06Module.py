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

def extractArguments(commandline):
    pattern = "[\\+][a-z][ \t]+[^+\\ \t]+"
    #print(123)
    matches = re.findall(pattern,commandline)
    #print(type(matches),matches)
    i = 0
    output =[]
    while i < len(matches):
        pattern = "[\\+](?P<switch>[a-z])[ \t]+(?P<value>[\S]+)"
        match = re.search(pattern,matches[i])
        output.append(tuple([match["switch"],match["value"]]))
        #print(output)
        i += 1
    #pattern = "[\\+](?P<switch>[\w])[ \t]+(?P<value>[\d])]"
    return sorted(output)

def extractNumerics(sentence):
    pattern = "([-+]?[0-9][\.][0-9]+[eE][-+]?[0-9]+|[-+]?[0-9]+[\.]+[0-9]+|[-+]?[0-9]+)"
    matches = re.findall(pattern,sentence)
    print(matches)
    return matches




if __name__ == "__main__":
    print(extractArguments("asdfasdfasd +v +i 2 +p /asdfasdf sadas"))
    extractNumerics("with the electron's - 1.6022e-19 -110 -32.0 +55 3.1415 2.7 +6.0221E+023,12e")