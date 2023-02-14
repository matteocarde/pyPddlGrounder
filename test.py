from pyGrounder.myClasses.Domain import Domain
from pyGrounder.myClasses.Problem import Problem

problem_path = r"C:/Users/Desktop/test/files/problem.pddl"
domain_path = r"C:/Users/Desktop/test/files/domain.pddl"
result_folder = r"C:/Users/Desktop/test/results"

objDomain = Domain(domain_path)
objProblem = Problem(problem_path)
objDomainGrounded = objDomain.ground(objProblem)

objDomain.writeJson(result_folder,"domain")
objProblem.writeJson(result_folder,"problem")
objDomainGrounded.writeJson(result_folder,"domain_grounded")

objDomainGrounded.writePddl(result_folder,"domain_grounded")