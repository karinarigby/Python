import sys
import Line_Point

'''
purpose
	for each line L in stdin
		repeat count times
			print L
			rotate L counter clockwise about the origin by angle a
preconditions
	stdin contains a legal lines file
'''

R = sys.argv[1:]
try:
	angle=float(R[0])
	count= int(R[1])
	#i=0
	
	for line in sys.stdin:
		#print line		
		L = line.split()		
		point0=Line_Point.Point(float(L[1]),float(L[2]))
		point1=Line_Point.Point(float(L[3]),float(L[4]))
		#line0=Line_Point.Line(point0,point1)	
		print 'line', point0,point1
		i=1
		while i<count:		
			point0=point0.rotate(angle)
			point1=point1.rotate(angle)
			print 'line',point0,point1
					
			i=i+1
			
 
except ValueError:
	print >> sys.stderr,'Syntax: rotate.py angle count'
