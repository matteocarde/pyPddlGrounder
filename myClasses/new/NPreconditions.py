from typing import List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.myClasses.new import NPredicate
from libs.pyGrounder.myClasses.new.NBinaryPredicate import NBinaryPredicate
from libs.pyGrounder.myClasses.new.NLiteral import NLiteral


class NPreconditions:
    conditions: [NPredicate] = []

    def __init__(self, node: pddlParser.PreconditionsContext):

        nodes: [pddlParser.NPreconditionContext] = []
        if isinstance(node.getChild(0), pddlParser.AndPreconditionContext):
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        else:
            nodes.append(node.getChild(0))

        for node in nodes:
            if isinstance(node, pddlParser.BooleanLiteralContext):
                self.conditions.append(NLiteral(node))
            elif isinstance(node, pddlParser.ComparationContext):
                self.conditions.append(NBinaryPredicate(node))
