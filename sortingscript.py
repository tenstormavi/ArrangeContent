#!/usr/bin/python
import os

file = open("tosort.txt", "rw+")
data = []

line = file.readline()
data.append(line)
while line:
	line = file.readline()
	data.append(line)

data.sort()
if not os.path.exists('sorted.txt'):
    z = open('sorted.txt','w')
    for x in data:
    	z.write(x)
    z.close()

file.close()
