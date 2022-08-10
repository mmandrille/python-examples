""" The Factory (Method) Pattern

Notes:

The Factory Pattern serves to introduce a layer of abstraction in the
object creation process. The factory serves as a common interface to construct
objects of multiple types. This can be particularly useful to manage object creation
in an organized and easily testable manner. Furthermore, the object creation factory
may be able to identify which type of object to construct based on some information
about the required nature of the object. For example, a factory that generates
objects with a base class 'Car' may be instructed to generate a car with `top_speed > n`
and `fuel_type == 'biodiesel'`; this factory might then generate a type (child) of `Car`
that matches these specifications.

There are many ways to implement this design pattern. The example shown below, known as
the 'Factory Method Pattern', is a very straightforward implementation. It is useful when
the factory is resoponsible for returning objects of multiple types that all share a
common parent. In this pattern, the factory is implemented as a static method of the
parent class, and can return objects of child classes based on some information about
the expected object type (passed as arguments to the factory method). If your factory
is expected to return objects with no known common parent class, the factory can easily
be implemented as a standalone function or within an independent `Factory` class.

"""
# Python imports
import abc
import random
# Package Imports
import pygame

# Classes definition
class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def make_object(self):
        return

class ShapeFactory(object):
    def __init__(self, x, y, window_dimensions):
        # Paramete5rs
        self.window_dimensions = window_dimensions
        # Horizontal Position
        self.x = x
        self.min_limit_x = 0
        self.max_limit_x = window_dimensions[0] - self.width
        # Vertical Position
        self.y = y
        self.min_limit_y = 0
        self.max_limit_y = window_dimensions[1] - self.height
        # Some feedback
        print(f"Position: {self.x} x {self.y}")
        print(f"Horizontal Limits: {self.min_limit_x} to {self.max_limit_x}")
        print(f"Vertical Limits: {self.min_limit_y} to {self.max_limit_y}")

    def draw(self):
        raise NotImplementedError()

    def move(self, direction, speed=1, limit=False):
        # Move circle
        steps = 4 * speed
        if direction == 'left':
            self.x -= steps
            if self.x < self.min_limit_x or limit:
                self.x = self.min_limit_x
        elif direction == 'right':
            self.x += steps
            if self.x > self.max_limit_x or limit:
                self.x = self.max_limit_x
        elif direction == 'up':
            self.y -= steps
            if self.y < self.min_limit_y or limit:
                self.y = self.min_limit_y
        elif direction == 'down':
            self.y += steps
            if self.y > self.max_limit_y or limit:
                self.y = self.max_limit_y 

    @staticmethod 
    def build(type, window_dimensions):
        shapeClass = ShapeDict.get(type)
        if shapeClass:
            return shapeClass(100, 100, window_dimensions)
        # In case no match
        assert 0, "Bad shape requested: " + type

    def transform(self):
        random_shapeClass = random.choice([value for key, value in ShapeDict.items() if not key == self.shape])
        return random_shapeClass(self.x, self.y, self.window_dimensions)

class Square(ShapeFactory):
    def __init__(self, x, y , window_dimensions):
        self.shape = "Square"
        self.width = 20
        self.height = 20
        super().__init__(x, y , window_dimensions)

    def draw(self):
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            pygame.Rect(self.x, self.y, self.width, self.height) # Position + Size
        )

class Circle(ShapeFactory):
    def __init__(self, x, y , window_dimensions):
        self.shape = "Circle"
        self.width = 10
        self.height = self.width
        super().__init__(x, y , window_dimensions)

    def draw(self):
        pygame.draw.circle(
            screen,
            (0, 255, 255),
            (self.x, self.y), # Position
            self.width # Size
        )

class Triangle(ShapeFactory):
    def __init__(self, x, y , window_dimensions):
        self.shape = "Triangle"
        self.width = 10
        self.height = self.width
        super().__init__(x, y , window_dimensions)

    def draw(self):
        pygame.draw.polygon(
            surface=screen,
            color = (255, 0, 255),
            points=[(self.x,self.y+25), (self.x,self.y-25), (self.x+25,self.y)]
        )

# Global Definition of Available Shapes
ShapeDict = {
    "Circle": Circle,
    "Square": Square,
    "Triangle": Triangle
}

if __name__ == '__main__':
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)
    obj = ShapeFactory.build("Square", window_dimensions)
    
    player_quits = False
    while not player_quits: # Keep doing till player press Exit
        # Every time something happens:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # player press Exit
                player_quits = True # End the while

            # Check player interaction            
            elif event.type == pygame.KEYDOWN:
                print(event)
                pressed = pygame.key.get_pressed() # We fetch keystroke
                
                # In case of Shift Pressing:
                limit = False
                speed = 1
                if  pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    speed = 5
                
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    limit = True
                
                # Get pressed key
                if pressed[pygame.K_UP]: obj.move('up', speed, limit)
                if pressed[pygame.K_DOWN]: obj.move('down', speed, limit)
                if pressed[pygame.K_LEFT]: obj.move('left', speed, limit)
                if pressed[pygame.K_RIGHT]: obj.move('right', speed, limit)

                # If want to transform:
                if pressed[pygame.K_c]: # After pressing C
                    obj = obj.transform()        
        
            screen.fill((0, 0, 0))
            obj.draw() # Draw my object
        pygame.display.flip()