import math

# all measurements in inches and degrees

diametricPitch = 20
NCutter = 40
NGear = 54
ZStart = .10
ZEnd = -.70
depthOfCut = .002
cutterOffset = 0.0
backOff = .120

pitchCircleDiaGear = NGear / diametricPitch
pitchCircleRadGear = pitchCircleDiaGear / 2

pitchCircleDiaCutter = NCutter / diametricPitch
pitchCircleRadCutter = pitchCircleDiaCutter / 2

cuttingRad = pitchCircleRadGear - pitchCircleRadCutter - cutterOffset

fullDepth = 2.2 / diametricPitch

ratio = NGear / NCutter

circularPitch = math.pi / diametricPitch
depthOfCutAngle = 360.0 / (math.pi * pitchCircleDiaCutter / depthOfCut) * 3

#print(ratio)
#print(depthOfCutAngle)
#quit()


class Modal(object):
	def __init__(self):
		self.G = None
		self.X = None
		self.Y = None
		self.Z = None
		self.A = None
		self.B = None
		self.F = None

	def stroke(self, X=None, Y=None, depthOfCut=None, ZStart=None, ZEnd=None, A=None, F=None):
		angle = math.atan2(X, Y)
		length = math.sqrt((X*X) + (Y*Y))
		length -= depthOfCut
		Xprime = (length * math.sin(angle))
		Yprime = (length * math.cos(angle))
		self.Gprint(0, X, Y, ZStart, A)
		self.Gprint(1, X, Y, ZEnd, A, F=F)
		self.Gprint(0, Xprime, Yprime, ZEnd, A)
		self.Gprint(0, Xprime, Yprime, ZStart, A)
	
	def Gprint(self, G=None, X=None, Y=None, Z=None, A=None, B=None, F=None):
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

# lead simple lead in 

X = 0
Y = 0
A = 0
B = 0

cnc = Modal()

print('G59.1G90')
print('G0X0Y0A0')
print('M6T20')
print('G43Z.5H20')
print('F100.0')
print('M8')

#while Y <= cuttingRad:
#	cnc.stroke(X, Y, depthOfCut, ZStart, ZEnd, A)
#	Y += depthOfCut

#Y = cuttingRad

cnc.Gprint(0, X, Y, ZStart, A)

endAngle = 360.0 * 1
atDepth = False
currentRad = cuttingRad - fullDepth

while A <= endAngle:
	X = (currentRad * math.sin(math.radians(-B)))
	Y = (currentRad * math.cos(math.radians(-B)))
	print('(B{:.4f})'.format(-B))
	cnc.stroke(X, Y, backOff, ZStart, ZEnd, B-A)
	if not atDepth:
		currentRad += depthOfCut
		if currentRad > cuttingRad:
			currentRad = cuttingRad
			atDepth = True
			endAngle += A
			
	A += (depthOfCutAngle / ratio)
	B += depthOfCutAngle

print('M9')
print('G30')
