from pyGrounder.myClasses.SimplePredicate import SimplePredicate
from pyGrounder.myClasses.ConstantPredicate import ConstantPredicate
from pyGrounder.myClasses.myUtilities import process_string2

def process_string(string):
            string = string.replace("?", " ?")
            string = string.replace("("," (")
            string = string.replace("*", "* ")
            return string

class ComposedPredicate():
    '''
    This class represents a Composed Predicate in this form: operation <argument1> <argument2>. For Example: >= (distanceRun ?r ?a ?b) (distance ?a ?b)
    
    Parameters
    ----------
    node : antlr4 tree
        The node containing the string of the predicate. For example: ">= (distanceRun ?r ?a ?b) (distance ?a ?b)"
    
    OR
    
    name : str
        The name of the operation of the predicate. For example: >=
    arguments:List[SimplePredicate|ConstantPredicate|ComposedPredicate]
        The list containing the predicate of each argument. For example [(distanceRun ?r ?a ?b),(distance ?a ?b)
    
    Attributes
    ----------
    string:str
        The string of the whole predicate into brackets.  For example: "(>= (distanceRun ?r ?a ?b) (distance ?a ?b))"
    name : str
        The name of the operation. For example: >=
    arguments:List[SimplePredicate|ConstantPredicate|ComposedPredicate]
        The list containing the predicate of each argument. For example [(distanceRun ?r ?a ?b),(distance ?a ?b)
    isComplex:True
        Metadata for some operations, it means it's a composed predicate
    isNegated:False
        Metadata for some operations, it means it's not a negated predicate
    '''
    __string = ""
    __name = ""
    __arguments = []
    __isComplex = True
    __isNegated = False

    def __init__(self,node = None,string = None, name = None, arguments = None):
        
        def getOperands(node):
            if node.getChildCount() == 0:
                return ConstantPredicate(node)
            elif "(" not in node.getText():
                return SimplePredicate(process_string2(node.getText()))
            else: return ComposedPredicate(node,(process_string2(node.getText())) )

        if node != None:
            self.__arguments = []
            self.__string = "("+string+")"
            self.__name = node.getChild(1).getText()
            for child in range (2, node.getChildCount()-1):
                if node.getChild(child).getText() != "(" and node.getChild(child).getText() != ")":
                    self.__arguments.append(getOperands(node.getChild(child)))
        else:
            self.__name = name
            self.__arguments = arguments
            string = name
            for argument in self.__arguments:
                string = string + argument.toString()
            self.__string = "("+string+")"

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

    def printStringPredicate(self):
        print(self.__string)
