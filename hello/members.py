class Member():
    def __init__(self):
        self._weight = 0.0
        self._height = 0.0
        self._name = ''

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        self._weight = weight
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height =height
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name