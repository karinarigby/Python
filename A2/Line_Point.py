import math

'''
Purpose
	Provide an exception class for Point and Line.
Exceptions
	None
Preconditions
	Message is a string.
'''
class Error(Exception):
	def __init__(self, message):
		self.message = message

'''
Purpose
	Store a point as an x, y pair.
	Provide functions to rotate, scale and translate the point.
Preconditions
	After instantiation, a Point object is modified only by
	rotate, scale and translate.
'''
class Point:
	'''
	Purpose
		Create a Point instance from x and y.
	Exceptions
		Raise Error if x or y are not of type float.
	Preconditions
		None
	'''
	def __init__(self, x, y):
		if type(x)!=float:
			raise Error('Parameter "x" illegal.')
		if type(y)!=float:
			raise Error('Parameter "y" illegal.')
		
		self.x=x
		self.y=y

		#return self
	'''
	Purpose
		Rotate counterclockwise, by a radians, about the origin.
	Exceptions
		Raise Error if a is not of type float.
	Preconditions
		None
	'''
	def rotate(self, a):
		if type(a)!=float:
			raise Error('Parameter "a" illegal.') 
		x0=(math.cos(a)*self.x)-(math.sin(a)*self.y)
		y0=(math.sin(a)*self.x)+(math.cos(a)*self.y)
		
		self.x=x0
		self.y=y0
		
		return self

	'''
	Purpose
		Scale point by factor f, about the origin.
	Exceptions
		Raise Error if f is not of type float.
	Preconditions
		None
	'''
	def scale(self, f):
		if type(f)!=float:
			raise Error('Parameter "f" illegal.') 
		x0=f*self.x
		y0=f*self.y
		
		self.x=x0
		self.y=y0
		
		return self;

	'''
	Purpose
		Translate point by delta_x and delta_y.
	Exceptions
		Raise Error if delta_x, delta_y are not of type float.
	Preconditions
		None
	'''
	def translate(self, delta_x, delta_y):
		if type(delta_x)!=float:
 			raise Error('Parameter "delta_x" illegal.')
		if type(delta_y)!=float:
			raise Error('Parameter "delta_y" illegal.')
		x0=self.x+delta_x
		y0=self.y+delta_y
		self.x=x0
		self.y=y0

		return self
	'''
	Purpose
		Round and convert to int in string form.
	Exceptions
		None
	Preconditions
		None
	'''
	def __str__(self):
		#round and convert 
		x0=round(self.x)
		y0=round(self.y)
		#cast to int 
		x0=int(x0)
		y0=int(y0)
		#to string 
		x0=str(x0)
		y0=str(y0)
		coord = x0+' '+y0
		return coord  
'''
Purpose
	Store a Line as a pair of Point instances.
	Provide functions to rotate, scale and translate the line.
Preconditions
	After instantiation, a Line object is modified only by
	rotate, scale and translate.
'''
class Line:
	'''
	Purpose
		Create a Line instance from point0 and point1.
	Exceptions
		None
	Preconditions
		None
	'''
	def __init__(self, point0, point1):
		self.point0=Point(point0.x,point0.y)
		self.point1=Point(point1.x,point1.y)

	'''
	Purpose
		Rotate counterclockwise, by a radians, about the origin.
	Exceptions
		Raise Error if a is not of type float.
		Raise Error if self.point0 or self.points1 is not legal.
	Preconditions
		None
	'''
	def rotate(self, a):
		if type(a)!=float:
			raise Error('Parameter "a" illegal.') 
		if type(self.point0.x)!=float:
			raise Error('Parameter "point0.x" illegal.') 
		if type(self.point0.y)!=float:
			raise Error('Parameter "point0.y" illegal.') 
		if type(self.point1.x)!=float:
			raise Error('Parameter "point1.x" illegal.') 
		if type(self.point1.y)!=float:
			raise Error('Parameter "point1.y" illegal.') 
	## what if they equal eachother?? 
		if self.point1.x==self.point0.x and self.point1.y==self.point0.y:
			raise Error('Parameter "NEVER A LINE " illegal')
	
		new_point0=self.point0.rotate(a)
		self.point0 = new_point0
			
		new_point1 =self.point1.rotate(a)
		self.point1 = new_point1
		

	'''
	Purpose
		Scale point by factor f, about the origin.
	Exceptions
		Raise Error if f is not of type float.
	Preconditions
		None
	'''
	def scale(self, factor):
		if type(factor)!=float:
			raise Error('Parameter "factor" illegal.')
		self.point0=self.point0.scale(factor)
		self.point1=self.point1.scale(factor)

	'''
	Purpose
		Translate Line by delta_x and delta_y.
	Exceptions
		Raise Error if delta_x, delta_y are not of type float.
	Preconditions
		None
	'''
	def translate(self, delta_x, delta_y):
		if type(delta_x)!=float:
 			raise Error('Parameter "delta_x" illegal.')
		if type(delta_y)!=float:
			raise Error('Parameter "delta_y" illegal.')
		self.point0=self.point0.translate(delta_x,delta_y)
		self.point1=self.point1.translate(delta_x,delta_y)
		

	'''
	Purpose
		Round and convert to int in string form.
	Exceptions
		None
	Preconditions
		None
	'''
	def __str__(self):
		pointzero=str(self.point0)
		pointone=str(self.point1)
		line=pointzero+' '+pointone
		return line
