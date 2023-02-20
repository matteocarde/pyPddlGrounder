from typing import Dict, List

from libs.pyGrounder.myClasses.Operation import Operation
from libs.pyGrounder.myClasses.myUtilities import remove_comments
from libs.pyGrounder.myClasses.myUtilities import get_antlr4_parsetree
from libs.pyGrounder.myClasses.Variable import Variable
from libs.pyGrounder.myClasses.Predicate import Predicate
from libs.pyGrounder.myClasses.Function import Function
from libs.pyGrounder.myClasses.Action import Action
from libs.pyGrounder.myClasses.Event import Event
from libs.pyGrounder.myClasses.Process import Process
from libs.pyGrounder.myClasses.SimplePredicate import SimplePredicate
from libs.pyGrounder.myClasses.NegatedPredicate import NegatedPredicate
from libs.pyGrounder.myClasses.ConstantPredicate import ConstantPredicate
from libs.pyGrounder.myClasses.ComposedPredicate import ComposedPredicate
from libs.pyGrounder.myClasses.Precondition import Precondition
from libs.pyGrounder.myClasses.Effect import Effect

from itertools import product
import json


class Domain:
    '''
    It represents the pddl Domain.
    
    Parameters
    ----------
    file_path : string
        The path of the domain.pddl file
        
    OR
    
    name : str
        The name of the domain
    requirements : List[str]
        The list of the requirements
    types : list[str]
        The list of the types
    constants : list[Variable]
        The list of constants
    predicates : list[Predicate]
        The list of predicates
    functions : list[Function]
        The list of functions
    actions : list[Action]
        The list of actions
    events : list [Event]
        The list of event
    processes : list[Process]
        The list of processes'''
    __name = str
    __requirements: list
    __types: list
    __predicates: list[Predicate]
    __functions: list[Function]
    __actions: list[Action]
    __events: list[Event]
    __processes: list[Process]
    __constants: list[Variable]

    __operationsDict: Dict[str, Operation]

    def __init__(self, file_path=None, name=None, requirements=None, constants=None, types=None, predicates=None,
                 functions=None, actions=None, events=None, processes=None):

        def getDomainName(stringa):
            stringa = stringa.replace("(domain", "")
            stringa = stringa.replace(")", "")
            return stringa.strip()

        def getRequirementsList(node):
            result = []
            for child in range(node.getChildCount()):
                stringa = node.getChild(child).getText()
                if stringa != '(' and stringa != ')' and stringa != ':requirements':
                    result.append(stringa)
            return result

        def getTypesList(node):
            result = []
            for child in range(node.getChildCount()):
                stringa = node.getChild(child).getText()
                if stringa != '(' and stringa != ')' and stringa != ':types':
                    result.append(stringa)
            return result

        def getPredicatesList(node):
            result = []
            for child in range(node.getChildCount()):
                child_node = node.getChild(child)
                child_string = child_node.getText()
                if child_string != '(' and child_string != ')' and child_string != ':predicates':
                    result.append(Predicate(child_node))
            return result

        def getFunctionsList(node):
            result = []
            for child in range(node.getChildCount()):
                child_node = node.getChild(child)
                child_string = child_node.getText()
                if child_string != '(' and child_string != ')' and child_string != ':functions':
                    result.append(Function(child_node))
            return result

        if file_path != None:
            file = remove_comments(file_path)
            tree = get_antlr4_parsetree(file).domain()
            self.__actions = []
            self.__processes = []
            self.__events = []
            self.__requirements = []
            self.__constants = None
            for i in range(tree.getChildCount()):
                if 'domain' in tree.getChild(i).getText():
                    self.__name = getDomainName(tree.getChild(i).getText())
                elif ':requirements' in tree.getChild(i).getText():
                    self.__requirements = getRequirementsList(tree.getChild(i))
                elif ':types' in tree.getChild(i).getText():
                    self.__types = getTypesList(tree.getChild(i))
                    # to do constants self.__constants =
                elif ':predicates' in tree.getChild(i).getText():
                    self.__predicates = getPredicatesList(tree.getChild(i))
                elif ':functions' in tree.getChild(i).getText():
                    self.__functions = getFunctionsList(tree.getChild(i))
                elif ':action' in tree.getChild(i).getText():
                    self.__actions.append(Action(tree.getChild(i)))
                elif ':process' in tree.getChild(i).getText():
                    self.__processes.append(Process(tree.getChild(i)))
                elif ':event' in tree.getChild(i).getText():
                    self.__events.append(Event(tree.getChild(i)))
        else:
            self.__name = name
            self.__requirements = requirements
            self.__types = types
            self.__constants = constants
            self.__predicates = predicates
            self.__functions = functions
            self.__actions = actions
            self.__processes = processes
            self.__events = events

    @property
    def name(self):
        return self.__name

    @property
    def requirements(self):
        return self.__requirements

    @property
    def constants(self):
        return self.__constants

    @property
    def types(self):
        return self.__types

    @property
    def predicates(self):
        return self.__predicates

    @property
    def functions(self):
        return self.__functions

    @property
    def actions(self):
        return self.__actions

    @property
    def events(self):
        return self.__events

    @property
    def processes(self):
        return self.__processes

    def writePddl(self, file_path: str, filename: str):
        f = open(file_path + "/" + filename + ".pddl", "w")

        # write the domain
        f.write("(define (domain " + self.__name + ")\n")

        # write the requirements
        f.write(" " * 4 + "(:requirements")
        for requirement in self.__requirements:
            f.write(" " + requirement)
        f.write(")\n")

        # write the types
        f.write(" " * 4 + "(:types")
        for type in self.__types:
            f.write(" " + type)
        f.write(")\n")

        # write the constants
        if self.__constants != None:
            f.write(" " * 4 + "(:constants" + "\n")
            for constant in self.__constants:
                f.write(" " * 8 + constant.toString() + "\n")
            f.write(" " * 4 + ")\n")

        # write the predicates
        f.write(" " * 4 + "(:predicates" + "\n")
        for predicate in self.__predicates:
            predicate.write(f)
        f.write(" " * 4 + ")\n")

        # write the functions
        f.write(" " * 4 + "(:functions" + "\n")
        for function in self.__functions:
            function.write(f)
        f.write(" " * 4 + ")\n")

        # write the actions
        for action in self.__actions:
            action.write(f, "action")

        # write the processes
        for process in self.__processes:
            process.write(f, "process")

        # write the events
        for event in self.__events:
            event.write(f, "event")

        f.write(")")

        f.close()

    def getOperationFromString(self, opStr):
        pass

    def printAll(self):
        print("----------------------------Domain name: ------------------------------------------------")
        print(self.__name + "\n")
        print("----------------------------Requirements: ---------------------------------------------- ")
        print(str(self.__requirements) + "\n")
        print("----------------------------Types : -----------------------------------------------------")
        print(str(self.__types) + "\n")
        if self.__constants != None:
            print("-----------------------------Constants: -------------------------------------------------")
            for constant in self.__constants:
                print(constant.toString())
        print("-----------------------------Functions: -------------------------------------------------")
        for func in self.__functions:
            print(func.toString())
        print("\n")
        print("----------------------------Predicates: -------------------------------------------------")
        for pred in self.__predicates:
            print(pred.toString())
        print("\n")
        print("------------------------------Actions: -------------------------------------------------")
        for action in self.__actions:
            print(action.name)
            action.printParameters()
            action.printPreconditions()
            action.printEffects()
            print("\n")
        print("\n \n \n")
        print("-----------------------------Processes: ------------------------------------------------")
        for process in self.__processes:
            print(process.name)
            process.printParameters()
            process.printPreconditions()
            process.printEffects()
            print("\n")
        print("\n \n \n")
        print("------------------------------Events: --------------------------------------------------")
        for event in self.__events:
            print(event.name)
            event.printParameters()
            event.printPreconditions()
            event.printEffects()
            print("\n")
        print("\n \n \n")

    def toJson(self):
        '''
        Returns a dictionary containing attributes represented in a json format
        '''

        def getConstants(List):
            result = []
            for constant in List:
                result.append({"constantName": constant.name, "constantType": constant.type})
            return result

        def getPredicates(List):
            result = []
            for predicate in List:
                result.append({"predicateName": predicate.name, "predicateParameters": predicate.argumentsAsList})
            return result

        def getFunctions(List):
            result = []
            for function in List:
                result.append({"predicateName": function.name, "predicateParameters": function.argumentsAsList})
            return result

        def getAEP(Operation, PaE):
            result = {}
            result[PaE + "Name"] = Operation.name
            result[PaE + "Parameters"] = getParameters(Operation)
            result[PaE + "Preconditions"] = getPreconditions(Operation)
            result[PaE + "Effects"] = getEffects(Operation)
            return result

        def getParameters(Operation):
            result = []
            for parameter in Operation.parameters:
                result.append({"parameterName": parameter.name, "parameterType": parameter.type})
            return result

        def getPreconditions(Operation):
            result = []
            for precondition in Operation.preconditions:
                result.append(precondition.predicateAsDict())
            return result

        def getEffects(Operation):
            result = []
            for effect in Operation.effects:
                result.append(effect.predicateAsDict())
            return result

        json_data = {}
        json_data['domain'] = self.__name
        json_data['requirements'] = self.__requirements
        json_data['types'] = self.__types
        if self.__constants != None: json_data['constants'] = getConstants(self.__constants)
        json_data['predicates'] = []
        json_data['predicates'] = getPredicates(self.__predicates)
        json_data['functions'] = getFunctions(self.__functions)
        json_data['actions'] = []
        json_data['processes'] = []
        json_data['events'] = []

        for action in self.__actions:
            json_data['actions'].append(getAEP(action, "action"))
        for process in self.__processes:
            json_data['processes'].append(getAEP(process, "process"))
        for event in self.__events:
            json_data['events'].append(getAEP(event, "event"))

        return json_data

    def writeJson(self, file_path: str, filename: str):
        '''
        It writes the json representation of the Domain

        Parameters
        ----------
        file_path : str
            The path to the folder where the json file will be saved
        filename : str
            The name of the file that will be written
        '''
        with open(file_path + "/" + filename + ".json", 'w') as json_file:
            json.dump(self.toJson(), json_file, indent=4)
        pass
