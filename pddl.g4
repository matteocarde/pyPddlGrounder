grammar pddl;



/************* LEXER ****************************/

LP : '(';
RP : ')';
QUOTE : '"';
COMMA : ',';
DEFINE : 'define';
PROBLEM : 'problem';
DOMAIN : 'domain';
REQUIREMENTS : ':requirements';
TYPES : ':types';
PREDICATES : ':predicates';
FUNCTIONS : ':functions';
ACTION : ':action';
PARAMETERS : ':parameters';
PRECONDITION : ':precondition';
EFFECT : ':effect';
PROCESS : ':process';
EVENT : ':event';
INCREASE : 'increase';
DECREASE : 'decrease';

DELTA: '#t';
NAME:    LETTER ANY_CHAR* ;
fragment LETTER : 'a'..'z' | 'A'..'Z';
fragment ANY_CHAR : LETTER | '0'..'9' | '-' | '_';
VARIABLE : '?' NAME ;
fragment DIGIT: '0'..'9';
NUMBER : ('-')? DIGIT+ ('.' DIGIT+)? | DELTA ;
WS : [ \t\r\n]+ -> skip ;

REQUIRE_KEY
    : ':typing'
    | ':duration-inequalities'
    | ':time'
    | ':fluents'
    | ':adl'
    | ':durative-actions'
    ;

OPERATION : '>'| '>='| '<'| '<='| '='| '+'| '-'| '*'| '/'| 'and'| 'or';

	/************* Start of grammar *******************/

pddlDoc : domain | problem;

/************* DOMAINS ****************************/

domain
    : '(' 'define' domainName 
	requireDef?
    typesDef?
	predicatesDef?
    functionsDef?
	structureDef*
	RP
    ;

domainName
    : LP DOMAIN NAME RP
    ;

requireDef
	: LP REQUIREMENTS REQUIRE_KEY+ RP
	;

typesDef
	: LP TYPES (NAME('-' NAME)?)+ RP
	;

predicatesDef
	: LP PREDICATES predicate+ RP
	;

predicate
	: LP NAME typedVariable* RP
	;


/* name stringa - stringa */
atomicFormulaSkeleton
	: LP NAME typedVariable+ RP
	;

typedVariable
	: VARIABLE '-' NAME
	;

functionsDef
	: LP FUNCTIONS function+ RP
	;

function
	: LP NAME typedVariable* RP
	;

predicatedVariables
	: NAME VARIABLE*  
	;

structureDef
	: actionDef
	| processDef
	| eventDef
	;


/************* ACTIONS ****************************/

actionDef
	: LP ACTION NAME
	    PARAMETERS LP typedVariable* RP
        precondition?
		effect?
		RP
;

precondition
	: PRECONDITION LP 'and' precondition_formula* RP
	;

precondition_formula
    : LP predicatedVariables RP
    | operation
    ;

effect
	: EFFECT LP 'and' effect_formula+ RP
	;

effect_formula
    : LP predicatedVariables RP
	| LP 'not' LP predicatedVariables RP RP
	| LP 'assign' LP predicatedVariables RP NUMBER RP
	| LP 'increase' LP predicatedVariables RP NUMBER RP
	| LP 'decrease' LP predicatedVariables RP NUMBER RP
	| LP 'assign' LP predicatedVariables RP operation RP
	| LP 'increase' LP predicatedVariables RP operation RP
	| LP 'decrease' LP predicatedVariables RP operation RP
	| LP 'assign' LP predicatedVariables RP LP predicatedVariables RP RP
	;

operation
	: LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') LP predicatedVariables RP NUMBER RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') NUMBER LP predicatedVariables RP RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') NUMBER NUMBER RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') LP predicatedVariables RP LP predicatedVariables RP RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') LP predicatedVariables RP operation RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/')  operation LP predicatedVariables RP RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') NUMBER operation RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') operation operation RP
	| LP (OPERATION|'-'|'='|'<'|'=<'|'>='|'>'|'+'|'*'|'/') operation NUMBER RP
	| LP 'not' operation RP
	| LP 'not' LP predicatedVariables RP RP
	| NUMBER
	;

/************* PROCESSES ****************************/

processDef
	: LP PROCESS NAME
		PARAMETERS LP typedVariable* RP
		precondition?
		effect?
		RP
	;





/************* EVENTS ****************************/

eventDef
	: LP EVENT NAME
	    PARAMETERS LP typedVariable* RP
        precondition?
		effect?
		RP
;

/************* PROBLEMS ****************************/

problem
	: '(' 'define' problemDecl
	problemDomain
	objectDecl?
	init
	goal
	metric?
	RP
	;

problemDecl
	: LP PROBLEM NAME RP
	;

problemDomain
	: LP ':domain' NAME RP
	;

objectDecl
	: LP ':objects' sameTypeNamesList+ RP
	;

sameTypeNamesList
	:NAME+ '-' NAME
	;

init : LP ':init' initEl* RP;
atomicNameFormula
	:LP NAME+ RP
	;
equalLiteral
	:LP '=' atomicNameFormula NUMBER RP
	;
initEl : nameLiteral | equalLiteral;

nameLiteral : atomicNameFormula | LP 'not' atomicNameFormula RP;

//groundAtom: name a b c d
//liftedAtom: name ?a ?b ?c ?d

atomName: NAME;
groundAtomParameter: NAME;
liftedAtomParameter: '?' NAME;
atom: atomName (groundAtomParameter+ | liftedAtomParameter+);

//positiveLiteral: (name a b c d)
positiveLiteral: LP atom RP;
//negativeLiteral: (not (name a b c d))
negativeLiteral: LP 'not' positiveLiteral RP;
booleanLiteral: positiveLiteral | negativeLiteral;

modificator: 'assign'|'increase'|'decrease';
operator: '+'|'-'|'*'|'/';
comparator: '>'|'>='|'<='|'<'|'=';
number: NUMBER;
delta: DELTA;
constant: number | delta;

operationSide: nOperation | positiveLiteral | constant;
nOperation: LP operator operationSide operationSide RP;

comparation: LP comparator positiveLiteral operationSide RP;
modification: LP modificator positiveLiteral operationSide RP;

nPrecondition: booleanLiteral | comparation;
nEffect:  booleanLiteral | modification;

andPrecondition: LP 'and' nPrecondition+ RP;
andEffect : LP 'and' nEffect+ RP;
preconditions: nPrecondition | andPrecondition;
effects: nEffect | andEffect;

goal : LP ':goal' preconditions RP;

metric : LP ':metric' ('maximize'|'minimize') atomicNameFormula RP;