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

def translate():
	global X 
	global Y 
	global A
	global B
	X += (cuttingRad * math.sin(B))
	Y += (cuttingRad * math.cos(B))
	A -= B
	B = 0
	 

while Y <= cuttingRad:
	print("G0X{:.4f}Y{:.4f}Z{:.4f}A{:.4f}".format(X, Y, ZStart, A))
	print("G1X{:.4f}Y{:.4f}Z{:.4f}A{:.4f}".format(X, Y, ZEnd, A))
	print("G0X{:.4f}Y{:.4f}Z{:.4f}A{:.4f}".format(X, Y - depthOfCut, ZEnd, A))
	print("G0X{:.4f}Y{:.4f}Z{:.4f}A{:.4f}".format(X, Y - depthOfCut, ZStart, A))
	Y += depthOfCut

print(depthOfCutAngle)
print(ratio)

print("G0X{:.4f}Y{:.4f}Z{:.4f}A{:.4f}B{:.4f}".format(X, Y, ZStart, A, B))
while A < 360.0:
	print("G0X{:.4f}Y{:.4f}Z{:.4f}A{:.4f}B{:.4f}".format(X, Y, ZStart, A, B))
	A += depthOfCutAngle
	B += depthOfCutAngle * ratio
	translate()

