from UniversalClasses import *

class AbstractShape(object()):
    """docstring for AbstractShape."""
    def __init__(self):
        super(AbstractShape, self).__init__()
        #
# Base Shape Class
class Shape(Assembly, AbstractShape):
    """docstring for Shape."""
    def __init__(self):
        AbstractShape.__init__(self)
        Assembly.__init__(self)
