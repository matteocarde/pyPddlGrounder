import json
from libs.pyGrounder.myClasses.myUtilities import remove_comments
from libs.pyGrounder.myClasses.myUtilities import get_antlr4_parsetree


class Problem:
    __name = ""
    __domain = ""
    __objects = []
    __init = []
    __goal = []

    def __init__(self, file_path):

        file = remove_comments(file_path)
        tree = get_antlr4_parsetree(file).problem()

        for i in range(tree.getChildCount()):
            child = tree.getChild(i)
            text = child.getText()
            if 'problem' in text:
                self.__name = Problem.__getProblemName(text)
            if ':domain' in text:
                self.__domain = Problem.__getDomainName(text)
            elif ':objects' in text:
                self.__objects = Problem.__getObjectsList(child)
            elif ':init' in text:
                self.__init = Problem.__getInitList(child)
            elif ':goal' in text:
                self.__goal = Problem.__getGoalList(child)

    @staticmethod
    def __getProblemName(problem):
        return problem.replace("(problem", "").replace(")", "").strip()

    @staticmethod
    def __getDomainName(domain):
        return domain.replace("(:domain", "").replace(")", "").strip()

    @staticmethod
    def __getObjectsList(node):
        result = []
        for child in range(2, node.getChildCount() - 1):
            result.append(Problem.__getObjects(node.getChild(child)))
        return result

    @staticmethod
    def __getObjects(node):
        result = {}
        objectList = []
        result["objectType"] = node.getChild(-1).getText()
        for child in range(node.getChildCount() - 2):  # -2 perchè il penultimo è "-" e -1 è il tipo
            objectList.append(node.getChild(child).getText())
        result["objectInstances"] = objectList
        return result

    @staticmethod
    def __getInitList(node):
        result = []
        for child in range(2, node.getChildCount() - 1):
            if "=" in node.getChild(child).getText():
                result.append(Problem.__getAssignmentPredicate(node.getChild(child)))
            else:
                result.append(Problem.__getSimplePredicate(node.getChild(child)))
        return result

    @staticmethod
    def __getSimplePredicate(node):
        result = {}
        if node.getChildCount() == 1:
            result = Problem.__getSimplePredicate(node.getChild(0))
        else:
            result["string"] = node.getText()
            result["isAssignment?"] = False
            result["predName"] = node.getChild(1).getText()
            result["predObjects"] = []
            for child in range(2, node.getChildCount() - 1):
                result["predObjects"].append(node.getChild(child).getText())
            return result
        return result

    @staticmethod
    def __getAssignmentPredicate(node):
        result = {}
        if node.getChildCount() == 1:
            return Problem.__getAssignmentPredicate(node.getChild(0))

        result["string"] = node.getText()
        result["isAssignment?"] = True
        result["operands"] = []
        result["operands"].append(Problem.__getOperand(node.getChild(2)))
        result["operands"].append(Problem.__getConstant(node.getChild(3)))

        return result

    @staticmethod
    def __getOperand(node):
        result = dict()
        result["operandName"] = node.getChild(1).getText()
        result["operandObjects"] = []
        for child in range(2, node.getChildCount() - 1):
            result["operandObjects"].append(node.getChild(child).getText())
        return result

    @staticmethod
    def __getConstant(node):
        result = dict()
        result["operandName"] = "Constant"
        result["operandValue"] = node.getText()
        return result

    @staticmethod
    def __getGoalPredicate(node):
        result = dict()
        if node.getChildCount() == 1:
            return Problem.__getSimplePredicate(node.getChild(0))

        result["string"] = node.getText()
        result["predName"] = node.getChild(1).getText()
        result["predObjects"] = []
        for child in range(2, node.getChildCount() - 1):
            result["predObjects"].append(node.getChild(child).getText())
        return result

    @staticmethod
    def __getGoalList(node):
        node = node.getChild(2)
        result = []
        for child in range(2, node.getChildCount() - 1):
            result.append(Problem.__getGoalPredicate(node.getChild(child)))
        return result

    @property
    def name(self):
        return self.__name

    @property
    def domain(self):
        return self.__domain

    @property
    def objects(self):
        return self.__objects

    @property
    def init(self):
        return self.__init

    @property
    def goal(self):
        return self.__goal

    def toJson(self):
        json_data = dict()
        json_data['problem'] = self.__name
        json_data['domain'] = self.__domain
        json_data['objects'] = self.__objects
        json_data['init'] = self.__init
        json_data['goal'] = self.__goal
        return json_data

    def writeJson(self, file_path: str, filename: str):
        with open(file_path + "/" + filename + ".json", 'w') as json_file:
            json.dump(self.toJson(), json_file, indent=4)

    def printALL(self):
        print("----------------------------Problem name: ------------------------------------------------")
        print(self.__name + "\n")
        print("----------------------------Domain name: -------------------------------------------------")
        print(self.__domain + "\n")
        print("----------------------------Objects: -----------------------------------------------------")
        for object in self.__objects:
            print(object["objectType"] + " - " + str(object["objectInstances"]))
            # print(object)
        print("----------------------------init: --------------------------------------------------------")
        for init in self.__init:
            print(init["string"])
        print("----------------------------goal: --------------------------------------------------------")
        for goal in self.__goal:
            print(goal["string"])
