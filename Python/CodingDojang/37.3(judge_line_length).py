import math

class Point2D:
    #Initialize x and y to 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

length = 0.0

p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for i in range(3) :
    a = p[i].x - p[i + 1].x
    b = p[i].y - p[i + 1].y
    length += math.sqrt((a * a) + (b * b))

print(length)
#print(round(length, 2))