class Road:
    _width: float  # meters
    _length: float  # meters
    _thickness: float  # centimeters
    _density = 25  # kg/sq m with 1 cm thick

    def __init__(self, width, length, thickness):
        self._width = width
        self._length = length
        self._thickness = thickness

    def Calculate(self):
        amount = self._width * self._length * self._thickness * self._density / 1000
        print(f"You will need {amount} tons of asphalt to build this road")


highway = Road(width=20, length=5000, thickness=5)
highway.Calculate()
