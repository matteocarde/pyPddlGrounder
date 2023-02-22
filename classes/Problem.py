import json
from typing import Dict, List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.InitialCondition import InitialCondition
from libs.pyGrounder.classes.Goal import Goal
from libs.pyGrounder.classes.Utilities import Utilities


class Problem:
    name: str
    domainName: str
    objectsByType: Dict[str, List[str]]
    init: InitialCondition
    goal: Goal

    def __init__(self, node: pddlParser.ProblemContext):

        self.objectsByType = dict()
        for node in node.getChildren():
            if isinstance(node, pddlParser.ProblemNameContext):
                self.__setProblemName(node)
            if isinstance(node, pddlParser.ProblemDomainContext):
                self.__setDomainName(node)
            if isinstance(node, pddlParser.ObjectsContext):
                self.__addObjects(node)
            if isinstance(node, pddlParser.InitContext):
                self.init = InitialCondition.fromNode(node)
            if isinstance(node, pddlParser.GoalContext):
                self.goal = Goal.fromNode(node)
            pass

    def __setProblemName(self, node: pddlParser.ProblemNameContext):
        self.name = node.getChild(2).getText()

    def __setDomainName(self, node: pddlParser.ProblemDomainContext):
        self.domainName = node.getChild(2).getText()

    def __addObjects(self, node: pddlParser.ObjectsContext):
        for typeNode in node.children:
            if not isinstance(typeNode, pddlParser.TypedObjectsContext):
                continue
            typeStr: str = ""
            objects = []
            for child in typeNode.children:
                if isinstance(child, pddlParser.GroundAtomParameterContext):
                    objects.append(child.getText())
                elif isinstance(child, pddlParser.TypeNameContext):
                    typeStr = child.getText()
            self.objectsByType.setdefault(typeStr, [])
            self.objectsByType[typeStr].extend(objects)

    @classmethod
    def fromFile(cls, filename):
        f = open(filename, 'r')
        domainString = f.read()
        f.close()
        domainString = Utilities.removeComments(domainString)

        parseTree: pddlParser = Utilities.getParseTree(domainString)
        return cls(parseTree.problem())
