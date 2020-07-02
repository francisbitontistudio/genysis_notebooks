import math as m
import numpy as np

def Main():
	pts = []
	for i in range(20):

		pts.append([i,i*3,m.pow(i,2)])

	f = open('points.csv','w')

	for i in range(len(pts)):

		for j in range(len(pts[i])):

			f.write(str(pts[i][j]))

			if j<len(pts[i])-1:

				f.write(',')

		if i<len(pts)-1:

			f.write('\n')

Main()