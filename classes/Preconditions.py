from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Conditions import Conditions


class Preconditions(Conditions):

    def __init__(self, node: pddlParser.PreconditionsContext):
        super().__init__(node)
