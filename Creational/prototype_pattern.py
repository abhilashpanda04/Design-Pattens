import copy

class Shape:
    def __init__(self,color):
        self.color=color
        
    def clone(self):
        return copy.deepcopy(self)
        

shape_1=Shape("red")
shape_2=shape_1.clone()
shape_2.color="blue"

print(shape_1.color)
print(shape_2.color)
