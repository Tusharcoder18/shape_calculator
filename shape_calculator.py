class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def set_width(self, width: int):
        self.width = width
    
    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        result = ''
        for _ in range(self.height):
            for _ in range(self.width):
                result += '*'
            result += '\n'
        return result
    
    def get_amount_inside(self, shape: object):
        if shape.get_area() > self.get_area():
            return 0
        
        shape_width = shape.width
        shape_height = shape.height

        result = (self.width // shape_width) * (self.height // shape_height)

        return result


    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'




class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def set_height(self, side: int):
        self.width = side
        self.height = side

    def width(self, side: int):
        self.width = side
        self.height = side
    
    def set_side(self, side: int):
        self.set_height(side)
    
    def __str__(self):
        return f'Square(side={self.width})'
    

