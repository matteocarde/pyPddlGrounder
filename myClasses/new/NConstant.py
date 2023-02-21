from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.myClasses.new.NPredicate import NPredicate


class NConstant(NPredicate):

    value: float
    isDelta: bool

    def __init__(self, node: pddlParser.ConstantContext):
        super().__init__()
        child = node.getChild(0)
        self.isDelta = False
        if isinstance(child, pddlParser.NumberContext):
            self.value = float(child.getText())
        elif isinstance(child, pddlParser.DeltaContext):
            self.isDelta = True

    def __str__(self):
        return "#t" if self.isDelta else str(self.value)

    def __repr__(self):
        return str(self)

