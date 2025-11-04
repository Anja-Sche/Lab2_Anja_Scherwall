# Lab2 - Geometry OOP
The purpose of this lab is to use object-oriented programming in Python to reuse code and design well-structured programs. Creating classes of different shapes.

## UML
[UML's](https://github.com/Anja-Sche/Lab2_Anja_Scherwall/tree/main/UMLs) for this project.

Started to crate a simple UML to get started and get a foundation. 
When moving on to part two of the excercise I updated the UML and implemented two new classes, Sphere and Cube. 

The last UML is for the implementation of a plot class, Shape2dPlotter. 

## Code

### Classes
There are 6 classes in this project: Center, Circle, Rectangle, Sphere, Cube and Shape2dPlotter.

Class Center is a parent class to Circle, Rectangle and Cube. It is also a grandparent class to Sphere that is a child to Circle. They inherit properties from the Center class.

Class Shape2dPlotter is used to plot different shapes of Rectangle and Circle. You can plot several shapes on the same canvas ant they will all be different colours.

### Dunder Methods
You are able to compare the shapes to see if they are the same shape, if they are equal when it comes to area and perimeter and if one is bigger or smaller.

### Utils
[Utils-file](https://github.com/Anja-Sche/Lab2_Anja_Scherwall/blob/main/utils.py) for this project.

The utils file contains validations that are created to be used in the classes. This makes it possible to use the validations in several places while only coding it once.


## Testing

### Manual testing
The manual testing was used from the beginning when building the first classes. I instanciated a class and test different thing to se if the code worked in the correct way.

### Unit testing
In part two of the excercise we were implementing unit testing. With the implementation I chose to do TDD-Test Driven Development where I started to write the tests before writing the code for class Sphere and Cube.

I later did unit testing on the classes that were already crated to see if any changes had to be made.


