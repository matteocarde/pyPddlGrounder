from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.myClasses.new.NAtom import NAtom
from libs.pyGrounder.myClasses.new.NPredicate import NPredicate
from pyspel.pyspel import Predicate


class NLiteral(NPredicate):

    def __init__(self, node: p.PositiveLiteralContext or p.NegativeLiteralContext):
        super().__init__()
        self.sign = "+" if isinstance(node, p.PositiveLiteralContext) else "-"
        positiveLiteralNode = node.getChild(2) if self.sign == "-" else node
        atomNode = positiveLiteralNode.getChild(1)

        self.atom = NAtom(atomNode)

    def __str__(self):
        if self.sign == "+":
            return f"({self.atom})"
        else:
            return f"(not ({self.atom}))"

    def __repr__(self):
        return str(self)



