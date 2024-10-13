from abc import ABC , abstractmethod

class Shape:
    @abstractmethod
    def draw():
        pass
    
class Circle(Shape):
    def draw(self):
        return "this is a circle"

class Square(Shape):
    def draw(self):
        return "this is a square"
    

class ShapeFunction:
    @staticmethod
    def get_shape(shape):
        if shape=="circle":
            return Circle()
            
        if shape=="square":
            return Sqaure()
        else:
            raise ValueError("shape not found")


if __name__=="__main__":
    shape=ShapeFunction.get_shape("circle")
    print(shape.draw())
