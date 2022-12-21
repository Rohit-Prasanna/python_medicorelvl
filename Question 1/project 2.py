import re
import csv
f = open("onelinefile.txt","r")
Flist = []
x = f.read()
numeric_const_pattern = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
rx = re.compile(numeric_const_pattern, re.VERBOSE)
number = rx.findall(x)
temp = re.compile("([a-zA-Z]+)")
string = temp.findall(x)
for i in range(0,17,2):
    listu = []
    listu.append(number[i])
    listu.append(string[i])
    listu.append(number[i+1])
    listu.append(string[i+1])
    Flist.append(listu)
f.close()
print(Flist)
with open("Filename2.csv","w", newline = '') as file:
    for i in Flist:
        print(i)
        writer = csv.writer(file)
        writer.writerow(i)
file.close()

        

    

