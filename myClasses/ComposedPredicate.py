from libs.pyGrounder.myClasses.SimplePredicate import SimplePredicate
from libs.pyGrounder.myClasses.ConstantPredicate import ConstantPredicate
from libs.pyGrounder.myClasses.myUtilities import process_string2
from pyspel.pyspel import Predicate


def process_string(string):
    string = string.replace("?", " ?")
    string = string.replace("(", " (")
    string = string.replace("*", "* ")
    return string


class ComposedPredicate:
    __string = ""
    __name = ""
    __arguments = []
    __isComplex = True
    __isNegated = False

    def __init__(self, node=None, string=None, name=None, arguments=None):

        def getOperands(node):
            if node.getChildCount() == 0 or node.getText() == "#t":
                return ConstantPredicate(node)
            elif "(" not in node.getText():
                return SimplePredicate(process_string2(node.getText()))
            else:
                return ComposedPredicate(node, (process_string2(node.getText())))

        if node is not None:
            self.__arguments = []
            self.__string = "(" + string + ")"
            self.__name = node.getChild(1).getText()
            for child in range(2, node.getChildCount() - 1):
                if node.getChild(child).getText() != "(" and node.getChild(child).getText() != ")":
                    self.__arguments.append(getOperands(node.getChild(child)))
        else:
            self.__name = name
            self.__arguments = arguments
            string = name
            for argument in self.__arguments:
                string = string + argument.toString()
            self.__string = "(" + string + ")"

    def __str__(self):
        return self.__string

    def __repr__(self):
        return str(self)

    @property
    def string(self):
        return self.__string

    @property
    def isComplex(self):
        return self.__isComplex

    @property
    def isNegated(self):
        return self.__isNegated

    @property
    def arguments(self):
        return self.__arguments

    @property
    def name(self):
        return self.__name

    def toString(self):
        return self.__string

    def ground(self, combination):
        groundedArguments = [arg.ground(combination) for arg in self.arguments]
        return ComposedPredicate(name=self.name, arguments=groundedArguments)

    def printStringPredicate(self):
        print(self.__string)
