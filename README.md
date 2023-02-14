# PyGrounder
PyGrounder is a library that provides classes and methods for modeling problems defined in **Planning Domain Definition Language (PDDL+)** 
and in particular it allows to ground the domain on a defined problem.

The grounding process is performed by replacing the variables in the domain with the instances of objects present in a given associated problem.

## Requirements
* Python version: 3.7 or higher
* [Antlr4](https://www.antlr.org/) 
* [Antlr4 Python3 runtime target](https://www.antlr.org/download.html)

## Installation

## Overview
The [example.py](example.py) contains an example of use where:
* ```Domain(domain_path)``` Creates an instance of the [Domain object](pyGrounder/blob/main/README.md#domain) from the file [domain.pddl](files/domain.pddl)
* ```Problem(problem_path)``` Creates an instance of the Problem object from the file [problem.pddl](files/problem.pddl)
* ```objDomain.ground(objProblem)``` Returns the grounded Domain object 
* ```.writeJson(result_folder,"filename")``` Writes the object in json format in the [result_folder](results)
* ```objDomainGrounded.writePddl(result_folder,"filename")``` Writes the [pddl file](results/domain_grounded.pddl) of the Domain object

## Documentation
### Domain
It represents the pddl file of the domain.

#### Attributes
* ```name : str``` The string representing the name of the domain
* ```requirements : list[str]``` The list representing the requirements of the domain
* ```types : list[str] ``` The list representing the types of the domain
* ```predicates : list[Predicate]``` The list representing the predicates of the domain 
* ```functions : list[Function]``` The list representing the functions of the domain
* ```actions : list[Action]``` The list representing the actions of the domain
* ```events : list[Event]``` The list representing the events of the domain
* ```processes : list[Process]``` The list representing the processes of the domain
* ```constants :list[Variable]``` The list representing the constants of the domain

#### Methods
* ```.writeJson(file_path:str,filename:str)``` <br>
  It writes the Json representation of the Domain, naming it as filename, in the folder result at the file_path. [Example](results/domain.json)
* ```.toJson()```<br>
  It returns the dictionary containing the json representation of the domain
* ```.printAll()```<br>
  It prints in console each attributes of the domain and their values
* ```.ground(problem: Problem)```<br>
  It makes the grounding of the domain on the problem given as input. The method returns a Domain object. [Example of grounded domain](results/domain_grounded.pddl)
* ```.writePddl(file_path:str,filename:str)```<br>
  It writes the PDDL file of the Domain, naming it as filename, in the folder result at the file_path
