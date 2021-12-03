class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y =20
print(point1.y)
point1.draw()

#we use classes to define new types in python