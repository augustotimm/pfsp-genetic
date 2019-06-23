import argparse
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-n", "--number", dest="number",
                        help="numero pra escrever", metavar="FILE",type=int, default = 10)
args = parser.parse_args()

file = open("./SAIDANUMEROS",'w+')
str1 = ""
for i in range(args.number):
    str1+=" "+str(i+1)
file.write(str1)
file.close()
