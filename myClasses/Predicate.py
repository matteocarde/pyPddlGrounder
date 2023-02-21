from libs.pyGrounder.myClasses.Literal import Literal

class Predicate(Literal):
    __name = ""
    __arguments = []

    def __init__(self, node):
        super().__init__(node)      
        pass

