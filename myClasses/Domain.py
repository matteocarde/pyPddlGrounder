from typing import Dict

from libs.pyGrounder.myClasses.Operation import Operation
from libs.pyGrounder.myClasses.myUtilities import remove_comments
from libs.pyGrounder.myClasses.myUtilities import get_antlr4_parsetree
from libs.pyGrounder.myClasses.Variable import Variable
from libs.pyGrounder.myClasses.Predicate import Predicate
from libs.pyGrounder.myClasses.Function import Function
from libs.pyGrounder.myClasses.Action import Action
from libs.pyGrounder.myClasses.Event import Event
from libs.pyGrounder.myClasses.Process import Process

import json


class Domain:
    __name = str
    __requirements: list
    __types: list
    __predicates: set[Predicate]
    __functions: set[Function]
    __actions: set[Action]
    __events: set[Event]
    __processes: set[Process]
    __constants: set[Variable]

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
            result = set()
            for child in range(node.getChildCount()):
                child_node = node.getChild(child)
                child_string = child_node.getText()
                if child_string != '(' and child_string != ')' and child_string != ':predicates':
                    result.add(Predicate(child_node))
            return result

        def getFunctionsList(node):
            result = set()
            for child in range(node.getChildCount()):
                child_node = node.getChild(child)
                child_string = child_node.getText()
                if child_string != '(' and child_string != ')' and child_string != ':functions':
                    result.add(Function(child_node))
            return result

        if file_path is not None:
            file = remove_comments(file_path)
            tree = get_antlr4_parsetree(file).domain()
            self.__actions = set()
            self.__processes = set()
            self.__events = set()
            self.__requirements = []
            self.__constants = set()
            for i in range(tree.getChildCount()):
                child = tree.getChild(i)
                childText = child.getText()
                if 'domain' in childText:
                    self.__name = getDomainName(childText)
                elif ':requirements' in childText:
                    self.__requirements = getRequirementsList(child)
                elif ':types' in childText:
                    self.__types = getTypesList(child)
                    # to do constants self.__constants =
                elif ':predicates' in childText:
                    self.__predicates = getPredicatesList(child)
                elif ':functions' in childText:
                    self.__functions = getFunctionsList(child)
                elif ':action' in childText:
                    self.__actions.add(Action(child))
                elif ':process' in childText:
                    self.__processes.add(Process(child))
                elif ':event' in childText:
                    self.__events.add(Event(child))
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
        for t in self.__types:
            f.write(" " + t)
        f.write(")\n")

        # write the constants
        if self.__constants is not None:
            f.write(" " * 4 + "(:constants" + "\n")
            for constant in self.__constants:
                f.write(" " * 8 + str(constant) + "\n")
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

    def printAll(self):
        print("----------------------------Domain name: ------------------------------------------------")
        print(self.__name + "\n")
        print("----------------------------Requirements: ---------------------------------------------- ")
        print(str(self.__requirements) + "\n")
        print("----------------------------Types : -----------------------------------------------------")
        print(str(self.__types) + "\n")
        if self.__constants is not None:
            print("-----------------------------Constants: -------------------------------------------------")
            for constant in self.__constants:
                print(str(constant))
        print("-----------------------------Functions: -------------------------------------------------")
        for func in self.__functions:
            print(str(func))
        print("\n")
        print("----------------------------Predicates: -------------------------------------------------")
        for pred in self.__predicates:
            print(str(pred))
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
        def getConstants(c):
            result = []
            for constant in c:
                result.append({"constantName": constant.name, "constantType": constant.type})
            return result

        def getPredicates(c):
            result = []
            for predicate in c:
                result.append({"predicateName": predicate.name, "predicateParameters": predicate.argumentsAsList})
            return result

        def getFunctions(c):
            result = []
            for function in c:
                result.append({"predicateName": function.name, "predicateParameters": function.argumentsAsList})
            return result

        def getAEP(operation, PaE):
            result = dict()
            result[PaE + "Name"] = operation.name
            result[PaE + "Parameters"] = getParameters(operation)
            result[PaE + "Preconditions"] = getPreconditions(operation)
            result[PaE + "Effects"] = getEffects(operation)
            return result

        def getParameters(operation):
            result = []
            for parameter in operation.parameters:
                result.append({"parameterName": parameter.name, "parameterType": parameter.type})
            return result

        def getPreconditions(operation):
            result = []
            for precondition in operation.preconditions:
                result.append(precondition.predicateAsDict())
            return result

        def getEffects(operation):
            result = []
            for effect in operation.effects:
                result.append(effect.predicateAsDict())
            return result

        json_data = dict()
        json_data['domain'] = self.__name
        json_data['requirements'] = self.__requirements
        json_data['types'] = self.__types
        if self.__constants is not None:
            json_data['constants'] = getConstants(self.__constants)
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
        with open(file_path + "/" + filename + ".json", 'w') as json_file:
            json.dump(self.toJson(), json_file, indent=4)
        pass
