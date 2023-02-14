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
* ```Domain(domain_path)``` Creates an instance of the Domain object from the file [domain.pddl](files/domain.pddl)
* ```Problem(problem_path)``` Creates an instance of the Problem object from the file [problem.pddl](files/problem.pddl)
* ```objDomain.ground(objProblem)``` Returns the grounded Domain object 
* ```.writeJson(result_folder,"filename")``` Writes the object in json format in the [result_folder](results)
* ```objDomainGrounded.writePddl(result_folder,"filename")``` Writes the [pddl file](results/domain_grounded.pddl) of the Domain object
