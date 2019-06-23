import argparse
from argparse import ArgumentParser
import csv

parser = ArgumentParser()
parser.add_argument("-if", "--inputfile", dest="filename",
                        help="arquivo csv pra adaptar", metavar="FILE", default = "VFR60_10_3_Gap")
args = parser.parse_args()


listOfElements = []
with open("./in_files/"+args.filename+".csv",'rt') as f:
    reader = csv.reader(f)
    listOfElements = list(reader)
neededList =[]

for i in range(len(listOfElements)):
    row = []
    for j in range(len(listOfElements[0])):
        if(j%2 != 0):
            row.insert(len(row), listOfElements[i][j])
    neededList.insert(len(neededList),row)
with open("./in_files/ready_"+args.filename+".csv",'wt') as f:
    filewriter = csv.writer(f)
    filewriter.writerows(neededList)
    


