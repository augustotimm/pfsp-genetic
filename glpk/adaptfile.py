import argparse
from argparse import ArgumentParser
import csv

parser = ArgumentParser()
parser.add_argument("-if", "--inputfile", dest="filename",
                        help="arquivo csv pra adaptar", metavar="FILE", default = "ready_VFR60_5_10_Gap")
args = parser.parse_args()


listOfElements = []
with open("/home/augusto/Documents/otimizacao/pfsp-genetic/in_files/"+args.filename+".csv",'rt') as f:
    reader = csv.reader(f)
    listOfElements = list(reader)
neededList =[]
neededList.insert(0, "tasks:  "+str(len(listOfElements)+1)+"  machines:  "+ str(len(listOfElements[0])+1)+"\n" )
for i in range(len(listOfElements)):
    row = []
    for j in range(len(listOfElements[0])):
        row =" "+str(i+1)+" "+str(j+1)+" "+ str(listOfElements[i][j])+"\n"
        neededList.insert(len(neededList),row)

    
file = open("./glpk-"+args.filename,'w+')
file.writelines(neededList)
file.close()

file = open("./SAIDANUMEROS",'w+')
str1 = ""
for i in range(len(listOfElements)):
    str1+=" "+str(i+1)
file.write(str1)
for i in range(len(listOfElements[0])):
    str1+=" "+str(i+1)
file.write(str1)




