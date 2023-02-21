class SimplePredicate:
    __string = ""
    __name = ""
    __arguments = []
    __isComplex = False
    __isNegated = False
    var: str

    def __init__(self, string=None, name=None, arguments=None):
        if string is not None:
            self.__string = "(" + string + ")"

            name = string.split(" ")
            self.__name = name[0]
            self.__arguments = name[1:]
        else:
            self.__name = name
            self.__arguments = arguments
            string = name
            for argument in self.__arguments:
                string = string + " " + argument
            self.__string = "(" + string + ")"

        self.var = f"{self.__name}({','.join(self.__arguments)})"

    def __str__(self):
        return self.__string

    def __repr__(self):
        return str(self)

    def ground(self, combination):
        groundedArguments = []
        for argument in self.arguments:
            for instance in combination:
                if argument in instance:
                    groundedArguments.append(instance.split("-")[0])
        return SimplePredicate(name=self.name, arguments=groundedArguments)

    @property
    def isComplex(self):
        return self.__isComplex

    @property
    def isNegated(self):
        return self.__isNegated

    @property
    def string(self):
        return self.__string

    @property
    def arguments(self):
        return self.__arguments

    @property
    def name(self):
        return self.__name

    def toString(self):
        '''
        It returns the string of the predicate into brackets.  For example: "(atRobot ?r ?b)
        '''
        return self.__string
