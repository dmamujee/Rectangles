#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Name:Rectangles.py
#Purpose: A program that will determine intersection of rectangles
#
#Author: Mamujee. D
#
#Created: 08/11/2013
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Rectangle():
    #method that accepts the parameters x,y,width, and height, then encapsulates them
    def __init__ (self,x = 0,y = 0,width = 1,height = 1):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    #print method that formats the output
    def __str__ (self):
        return "base: (" + str(self.get_X()) + "," + str(self.get_Y()) + ") w:" + str(self.get_Width()) + " h:" + str(self.get_Height())
    
    #Calculates area of rectangle
    def area(self):        
        return self.get_Width()*self.get_Height()
    
    #Calculates perimeter of rectangle
    def perimeter(self):
        return (self.get_Width() + self.get_Height())*2
    
    #Calculates the rectangle of intersection
    def intersection(self,rec):        
        x = 0
        y = 0
        width = 0
        height = 0
        #Determines difference between x and y-axises of two rectangles
        X_Difference = rec.get_X() - self.get_X()
        Y_Difference = rec.get_Y() - self.get_Y()
        
        #Checks if rec is completely inside self
        if rec.get_Y() <= self.get_Y() and rec.get_X() <= self.get_X() and rec.get_Y() + rec.get_Height() <= self.get_Y() + self.get_Height() and rec.get_X() + rec.get_Width() <= self.get_X() + self.get_Width():
            return "base: (0,0) w:0 h:0"

        #Check is self is completely inside rec
        elif rec.get_Y() >= self.get_Y() and rec.get_X() >= self.get_X() and rec.get_Y() + rec.get_Height() >= self.get_Y() + self.get_Height() and rec.get_X() + rec.get_Width() >= self.get_X() + self.get_Width():
            return "base: (0,0) w:0 h:0"
        
        #If the difference in x-axis is greater than 0, therefore rec is to the right of self
        if X_Difference >= 0:
            #Checks if diference in x-axis is greater than width of rectangle. Is so, they do not intersect
            if X_Difference > self.get_Width():
                return "base: (0,0) w:0 h:0"
            #Because rec is to the right of self, the value of x in the intersecting rectangle will be the value of x in rec
            else:
                x = rec.get_X()
                #if rec width is less than self with munis x difference, intersecting rectangle width is same as rec width
                if rec.get_Width() < self.get_Width() - X_Difference:
                    width = rec.get_Width()
                #If not, then width is self width minus x difference
                else:
                    width = self.get_Width() - X_Difference
                    
        #If x_Difference is les than zero, than rec must be to the left of self
        elif X_Difference < 0:
            #If rec X plus rec's width is further left than self, they do not intersect
            if rec.get_X() + rec.get_Width() < self.get_X():
                return "base: (0,0) w:0 h:0"
            #Calculates x and width
            else:
                x = self.get_X()
                if rec.get_Width() + X_Difference > self.get_Width():
                    width = self.get_Width()
                else:
                    width = rec.get_Width() + X_Difference
                    
        #Uses the same calculation method for Y as X
        if Y_Difference >= 0:
            if Y_Difference > self.get_Height():
                return "base: (0,0) w:0 h:0"
            else:
                y = rec.get_Y()
                if rec.get_Height() < self.get_Height() - Y_Difference:
                    height = rec.get_Height()
                else:
                    height = self.get_Height() - Y_Difference
                    
        elif Y_Difference < 0:
            if rec.get_Y() + rec.get_Height() < self.get_Y():
                return "base: (0,0) w:0 h:0"
            else:
                y = self.get_Y()
                if rec.get_Height() + Y_Difference > self.get_Height():
                    height = self.get_Height()
                else:
                    height = rec.get_Height() + Y_Difference                
                
        #Returns intersecting rectangle    
        return  "base: (" + str(x) + "," + str(y) + ") w:" + str(width) + " h:" + str(height)   
        
    #Method that will find the outside perimeter of two intersecting rectangles        
    def total_Perimeter(self,rec):
        #If rectangles are completly inside each other, then the total perimeter is the oerimeter of the bigger rectangle
        
        #Checks if rec is completely inside self
        if rec.get_Y() <= self.get_Y() and rec.get_X() <= self.get_X() and rec.get_Y() + rec.get_Height() <= self.get_Y() + self.get_Height() and rec.get_X() + rec.get_Width() <= self.get_X() + self.get_Width():
            return str(self.perimeter())

        #Checks is self is completely inside rec
        elif rec.get_Y() >= self.get_Y() and rec.get_X() >= self.get_X() and rec.get_Y() + rec.get_Height() >= self.get_Y() + self.get_Height() and rec.get_X() + rec.get_Width() >= self.get_X() + self.get_Width():
            return str(rec.perimeter())

        #If the two rectangles are not within each other, than the total will be the total perimeter of the two seperate rectangles minus the perimeter of the intersecting rectangle
        else:
            #Finds total perimter of two rectangles
            total_Perimeter = self.perimeter() + rec.perimeter()
            intersection_Rec = self.intersection(rec)
            #Finds width of intersected rectangle based on output from intersection method
            width_Index = int(intersection_Rec.find("w")) + 2
            #for loop that finds how many digits long the width is. Can handle up to number 1 million digits long
            for x in range(3,1000003):
                if (intersection_Rec[width_Index:-x]).isdigit() == True:
                    width = int(intersection_Rec[width_Index:-x])
                    break
            #Finds Height from intersection output
            height_Index = int(intersection_Rec.find("h")) + 2       
            height = int(intersection_Rec[height_Index:len(intersection_Rec)])
            #Finds perimter of intersection rectangle
            intersection_Perimeter = (width + height)*2            
            return total_Perimeter - intersection_Perimeter            
        
    #Returns encapsulted field x
    def get_X(self):
        return self.__x
    
    #Returns encapsulated field y
    def get_Y(self):
        return self.__y
    
    #Returns encapsulated field of width
    def get_Width(self):
        return self.__width
    
    #Returns encapsulated field of height
    def get_Height(self):
        return self.__height


