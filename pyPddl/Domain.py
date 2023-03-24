from __future__ import annotations
from typing import Dict, List, Set, cast

from Atom import Atom
from antlr4_directory.pddlParser import pddlParser
from Operation import Operation
from Problem import Problem

from Utilities import Utilities
from Variable import Variable
from Action import Action
from Event import Event
from Process import Process

from Type import Type
from TypedPredicate import TypedPredicate


class Domain:
    name = str
    requirements: List[str]
    types: Dict[str, Type]
    predicates: set[TypedPredicate]
    functions: set[TypedPredicate]
    actions: set[Action]
    events: set[Event]
    processes: set[Process]
    constants: set[Variable]
    __operationsDict: Dict[str, Operation]

    def __init__(self):
        self.types = dict()
        self.predicates = set()
        self.functions = set()
        self.actions = set()
        self.processes = set()
        self.events = set()
        self.requirements = list()
        self.constants = set()
        pass

    def ground(self, problem: Problem, avoidSimplification=False) -> GroundedDomain:

        gActions: Set[Action] = set([g for action in self.actions for g in action.ground(problem)])
        gEvents: Set[Event] = set([g for event in self.events for g in event.ground(problem)])
        gProcess: Set[Process] = set([g for process in self.processes for g in process.ground(problem)])

        gDomain = GroundedDomain(self.name, gActions, gEvents, gProcess)

        if avoidSimplification:
            return gDomain

        from RPG import RPG
        from ARPG import ARPG

        rpg = RPG(gDomain, problem)
        arpg = ARPG(rpg.getReachableActions(), problem)

        self.actions = rpg.getReachableActions()
        constants: Dict[Atom, float] = arpg.getConstantAtoms()

        gDomain = gDomain.substitute(constants)
        gDomain.arpg = ARPG(gDomain.actions, problem)
        return gDomain

    @classmethod
    def fromNode(cls, node: pddlParser.DomainContext) -> Domain:

        domain = cls()

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            if isinstance(child, pddlParser.DomainNameContext):
                domain.__setDomainName(child)
            elif isinstance(child, pddlParser.RequirementsContext):
                domain.__setRequirementsList(child)
            elif isinstance(child, pddlParser.TypesContext):
                domain.__setTypesList(child)
            elif isinstance(child, pddlParser.PredicatesContext):
                domain.__setPredicates(child)
            elif isinstance(child, pddlParser.FunctionsContext):
                domain.__setFunctions(child)
            elif isinstance(child, pddlParser.ActionContext):
                domain.actions.add(Action.fromNode(child))
            elif isinstance(child, pddlParser.EventContext):
                domain.events.add(Event.fromNode(child))
            elif isinstance(child, pddlParser.ProcessContext):
                domain.processes.add(Process.fromNode(child))

        return domain

    @classmethod
    def fromFile(cls, filename) -> Domain:
        f = open(filename, 'r')
        domainString = f.read()
        f.close()
        domainString = Utilities.removeComments(domainString)

        parseTree: pddlParser = Utilities.getParseTree(domainString)
        return cls.fromNode(parseTree.domain())

    def __setDomainName(self, node: pddlParser.DomainNameContext):
        self.name = node.getChild(2).getText()

    def __setRequirementsList(self, node: pddlParser.RequirementsContext):
        for child in node.children:
            if not isinstance(child, pddlParser.RequireKeyContext):
                continue
            self.requirements.append(child.getText())

    def __setTypesList(self, node: pddlParser.TypesContext):
        for child in node.children:
            if not isinstance(child, pddlParser.TypeContext):
                continue
            name = child.getText()
            self.types[name] = Type(name)

    def __setPredicates(self, node: pddlParser.PredicatesContext):
        for child in node.children:
            if not isinstance(child, pddlParser.PositiveLiteralContext):
                continue
            self.predicates.add(TypedPredicate.fromNode(child, self.types))

    def __setFunctions(self, node: pddlParser.FunctionsContext):
        for child in node.children:
            if not isinstance(child, pddlParser.PositiveLiteralContext):
                continue
            self.functions.add(TypedPredicate.fromNode(child, self.types))


class GroundedDomain(Domain):
    __operationsDict: Dict[str, Operation] = dict()
    functions: Set[Atom]
    predicates: Set[Atom]
    pre: Dict[Atom, Set[Operation]]
    preN: Dict[Atom, Set[Operation]]
    preB: Dict[Atom, Set[Operation]]
    addList: Dict[Atom, Set[Operation]]
    delList: Dict[Atom, Set[Operation]]
    assList: Dict[Atom, Set[Operation]]

    def __init__(self, name: str, actions: Set[Action], events: Set[Event], process: Set[Process]):
        super().__init__()

        self.name = name
        self.actions = actions
        self.events = events
        self.processes = process

        self.operations: Set[Operation] = set()
        self.operations.update(self.actions)
        self.operations.update(self.events)
        self.operations.update(self.processes)

        self.functions: Set[Atom] = set()
        self.predicates: Set[Atom] = set()
        self.allAtoms: Set[Atom] = set()
        self.preB: Dict[Atom, Set[Operation]] = dict()
        self.addList: Dict[Atom, Set[Operation]] = dict()
        self.delList: Dict[Atom, Set[Operation]] = dict()
        self.assList: Dict[Atom, Set[Operation]] = dict()

        for op in self.operations:
            self.__operationsDict[op.planName] = op
            self.functions |= op.getFunctions()
            self.predicates |= op.getPredicates()

            for v in op.getPreB():
                self.preB.setdefault(v, set())
                self.preB[v].add(op)
            for v in op.getAddList():
                self.addList.setdefault(v, set())
                self.addList[v].add(op)
            for v in op.getDelList():
                self.delList.setdefault(v, set())
                self.delList[v].add(op)
            for v in op.getAssList():
                self.assList.setdefault(v, set())
                self.assList[v].add(op)

        self.allAtoms = self.functions | self.predicates
        self.arpg = None

    def getOperationByPlanName(self, planName) -> Operation:
        return self.__operationsDict[planName]

    def substitute(self, sub: Dict[Atom, float], default=None) -> GroundedDomain:
        subActions: Set[Action] = {a.substitute(sub, default) for a in self.actions}

        return GroundedDomain(self.name, subActions, self.events, self.processes)

    def getARPG(self):
        return self.arpg
