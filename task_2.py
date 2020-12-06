class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_masses(self, masses, thickness):
        self.masses = masses
        self.thickness = thickness
        print(f'Масса асфальта: {self._length * self._width * self.masses * self.thickness / 1000} т')


a = Road(5000, 20)
a.asphalt_masses(25, 5)
