from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p


class Atom:

    def __init__(self, node: p.AtomContext):
        self.name = node.getChild(0).getText()
        self.attributes = []
        node: p.GroundAtomParameterContext or p.LiftedAtomParameterContext
        for attr in node.children[1:]:
            self.attributes.append(attr.getText())

    def __str__(self):
        return f"{self.name} {' '.join([a for a in self.attributes])}"

    def __repr__(self):
        return str(self)

    def toFunctionName(self):
        return f"{self.name}({''.join([a for a in self.attributes])})"

    def toAlphaFunctionName(self):
        return f"\\alpha_{{{self.name}}}({''.join([a for a in self.attributes])})"
