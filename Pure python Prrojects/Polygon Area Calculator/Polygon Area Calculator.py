class Rectangle:
    def __init__ (self,width,height):
        def numberfromstring(string_a):
            n=list(str(string_a))
            for i in n:
                if i.isdigit():
                    k=int(i)
                    return(k)

        if str(width).isnumeric() ==True and str(height).isnumeric() == True :
            self.width = width
            self.height = height
        else :
            self.width = numberfromstring(width)
            self.height = numberfromstring(height) 
    
    def get_area (self):
        self.area = self.width*self.height
        return self.area

    def get_perimeter (self):
        return (2*self.width + 2* self.height)

    def get_diagonal (self):
        return((self.width ** 2 +self.height **2) ** .5)

    def get_picture (self):
        if self.height > 50 or self.width > 50 :
            return("Too big for picture.")
        else :
            while self.height > 0 :
                return(self.width*"*" )
                self.height -= 1

    def get_amount_inside (self,shape):
        x = shape.get_area()
        y = self.area
        z = ((y/x)-((y/x)%1))
        return ("This shape can fit in "+str(z)+" times.")
    
class Square(Rectangle):
    def __init__ (self,side) :
        self.width = side
        self.height = side

p1 = Rectangle(2,3)
print(p1.get_area())