# #!/usr/bin/env python3

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x:.1f}, {self.y:.1f})'

    def midpoint(self, other):
        tmp_x = (self.x + other.x) / 2
        tmp_y = (self.y + other.y) / 2
        return Point(tmp_x, tmp_y)

class Circle():
    def __init__(self, centre=None, radius=1):
        self.centre = Point(0, 0) if centre is None else centre
        self.radius = radius

    def __str__(self):
        s = []
        s.append(f'Centre: {self.centre}')
        s.append(f'Radius: {self.radius}')
        return '\n'.join(s)
