from libs.pyGrounder.myClasses.SimplePredicate import SimplePredicate
from libs.pyGrounder.myClasses.NegatedPredicate import NegatedPredicate
from libs.pyGrounder.myClasses.ConstantPredicate import ConstantPredicate
from libs.pyGrounder.myClasses.ComposedPredicate import ComposedPredicate
from libs.pyGrounder.myClasses.myUtilities import process_string


class Precondition:
    __predicate = None

    def __init__(self, node=None, predicate=None):
        if node is None:
            self.__predicate = predicate
            return

        string = node.getText()
        OPERATORS = {">", ">=", "<", "<=", "assign", "increase", "decrease", "*"}
        predicateString = process_string(string)
        predicate = predicateString.split(" ")
        if predicate[0] == "not":
            self.__predicate = NegatedPredicate(node.getChild(3), predicateString)
        elif predicate[0] in OPERATORS:
            self.__predicate = ComposedPredicate(node, predicateString)
        else:
            self.__predicate = SimplePredicate(predicateString)

    def ground(self, combination):
        return Precondition(predicate=self.predicate.ground(combination))

    def __str__(self):
        return str(self.__predicate)

    def __repr__(self):
        return str(self)

    @property
    def predicate(self):
        return self.__predicate

    def predicateAsDict(self):
        '''
        It returns the dict containing the details of the Precondition in order to write its Json representation
        '''

        def makeDictOfPredicates(predicate):
            result = {}
            if not isinstance(predicate, ComposedPredicate) and not isinstance(predicate, ConstantPredicate):
                result["preconditionString"] = predicate.string
                result["isNegated?"] = predicate.isNegated
                result["isOperation?"] = predicate.isComplex
                result["Name"] = predicate.name
                result["Parameters"] = predicate.arguments
            elif isinstance(predicate, ComposedPredicate):
                result["preconditionString"] = predicate.string
                result["isNegated?"] = predicate.isNegated
                result["isOperation?"] = predicate.isComplex
                result["Name"] = predicate.name
                result["Parameters"] = []
                for parameter in predicate.arguments:
                    result["Parameters"].append(makeDictOfPredicates(parameter))
            elif isinstance(predicate, ConstantPredicate):
                result["preconditionString"] = predicate.value
                result["Name"] = predicate.name
                result["Parameters"] = predicate.arguments
                result["isNegated?"] = predicate.isNegated
                result["isOperation?"] = predicate.isComplex
            return result

        result = makeDictOfPredicates(self.__predicate)

        return result

