import sys
import math
import Line_Point

'''
purpose
	write to stderr a regular polygon with s sides and first vertex at (x0,y0)
preconditions
	s > 2
	x0 and y0 are of type float
'''

L = sys.argv[1:]
try:
	x0=float(L[0])
	y0=float(L[1])
	s=int(L[2])
	if s<= 2:
		print >> sys.stderr, 'Syntax: generate_polygon.py x0 y0 s'

	central_angle = (2*math.pi)/s
	vertex0 = Line_Point.Point(x0,y0)
	i=0
	while i<s:
		vertex1=Line_Point.Point(vertex0.x,vertex0.y)
		vertex1=vertex1.rotate(central_angle)	 
		line= Line_Point.Line(vertex0,vertex1)
		print 'line',
		print line
		vertex0=vertex1
		i=i+1
	
except ValueError:
	print >> sys.stderr,'Syntax: generate_polygon.py x0 y0 s'


