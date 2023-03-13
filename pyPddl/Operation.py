import itertools
from itertools import product
from typing import Dict, Tuple, List, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Literal import Literal
from antlr4_directory.pddlParser import pddlParser as p
from OperationType import OperationType
from Parameter import Parameter
from Problem import Problem
from Effects import Effects
from Preconditions import Preconditions


class Operation:
    name: str
    planName: str
    parameters: List[Parameter]
    preconditions: Preconditions
    effects: Effects

    def __init__(self):
        self.parameters = list()

    @classmethod
    def fromNode(cls, node: p.ActionContext or p.EventContext or p.ProcessContext):
        operation = cls()
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                operation.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                operation.__setParameters(child.getChild(1))
            elif isinstance(child, p.OpPreconditionContext):
                operation.__addPreconditions(child)
            elif isinstance(child, p.OpEffectContext):
                operation.__addEffects(child)

        return operation

    def __setParameters(self, node: p.ParametersContext):
        for child in node.children:
            if not isinstance(child, p.TypedAtomParameterContext):
                continue
            varNames = []
            varType = None
            for x in child.children:
                if isinstance(x, p.LiftedAtomParameterContext):
                    varNames.append(x.getText())
                elif isinstance(x, p.TypeNameContext):
                    varType = x.getText()

            for name in varNames:
                self.parameters.append(Parameter(name, varType))

    def __addPreconditions(self, node: p.OpPreconditionContext):
        self.preconditions = Preconditions.fromNode(node.getChild(1))

    def __addEffects(self, node: p.OpEffectContext):
        self.effects = Effects.fromNode(node.getChild(1))

    def __getCombinations(self, problem: Problem) -> List[Dict[str, str]]:
        subs: List[List[str]] = list()
        for parameter in self.parameters:
            subs.append(problem.objectsByType[parameter.type])

        combinations: List[Dict[str, str]] = list()
        for sub in itertools.product(*subs):
            comb: Dict[str, str] = dict()
            for i, parameter in enumerate(self.parameters):
                comb[parameter.name] = sub[i]
            combinations.append(comb)

        return combinations

    def getGroundedOperations(self, problem):
        combinations: List[Dict[str, str]] = self.__getCombinations(problem)
        gOperations = []
        for subs in combinations:
            operation: Operation = Operation()
            operation.name = self.__getGroundedName(subs)
            operation.preconditions = self.preconditions.ground(subs)
            operation.effects = self.effects.ground(subs)
            operation.planName = self.__getGroundedPlanName(subs)
            gOperations.append(operation)
        return gOperations

    def __getGroundedName(self, sub: Dict[str, str]) -> str:
        parts = [self.name] + [c[1] for c in sub.items()]
        return "_".join(parts)

    def __getGroundedPlanName(self, sub: Dict[str, str]):
        parts = [self.name] + [c[1] for c in sub.items()]
        return f"({'_'.join(parts)})"

    @property
    def type(self) -> OperationType:
        raise NotImplemented()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def getFunctions(self) -> Set[Atom]:
        return self.preconditions.getFunctions() | self.effects.getFunctions()

    def getPredicates(self) -> Set[Atom]:
        return self.preconditions.getPredicates() | self.effects.getPredicates()

    def getPreN(self) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.preconditions:
            if not isinstance(c, BinaryPredicate):
                continue
            atomList = atomList | {c.getAtom()}
        return atomList
        pass

    def getPreB(self) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.preconditions:
            if not isinstance(c, Literal):
                continue
            atomList = atomList | {c.getAtom()}
        return atomList
        pass

    def getLiteralList(self, sign: str) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.effects:
            if not isinstance(c, Literal) or c.sign != sign:
                continue
            atomList = atomList | c.getPredicates()
        return atomList

    def getModificationList(self, modificator: str) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.effects:
            if not isinstance(c, BinaryPredicate) or c.operator != modificator:
                continue
            atomList = atomList | c.getFunctions()
        return atomList

    def getAddList(self) -> Set[Atom]:
        return self.getLiteralList("+") | self.getModificationList("increase")

    def getDelList(self) -> Set[Atom]:
        return self.getLiteralList("-") | self.getModificationList("decrease")

    def getAssList(self) -> Set[Atom]:
        return self.getModificationList("assign")
