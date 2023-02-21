from libs.pyGrounder.myClasses.SimplePredicate import SimplePredicate
from libs.pyGrounder.myClasses.NegatedPredicate import NegatedPredicate
from libs.pyGrounder.myClasses.ConstantPredicate import ConstantPredicate
from libs.pyGrounder.myClasses.ComposedPredicate import ComposedPredicate
from libs.pyGrounder.myClasses.myUtilities import process_string

class Effect():

    '''
    The Effect class represents one Effect for the action/process/event. It only contains one predicate, that can be a SimplePredicate, NegatedPredicate or ComposedPredicate
    
    Parameters
    ----------
    node : antrl4 tree
    
    OR
    
    predicate : SimplePredicate | NegatedPredicate | ComposedPredicate
    
    Attributes
    ----------
    predicate : SimplePredicate | NegatedPredicate | ComposedPredicate '''

    __predicate = None


    def __init__(self, node = None, predicate = None):

        if node is not None:
            string = node.getText()
            OPERATORS = [">", ">=", "<", "<=", "assign", "increase", "decrease", "*"]
            predicateString = process_string(string)
            predicate = predicateString.split(" ")
            if predicate[0] == "not":
                self.__predicate = NegatedPredicate(node.getChild(3), predicateString)
            elif predicate[0] in OPERATORS:
                self.__predicate = ComposedPredicate(node, predicateString)
            else:
                self.__predicate = SimplePredicate(predicateString)
        else:
            self.__predicate = predicate

    def ground(self, combination):
        return Effect(predicate=self.predicate.ground(combination))

    def __str__(self):
        return str(self.__predicate)

    def __repr__(self):
        return str(self)

    def predicateAsDict(self):
        '''
        It returns the dict containing the details of the Precondition in order to write its Json representation
        '''

        def makeDictOfPredicates(predicate):
            result = {}
            if not isinstance(predicate, ComposedPredicate) and not isinstance(predicate, ConstantPredicate):
                result["effect"] = predicate.string
                result["isNegated?"] = predicate.isNegated
                result["isOperation?"] = predicate.isComplex
                result["Name"] = predicate.name
                result["Parameters"] = predicate.arguments
            elif isinstance(predicate, ComposedPredicate):
                result["effectString"] = predicate.string
                result["isNegated?"] = predicate.isNegated
                result["isOperation?"] = predicate.isComplex
                result["Name"] = predicate.name
                result["Parameters"] = []
                for parameter in predicate.arguments:
                    result["Parameters"].append(makeDictOfPredicates(parameter))
            elif isinstance(predicate, ConstantPredicate):
                result["effectString"] = predicate.value
                result["Name"] = predicate.name
                result["Parameters"] = predicate.arguments
                result["isNegated?"] = predicate.isNegated
                result["isOperation?"] = predicate.isComplex
            return result

        result = makeDictOfPredicates(self.__predicate)
        
        return result

    @property
    def predicate(self):
        return self.__predicate