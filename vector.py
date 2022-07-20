import math
class vector:
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
    def setax(self, ax):
        self.ax = ax
    def setay(self, ay):
        self.ay = ay
    def setbx(self, bx):
        self.bx = bx
    def setby(self, by):
        self.by = by
    def getax(self):
        return self.ax
    def getay(self):
        return self.ay
    def getbx(self):
        return self.bx
    def getby(self):
        return self.by
    def __str__(self):
        return "A = ("+str(self.ax)+", "+str(self.ay)+")\nB = ("+str(self.bx)+", "+str(self.by)+")"
    def calcVector(self):
        vx = self.bx - self.ax
        vy = self.by - self.ay
        return "The directional vector is <"+str(vx)+", "+str(vy)+">"
    def calcMag(self):
        mag = math.sqrt(((self.bx-self.ax)*(self.bx-self.ax))+((self.by-self.ay)*(self.by-self.ay)))
        mag = round(mag, 2)
        return "The magnitude is "+str(mag)


ax = int(input("X coordinate of point A: "))
ay = int(input("Y coordinate of point A: "))
bx = int(input("X coordinate of point B: "))
by = int(input("Y coordinate of point B: "))
v1 = vector(ax, ay, bx, by)
print(v1)
print(v1.calcVector())
print(v1.calcMag())