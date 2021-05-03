class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Now drawing with {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Now using {self.title} pencil for drawing")


class Pen(Stationery):

    def draw(self):
        print(f"Now using {self.title} pen for drawing")


class Marker(Stationery):

    def draw(self):
        print(f"Now using {self.title} marker for drawing")


tool1 = Marker('red')
tool2 = Pen('blue')
tool3 = Pencil('black')
tool1.draw()
tool2.draw()
tool3.draw()