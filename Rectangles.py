# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name:Rectangles.py
# Purpose: A program that will determine intersection of rectangles
#
# Author: Mamujee. D
#
# Created: 08/11/2013
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Rectangle:
    # method that accepts the parameters x,y,width, and height, then encapsulates them
    def __init__(self, x=0, y=0, width=1, height=1):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    # print method that formats the output
    def __str__(self):
        return "base: (" + str(self.get_x()) + "," + str(self.get_y()) + ") w:" + str(self.get_width()) + " h:" + str(
            self.get_height())

    # Calculates area of rectangle
    def area(self):
        return self.get_width() * self.get_height()

    # Calculates perimeter of rectangle
    def perimeter(self):
        return (self.get_width() + self.get_height()) * 2

    # Calculates the rectangle of intersection
    def intersection(self, rec):
        x = 0
        y = 0
        width = 0
        height = 0
        # Determines difference between x and y-axises of two rectangles
        x_difference = rec.get_x() - self.get_x()
        y_difference = rec.get_y() - self.get_y()

        # Checks if rec is completely inside self
        if rec.get_y() <= self.get_y() and rec.get_x() <= self.get_x() and rec.get_y() + rec.get_height() <= \
                self.get_y() + self.get_height() and rec.get_x() + rec.get_width() <= self.get_x() + self.get_width():
            return "base: (0,0) w:0 h:0"

        # Check is self is completely inside rec
        elif rec.get_y() >= self.get_y() and rec.get_x() >= self.get_x() and rec.get_y() + rec.get_height() >= \
                self.get_y() + self.get_height() and rec.get_x() + rec.get_width() >= self.get_x() + self.get_width():
            return "base: (0,0) w:0 h:0"

        # If the difference in x-axis is greater than 0, therefore rec is to the right of self
        if x_difference >= 0:
            # Checks if diference in x-axis is greater than width of rectangle. Is so, they do not intersect
            if x_difference > self.get_width():
                return "base: (0,0) w:0 h:0"
            # Because rec is to the right of self, the value of x in the
            # intersecting rectangle will be the value of x in rec
            else:
                x = rec.get_x()
                # if rec width is less than self with munis x difference,
                # intersecting rectangle width is same as rec width
                if rec.get_width() < self.get_width() - x_difference:
                    width = rec.get_width()
                # If not, then width is self width minus x difference
                else:
                    width = self.get_width() - x_difference

        # If x_Difference is les than zero, than rec must be to the left of self
        elif x_difference < 0:
            # If rec X plus rec's width is further left than self, they do not intersect
            if rec.get_x() + rec.get_width() < self.get_x():
                return "base: (0,0) w:0 h:0"
            # Calculates x and width
            else:
                x = self.get_x()
                if rec.get_width() + x_difference > self.get_width():
                    width = self.get_width()
                else:
                    width = rec.get_width() + x_difference

        # Uses the same calculation method for Y as X
        if y_difference >= 0:
            if y_difference > self.get_height():
                return "base: (0,0) w:0 h:0"
            else:
                y = rec.get_y()
                if rec.get_height() < self.get_height() - y_difference:
                    height = rec.get_height()
                else:
                    height = self.get_height() - y_difference

        elif y_difference < 0:
            if rec.get_y() + rec.get_height() < self.get_y():
                return "base: (0,0) w:0 h:0"
            else:
                y = self.get_y()
                if rec.get_height() + y_difference > self.get_height():
                    height = self.get_height()
                else:
                    height = rec.get_height() + y_difference

                    # Returns intersecting rectangle
        return "base: (" + str(x) + "," + str(y) + ") w:" + str(width) + " h:" + str(height)

        # Method that will find the outside perimeter of two intersecting rectangles

    def total_perimeter(self, rec):
        # If rectangles are completely inside each other, then the total
        # perimeter is the perimeter of the bigger rectangle

        # Checks if rec is completely inside self
        if rec.get_y() <= self.get_y() and rec.get_x() <= self.get_x() and rec.get_y() + rec.get_height() <= \
                self.get_y() + self.get_height() and rec.get_x() + rec.get_width() <= self.get_x() + self.get_width():
            return str(self.perimeter())

        # Checks is self is completely inside rec
        elif rec.get_y() >= self.get_y() and rec.get_x() >= self.get_x() and rec.get_y() + rec.get_height() >= \
                self.get_y() + self.get_height() and rec.get_x() + rec.get_width() >= self.get_x() + self.get_width():
            return str(rec.perimeter())

        # If the two rectangles are not within each other, than the total will be the total perimeter of the
        # two separate rectangles minus the perimeter of the intersecting rectangle
        else:
            # Finds total perimter of two rectangles
            total_perimeter = self.perimeter() + rec.perimeter()
            intersection_rec = self.intersection(rec)
            # Finds width of intersected rectangle based on output from intersection method
            width_index = int(intersection_rec.find("w")) + 2
            # for loop that finds how many digits long the width is. Can handle up to number 1 million digits long
            width = 1
            for x in range(3, 1000003):
                if (intersection_rec[width_index:-x]).isdigit():
                    width = int(intersection_rec[width_index:-x])
                    break
            # Finds Height from intersection output
            height_index = int(intersection_rec.find("h")) + 2
            height = int(intersection_rec[height_index:len(intersection_rec)])
            # Finds perimeter of intersection rectangle
            intersection_perimeter = (width + height) * 2
            return total_perimeter - intersection_perimeter

            # Returns encapsulated field x

    def get_x(self):
        return self.__x

    # Returns encapsulated field y
    def get_y(self):
        return self.__y

    # Returns encapsulated field of width
    def get_width(self):
        return self.__width

    # Returns encapsulated field of height
    def get_height(self):
        return self.__height


