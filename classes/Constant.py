from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Predicate import Predicate


class Constant(Predicate):
    value: float
    isDelta: bool

    def __init__(self, node: pddlParser.ConstantContext or pddlParser.NumberContext):
        super().__init__()
        self.isDelta = False
        if isinstance(node, pddlParser.NumberContext):
            self.value = float(node.getText())
            return

        child = node.getChild(0)
        if isinstance(child, pddlParser.NumberContext):
            self.value = float(child.getText())
        elif isinstance(child, pddlParser.DeltaContext):
            self.isDelta = True

    def __str__(self):
        return "#t" if self.isDelta else str(self.value)

    def __repr__(self):
        return str(self)