#Testing Log

#Corner of b is intersecting with a
a = Rectangle(2,-2,4,7)
b = Rectangle(3,-4,4,3)
print(a)
print(b)
print(a.area())
print(a.perimeter())
print(a.intersection(b))
print(a.total_Perimeter(b))

#Same as above but on opposite side
b1 = Rectangle(1,-4,4,3)
print(a.intersection(b1))
print(a.total_Perimeter(b1))

#d is completly inside of c
c = Rectangle(2,-2,5,7)
d = Rectangle(3,0,2,3)
print(c.intersection(d))
print(c.total_Perimeter(d))

#e and f have a common x-axis line
e = Rectangle(2,-2,3,7)
f = Rectangle(3,-4,4,2)
print(e.intersection(f))
print(e.total_Perimeter(f))

#g and h have a common y-axis line
g = Rectangle(2,1,3,4)
h = Rectangle(5,3,2,4)
print(g.intersection(h))
print(g.total_Perimeter(h))

#i extends on both side of g
i = Rectangle(-1,2,7,2)
print(g.intersection(i))
print(g.total_Perimeter(i))

#i and j are the same
j = Rectangle (-1,2,7,2)
print(i.intersection(j))
print(i.total_Perimeter(j))

#k and l have no intersection
k = Rectangle(-3,1,4,4)
l = Rectangle(3,-2,2,5)
print(k.intersection(l))
print(k.total_Perimeter(l))

#k and m intersect to the top of k
m = Rectangle(-1,3,4,6)
print(k.intersection(m))
print(k.total_Perimeter(m))

#3 side of m are inside k
n = Rectangle(-2,-2,2,6)
print(k.intersection(n))
print(k.total_Perimeter(n))

#Shows that program can handle two digits
o = Rectangle(20,-20,40,70)
p = Rectangle(30,-40,40,30)
print(o.intersection(p))
print(o.total_Perimeter(p))

#Shows that program can handle large numbers
q = Rectangle(20000000000000000000000000000000,-20000000000000000000000000000000,40000000000000000000000000000000,70000000000000000000000000000000)
r = Rectangle(30000000000000000000000000000000,-40000000000000000000000000000000,40000000000000000000000000000000,0000000000000000000000000000000)
print(q.intersection(r))
print(q.total_Perimeter(r))
