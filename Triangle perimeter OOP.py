import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot( (self.__x - x), (self.__y - y))

    def distance_from_point(self, point):
        return math.hypot( (self.__x - point.__x), (self.__y - point.__y))


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.__vertices = [vertex1, vertex2, vertex3]
        self.__vertex1 = vertex1
        self.__vertex2 = vertex2
        self.__vertex3 = vertex3

    def perimeter(self):
        side_length_lst = []
        
        length0 = self.__vertices[0].distance_from_point(self.__vertices[1])
        if length0 > 0: #if the length is positive or zero
            side_length_lst.append(length0)
        else: #if the length is negative
            side_length_lst.append(length0 * (-1))
        
        length1 = self.__vertices[1].distance_from_point(self.__vertices[2])
        if length1 > 0: #if the length is positive or zero
            side_length_lst.append(length1)
        else: #if the length is negative
            side_length_lst.append(length1 * (-1))
            
        length2 = self.__vertices[1].distance_from_point(self.__vertices[0])
        if length2 > 0: #if the length is positive or zero
            side_length_lst.append(length2)
        else: #if the length is negative
            side_length_lst.append(length2 * (-1))
            
        return sum(side_length_lst)
            


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
