class ToolBox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def remove_tool(self, tool):
        index = self.tools.index(tool)
        del self.tools[index]


class Screwdriver:
    def __init__(self, size=3):
        self.size = size

    def tighten(self, screw):
        screw.tighten()

    def loosen(self, screw):
        screw.loosen()

    def __repr__(self):
        return f"Tournevis de taille {self.size}"


class Hammer:
    def __init__(self, color="red"):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self, nail):
        nail.nail_in()

    def remove(self, nail):
        nail.remove()

    def __repr__(self):
        return f"Marteau de couleur {self.color}"


class Screw:
    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."


toolbox = ToolBox()
screwdriver = Screwdriver()
hammer = Hammer()

toolbox.add_tool(screwdriver)
toolbox.add_tool(hammer)

screw = Screw()
print(screw)
screwdriver.tighten(screw)
print(screw)
screwdriver.loosen(screw)
print(screw)

nail = Nail()
print(nail)
hammer.hammer_in(nail)
print(nail)
hammer.remove(nail)
print(nail)
