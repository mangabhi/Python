#Description : Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle(object):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        return self.l*self.b
    
Rec=Rectangle(2,5)
print (Rec.area())
        
