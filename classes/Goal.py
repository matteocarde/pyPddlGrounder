from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Preconditions import Preconditions


class Goal(Preconditions):

    def __init__(self, node: pddlParser.GoalContext):
        super().__init__(node.getChild(2))