from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.myClasses.new.NPreconditions import NPreconditions


class Goal(NPreconditions):

    def __init__(self, node: pddlParser.GoalContext):
        super().__init__(node.getChild(2))