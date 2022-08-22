

class Rectangle:
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._height * self._width

    def __str__(self) -> str:
        return f"Width: {self.width} Height: {self.height}"

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

        
