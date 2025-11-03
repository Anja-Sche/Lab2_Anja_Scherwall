import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from circle import Circle
from rectangle import Rectangle

class Shape2dPlotter:
    def __init__(self, *shapes):
        self._shapes= tuple(shape for shape in shapes)

    @property
    def shapes(self):
        return self._shapes

    def plot(self):
        list_of_shapes= []
        for shape in self._shapes:            
            # 3 random to produce a combination of red, green and blue
            col = (np.random.random(), np.random.random(), np.random.random())

            if isinstance(shape, Circle):
                circ = patches.Circle(shape._center, shape._radius, color= col)
                list_of_shapes.append(circ)              
                
            elif isinstance(shape, Rectangle):
                rect = patches.Rectangle(shape.left_corner_position(), shape._width, shape._height, color= col)
                list_of_shapes.append(rect)

        fig, ax = plt.subplots()
        plt.axis("equal")
        for shape in list_of_shapes:
            ax.add_patch(shape)
        
        ax.set(xlabel="x", ylabel="y", title="Shapes", xlim=(-8, 10)) 
        ax.grid()

        plt.show()
      
    def __repr__(self):
        return f"Shape2dPlotter{self._shapes}"
    
    def __str__(self):
        return f"These shapes will be shown: {self._shapes}"