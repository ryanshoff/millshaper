import math

# all measurements in inches and degrees

diametricPitch = 20
NCutter = 40
NGear = 60
ZStart = 0
ZEnd = -.50
depthOfCut = .002

pitchCircleDiaGear = NGear / diametricPitch
pitchCircleRadGear = pitchCircleDiaGear / 2

pitchCircleDiaCutter = NCutter / diametricPitch
pitchCircleRadCutter = pitchCircleDiaCutter / 2

cuttingRad = pitchCircleRadGear - pitchCircleRadCutter

fullDepth = 2.2 / diametricPitch

ratio = NGear / NCutter

circularPitch = math.pi / diametricPitch
depthOfCutAngle = 360.0 / (math.pi * pitchCircleDiaGear / depthOfCut)

# lead simple lead in 

X = 0
Y = cuttingRad - fullDepth
A = 0
B = 0


class Modal(object):
	def __init__(self):
		self.G = None
		self.X = None
		self.Y = None
		self.Z = None
		self.A = None
		self.B = None
		self.F = None
	
	def print(self, G=None, X=None, Y=None, Z=None, A=None, B=None, F=None):
		newline = False
		if G != self.G:
			print('G{:d}'.format(G), end='')
			self.G = G
			newline = True
		if X != self.X:
			print('X{:.4f}'.format(X), end='')
			self.X = X
			newline = True
		if Y != self.Y:
			print('Y{:.4f}'.format(Y), end='')
			self.Y = Y
			newline = True
		if Z != self.Z:
			print('Z{:.4f}'.format(Z), end='')
			self.Z = Z
			newline = True
		if A != self.A:
			print('A{:.4f}'.format(A), end='')
			self.A = A
			newline = True
		if B != self.B:
			print('B{:.4f}'.format(B), end='')
			self.B = B
			newline = True
		if F != self.F:
			print('F{:.4f}'.format(F), end='')
			self.F = F
			newline = True
		if newline:
			print()


def translate():
	global X 
	global Y 
	X = (cuttingRad * math.sin(math.radians(B)))
	Y = (cuttingRad * math.cos(math.radians(B)))
	 

cnc = Modal()

while Y <= cuttingRad:
	cnc.print(0, X, Y, ZStart, A)
	cnc.print(1, X, Y, ZEnd, A)
	cnc.print(0, X, Y - depthOfCut, ZEnd, A)
	cnc.print(0, X, Y - depthOfCut, ZStart, A)
	Y += depthOfCut

cnc.print(0, X, Y, ZStart, A)
while A < 360.0:
	cnc.print(0, X, Y, ZStart, A)
	A += depthOfCutAngle
	B += depthOfCutAngle * ratio
	translate()

