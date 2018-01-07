import sys
import Line_Point

'''
purpose
	for each line L in stdin
		repeat count times
			translate L horizontally by delta_x
			translate L vertically by delta_y
			print L
preconditions
	stdin contains a legal lines file
'''

import sys
import Line_Point

'''
purpose
	for each line L in stdin
		repeat count times
			scale L about the origin by factor
			print L
preconditions
	stdin contains a legal lines file
'''

R = sys.argv[1:]
try:
	delta_x=float(R[0])
	delta_y= float(R[1])
	count=float(R[2])
	i=0
	for line in sys.stdin:
		#print line		
		L = line.split()		
		point0=Line_Point.Point(float(L[1]),float(L[2]))
		point1=Line_Point.Point(float(L[3]),float(L[4]))
		i=0
		while i<count:		
			point0=point0.translate(delta_x,delta_y)
			point1=point1.translate(delta_x,delta_y)
			print 'line',point0,point1	
			i=i+1
			
 
except ValueError:
	print >> sys.stderr,'Syntax: translate.py delta_x delta_y count'
