class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, width, height):
        self.starting_point = origin
        self.new_x_coord = width
        self.new_y_coord = height

    def get_area(self):
        return self.width * self.height

    def end_points(self):
        top_right = self.origin.x + self.width
        bottom_left = self.origin.y + self.height
        print('Starting Point (X)): ' + str(self.starting_point.coordX))
        print('Starting Point (Y)): ' + str(self.starting_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


my_rectangle = build_rectangle()

print(my_rectangle.get_area())
my_rectangle.end_points()
