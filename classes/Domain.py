from __future__ import annotations
from typing import Dict, List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Operation import Operation

from libs.pyGrounder.classes.Utilities import Utilities
from libs.pyGrounder.classes.Variable import Variable
from libs.pyGrounder.classes.Action import Action
from libs.pyGrounder.classes.Event import Event
from libs.pyGrounder.classes.Process import Process

from libs.pyGrounder.classes.Type import Type
from libs.pyGrounder.classes.TypedPredicate import TypedPredicate


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

    def __init__(self, node: pddlParser.DomainContext = None):

        if node is None:
            return

        self.types = dict()
        self.predicates = set()
        self.functions = set()
        self.actions = set()
        self.processes = set()
        self.events = set()
        self.requirements = []
        self.constants = set()

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            if isinstance(child, pddlParser.DomainNameContext):
                self.__setDomainName(child)
            elif isinstance(child, pddlParser.RequirementsContext):
                self.__setRequirementsList(child)
            elif isinstance(child, pddlParser.TypesContext):
                self.__setTypesList(child)
            elif isinstance(child, pddlParser.PredicatesContext):
                self.__setPredicates(child)
            elif isinstance(child, pddlParser.FunctionsContext):
                self.__setFunctions(child)
            elif isinstance(child, pddlParser.ActionContext):
                self.actions.add(Action(child, self.types))
            elif isinstance(child, pddlParser.EventContext):
                self.events.add(Event(child, self.types))
            elif isinstance(child, pddlParser.ProcessContext):
                self.processes.add(Process(child, self.types))

    @classmethod
    def fromFile(cls, filename) -> Domain:
        f = open(filename, 'r')
        domainString = f.read()
        f.close()
        domainString = Utilities.removeComments(domainString)

        parseTree: pddlParser = Utilities.getParseTree(domainString)
        domain = cls(parseTree.domain())
        return domain

    def __setDomainName(self, node: pddlParser.DomainNameContext):
        self.name = node.getChild(2)

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
            self.predicates.add(TypedPredicate(child, self.types))

    def __setFunctions(self, node: pddlParser.FunctionsContext):
        for child in node.children:
            if not isinstance(child, pddlParser.PositiveLiteralContext):
                continue
            self.functions.add(TypedPredicate(child, self.types))
