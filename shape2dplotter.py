import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
            if isinstance(shape, Circle):
                circ = patches.Circle(shape._center, shape._radius)
                list_of_shapes.append(circ)
                
            elif isinstance(shape, Rectangle):
                rect = patches.Rectangle(shape.left_corner_position(), shape._width, shape._height)
                list_of_shapes.append(rect)

        fig, ax = plt.subplots()
        plt.axis("equal")
        for shape in list_of_shapes:
            ax.add_patch(shape)

        ax.set(xlabel="x", ylabel="y", title="Shapes", xlim=(-8, 10)) 
        
        plt.show()

        #TODO: limits beroende på formerna
        #TODO: olika färger på formerna
    
        
    def __repr__(self):
        return f"Shape2dPlotter{self._shapes}"
    
    def __str__(self):
        return f"These shapes will be shown: {self._shapes}"