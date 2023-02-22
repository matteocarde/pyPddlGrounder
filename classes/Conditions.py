from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes import Predicate
from libs.pyGrounder.classes.BinaryPredicate import BinaryPredicate
from libs.pyGrounder.classes.Literal import Literal


class Conditions:
    conditions: [Predicate]

    def __init__(self, node: p.PreconditionsContext or p.EffectContext):
        self.conditions = []
        nodes: [p.PreconditionContext] = []
        if isinstance(node.getChild(0), p.AndPreconditionContext) or isinstance(node.getChild(0), p.AndEffectContext):
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        else:
            nodes.append(node.getChild(0))

        for node in nodes:
            if isinstance(node, p.BooleanLiteralContext):
                self.conditions.append(Literal(node.getChild(0)))
            else:
                self.conditions.append(BinaryPredicate(node))