# Testing Log

# Corner of b is intersecting with a
a = Rectangle(2, -2, 4, 7)
b = Rectangle(3, -4, 4, 3)
print(a)
print(b)
print(a.area())
print(a.perimeter())
print(a.intersection(b))
print(a.total_perimeter(b))

# Same as above but on opposite side
b1 = Rectangle(1, -4, 4, 3)
print(a.intersection(b1))
print(a.total_perimeter(b1))

# d is completely inside of c
c = Rectangle(2, -2, 5, 7)
d = Rectangle(3, 0, 2, 3)
print(c.intersection(d))
print(c.total_perimeter(d))

# e and f have a common x-axis line
e = Rectangle(2, -2, 3, 7)
f = Rectangle(3, -4, 4, 2)
print(e.intersection(f))
print(e.total_perimeter(f))

# g and h have a common y-axis line
g = Rectangle(2, 1, 3, 4)
h = Rectangle(5, 3, 2, 4)
print(g.intersection(h))
print(g.total_perimeter(h))

# i extends on both side of g
i = Rectangle(-1, 2, 7, 2)
print(g.intersection(i))
print(g.total_perimeter(i))

# i and j are the same
j = Rectangle(-1, 2, 7, 2)
print(i.intersection(j))
print(i.total_perimeter(j))

# k and l have no intersection
k = Rectangle(-3, 1, 4, 4)
l = Rectangle(3, -2, 2, 5)
print(k.intersection(l))
print(k.total_perimeter(l))

# k and m intersect to the top of k
m = Rectangle(-1, 3, 4, 6)
print(k.intersection(m))
print(k.total_perimeter(m))

# 3 side of m are inside k
n = Rectangle(-2, -2, 2, 6)
print(k.intersection(n))
print(k.total_perimeter(n))

# Shows that program can handle two digits
o = Rectangle(20, -20, 40, 70)
p = Rectangle(30, -40, 40, 30)
print(o.intersection(p))
print(o.total_perimeter(p))

# Shows that program can handle large numbers
q = Rectangle(20000000000000000000000000000000, -20000000000000000000000000000000, 40000000000000000000000000000000,
              70000000000000000000000000000000)
r = Rectangle(30000000000000000000000000000000, -40000000000000000000000000000000, 40000000000000000000000000000000,
              0000000000000000000000000000000)
print(q.intersection(r))
print(q.total_perimeter(r))
