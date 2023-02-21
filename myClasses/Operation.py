from enum import Enum
from itertools import product

from libs.pyGrounder.myClasses.OperationType import OperationType
from libs.pyGrounder.myClasses.Parameter import Parameter
from libs.pyGrounder.myClasses.Precondition import Precondition
from libs.pyGrounder.myClasses.Effect import Effect
from libs.pyGrounder.myClasses.Problem import Problem


class Operation:
    __name = ""
    __parameters = [Parameter]
    __preconditions = []
    __effects = []
    planName: str

    def __init__(self, node=None, name=None, planName=None, preconditions=None, effects=None):

        self.planName = planName
        if node is not None:
            node = node.getChild(0)
            self.__name = node.getChild(2).getText()
            self.__parameters = self.__parseParameters(node)
            self.__preconditions = self.__parsePreconditions(node)
            self.__effects = self.__parseEffects(node)
        else:
            self.__name = name
            self.__parameters = []
            self.__preconditions = preconditions
            self.__effects = effects

    @property
    def type(self) -> OperationType:
        raise NotImplemented()

    @staticmethod
    def __parseParameters(node):
        result = []
        for child in range(5, node.getChildCount() - 1):
            if node.getChild(child).getText() == ')':
                return result
            else:
                result.append(Parameter(node.getChild(child).getText()))

    @staticmethod
    def __parsePreconditions(node):
        result = []
        for child in range(node.getChildCount() - 1):
            if ":precondition" in node.getChild(child).getText():
                node = node.getChild(child)
                break
        for child in range(3, node.getChildCount() - 1):
            precondition = Precondition(node.getChild(child))
            result.append(precondition)
        return result

    @staticmethod
    def __parseEffects(node):
        result = []
        for child in range(node.getChildCount() - 1):
            text = node.getChild(child).getText()
            if ":effect" in text:
                node = node.getChild(child)
                break
        for child in range(3, node.getChildCount() - 1):
            effect = Effect(node.getChild(child))
            result.append(effect)
        return result

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters):
        self.__name = parameters

    @property
    def preconditions(self):
        return self.__preconditions

    @preconditions.setter
    def preconditions(self, preconditions):
        self.__preconditions = preconditions

    @property
    def effects(self):
        return self.__effects

    def printParameters(self):
        print("PARAMETERS: ")
        if self.__parameters:
            for parameter in self.__parameters:
                print(parameter.toString())
        else:
            print("()")
        # print("\n")

    def printPreconditions(self):
        print("PRECONDITIONS: ")
        for precondition in self.__preconditions:
            precondition.getString()
            # print("\n")

    def printEffects(self):
        print("EFFECTS: ")
        for effect in self.__effects:
            effect.getString()
            # print("\n")

    def __getCombinations(self, problem: Problem):
        combinations = []
        objects_dict = {}
        for obj in problem.objects:
            objects_dict[obj["objectType"]] = obj["objectInstances"]

        param: Parameter
        for param in self.parameters:
            param_objects = objects_dict[param.type]
            param_combinations = []
            for obj in param_objects:
                param_combinations.append(obj + "-" + param.name)
            combinations.append(param_combinations)
        return list(product(*combinations))

    def __getGroundedName(self, parameters):
        groundedName = self.name
        for p in parameters:
            groundedName = groundedName + "_" + p.split("-")[0]
        return groundedName

    def __getPlanName(self, combination):
        parameters = ''.join([c.split('-')[0] for c in combination])
        return f"({self.name} {parameters})"

    def getGroundedOperations(self, problem):
        combinations = self.__getCombinations(problem)
        gOperations = []
        for combination in combinations:
            gPreconditions = [p.ground(combination) for p in self.preconditions]
            gEffects = [e.ground(combination) for e in self.effects]
            operation: Operation = Operation(name=self.__getGroundedName(combination),
                                             planName=self.__getPlanName(combination),
                                             preconditions=gPreconditions, effects=gEffects)
            gOperations.append(operation)
        return gOperations

    def write(self, f, ActionEventProcess: str):

        f.write(" " * 4 + "(:" + ActionEventProcess + " " + self.__name + "\n")
        if self.__parameters:
            f.write(" " * 8 + ":parameters (")
            for parameter in self.__parameters:
                f.write(" " + parameter.toString())
            f.write(" )" + "\n")
        else:
            f.write(" " * 8 + ":parameters ()" + "\n")
        f.write(" " * 8 + ":precondition (and" + "\n")
        for precondition in self.__preconditions:
            f.write(" " * 10 + precondition.predicate.toString() + "\n")
        f.write(" " * 8 + ")" + "\n")
        f.write(" " * 8 + ":effect (and" + "\n")
        for effect in self.__effects:
            f.write(" " * 10 + effect.predicate.toString() + "\n")
        f.write(" " * 8 + ")" + "\n")
        f.write(" " * 4 + ")\n")

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


