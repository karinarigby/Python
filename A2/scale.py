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
	factor=float(R[0])
	count= int(R[1])
	i=0
	
	for line in sys.stdin:
		#print line		
		L = line.split()		
		point0=Line_Point.Point(float(L[1]),float(L[2]))
		point1=Line_Point.Point(float(L[3]),float(L[4]))
		#line0=Line_Point.Line(point0,point1)	
		#print 'line', point0,point1
		i=0
		while i<count:		
			point0=point0.scale(factor)
			point1=point1.scale(factor)
			print 'line',point0,point1	
			i=i+1
			
 
except ValueError:
	print >> sys.stderr,'Syntax: scale.py factor count'
