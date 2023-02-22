from itertools import product
from typing import Dict, Tuple, List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes.OperationType import OperationType
from libs.pyGrounder.classes.Parameter import Parameter
from libs.pyGrounder.classes.Problem import Problem
from libs.pyGrounder.classes.Effects import Effects
from libs.pyGrounder.classes.Preconditions import Preconditions
from libs.pyGrounder.classes.Type import Type


class Operation:
    name: str
    parameters: List[Tuple[str, Type]]
    preconditions: Preconditions
    effects: Effects

    def __init__(self, node: p.ActionContext or p.EventContext or p.ProcessContext, types: Dict[str, Type]):
        self.parameters = []
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                self.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                self.__setParameters(child.getChild(1), types)
            elif isinstance(child, p.OpPreconditionContext):
                self.__addPreconditions(child)
            elif isinstance(child, p.OpEffectContext):
                self.__addEffects(child)

    def __setParameters(self, node: p.ParametersContext, types: Dict[str, Type]):
        for child in node.children:
            if not isinstance(child, p.TypedAtomParameterContext):
                continue
            varName = child.getChild(0).getText()
            varType = child.getChild(2).getText()
            self.parameters.append((varName, types[varType]))

    def __addPreconditions(self, node: p.OpPreconditionContext):
        self.preconditions = Preconditions(node.getChild(1))

    def __addEffects(self, node: p.OpEffectContext):
        self.effects = Effects(node.getChild(1))

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

    def __getGroundedPlanName(self, combination):
        parameters = ''.join([c.split('-')[0] for c in combination])
        return f"({self.name} {parameters})"

    def getGroundedOperations(self, problem):
        combinations = self.__getCombinations(problem)
        gOperations = []
        for combination in combinations:
            gPreconditions = [p.ground(combination) for p in self.preconditions]
            gEffects = [e.ground(combination) for e in self.effects]
            operation: Operation = Operation(name=self.__getGroundedName(combination),
                                             planName=self.__getGroundedPlanName(combination),
                                             preconditions=gPreconditions, effects=gEffects)
            gOperations.append(operation)
        return gOperations

    @property
    def type(self) -> OperationType:
        raise NotImplemented()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
