import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from circle import Circle
from rectangle import Rectangle

class Shape2dPlotter:
    """
    A class used to plot shapes from Circle and Rectangle class.

    Attributes:
    - *shapes (collecton): Unknown amount of shapes type circle and rectangle.

    Methods:
    - plot(): Plotts all the shapes on one canvas.

    Example usage:
    >>> plot1 = Shape2dPlotter(circle1, rectangle1)
    >>> plot1.plot()
    """

    def __init__(self, *shapes) -> None:
        """
        Initializes an new instance of the class Shape2dPlotter.

        Parameters:
        - *shapes (collection): Unknown amount of shapes type circle and rectangle.
        """
        self._shapes= tuple(shape for shape in shapes)

    @property
    def shapes(self) -> tuple:
        return self._shapes

    def plot(self) ->None:
        """Plotts all the shapes on one canvas."""
        list_of_shapes= []
        for shape in self._shapes:            
            # 3 random to produce a combination of red, green and blue
            col = (np.random.random(), np.random.random(), np.random.random())

            if isinstance(shape, Circle):
                circ = patches.Circle(shape._center, shape._radius, color= col)
                list_of_shapes.append(circ)              
                
            elif isinstance(shape, Rectangle):
                rect = patches.Rectangle(shape._left_corner_position(), shape._width, shape._height, color= col)
                list_of_shapes.append(rect)

        fig, ax = plt.subplots()
        plt.axis("equal")
        for shape in list_of_shapes:
            ax.add_patch(shape)
        
        ax.set(xlabel="x", ylabel="y", title="Shapes", xlim=(-8, 10)) 
        ax.grid()

        plt.show()
      
    def __repr__(self) ->str:
        return f"Shape2dPlotter{self._shapes}"
    
    def __str__(self) ->str:
        return f"These shapes will be shown: {self._shapes}"