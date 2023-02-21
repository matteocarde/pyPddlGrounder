# Generated from pddl.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pddlParser import pddlParser
else:
    from pddlParser import pddlParser

# This class defines a complete listener for a parse tree produced by pddlParser.
class pddlListener(ParseTreeListener):

    # Enter a parse tree produced by pddlParser#pddlDoc.
    def enterPddlDoc(self, ctx:pddlParser.PddlDocContext):
        pass

    # Exit a parse tree produced by pddlParser#pddlDoc.
    def exitPddlDoc(self, ctx:pddlParser.PddlDocContext):
        pass


    # Enter a parse tree produced by pddlParser#domain.
    def enterDomain(self, ctx:pddlParser.DomainContext):
        pass

    # Exit a parse tree produced by pddlParser#domain.
    def exitDomain(self, ctx:pddlParser.DomainContext):
        pass


    # Enter a parse tree produced by pddlParser#domainName.
    def enterDomainName(self, ctx:pddlParser.DomainNameContext):
        pass

    # Exit a parse tree produced by pddlParser#domainName.
    def exitDomainName(self, ctx:pddlParser.DomainNameContext):
        pass


    # Enter a parse tree produced by pddlParser#requireDef.
    def enterRequireDef(self, ctx:pddlParser.RequireDefContext):
        pass

    # Exit a parse tree produced by pddlParser#requireDef.
    def exitRequireDef(self, ctx:pddlParser.RequireDefContext):
        pass


    # Enter a parse tree produced by pddlParser#typesDef.
    def enterTypesDef(self, ctx:pddlParser.TypesDefContext):
        pass

    # Exit a parse tree produced by pddlParser#typesDef.
    def exitTypesDef(self, ctx:pddlParser.TypesDefContext):
        pass


    # Enter a parse tree produced by pddlParser#predicatesDef.
    def enterPredicatesDef(self, ctx:pddlParser.PredicatesDefContext):
        pass

    # Exit a parse tree produced by pddlParser#predicatesDef.
    def exitPredicatesDef(self, ctx:pddlParser.PredicatesDefContext):
        pass


    # Enter a parse tree produced by pddlParser#predicate.
    def enterPredicate(self, ctx:pddlParser.PredicateContext):
        pass

    # Exit a parse tree produced by pddlParser#predicate.
    def exitPredicate(self, ctx:pddlParser.PredicateContext):
        pass


    # Enter a parse tree produced by pddlParser#atomicFormulaSkeleton.
    def enterAtomicFormulaSkeleton(self, ctx:pddlParser.AtomicFormulaSkeletonContext):
        pass

    # Exit a parse tree produced by pddlParser#atomicFormulaSkeleton.
    def exitAtomicFormulaSkeleton(self, ctx:pddlParser.AtomicFormulaSkeletonContext):
        pass


    # Enter a parse tree produced by pddlParser#typedVariable.
    def enterTypedVariable(self, ctx:pddlParser.TypedVariableContext):
        pass

    # Exit a parse tree produced by pddlParser#typedVariable.
    def exitTypedVariable(self, ctx:pddlParser.TypedVariableContext):
        pass


    # Enter a parse tree produced by pddlParser#functionsDef.
    def enterFunctionsDef(self, ctx:pddlParser.FunctionsDefContext):
        pass

    # Exit a parse tree produced by pddlParser#functionsDef.
    def exitFunctionsDef(self, ctx:pddlParser.FunctionsDefContext):
        pass


    # Enter a parse tree produced by pddlParser#function.
    def enterFunction(self, ctx:pddlParser.FunctionContext):
        pass

    # Exit a parse tree produced by pddlParser#function.
    def exitFunction(self, ctx:pddlParser.FunctionContext):
        pass


    # Enter a parse tree produced by pddlParser#predicatedVariables.
    def enterPredicatedVariables(self, ctx:pddlParser.PredicatedVariablesContext):
        pass

    # Exit a parse tree produced by pddlParser#predicatedVariables.
    def exitPredicatedVariables(self, ctx:pddlParser.PredicatedVariablesContext):
        pass


    # Enter a parse tree produced by pddlParser#structureDef.
    def enterStructureDef(self, ctx:pddlParser.StructureDefContext):
        pass

    # Exit a parse tree produced by pddlParser#structureDef.
    def exitStructureDef(self, ctx:pddlParser.StructureDefContext):
        pass


    # Enter a parse tree produced by pddlParser#actionDef.
    def enterActionDef(self, ctx:pddlParser.ActionDefContext):
        pass

    # Exit a parse tree produced by pddlParser#actionDef.
    def exitActionDef(self, ctx:pddlParser.ActionDefContext):
        pass


    # Enter a parse tree produced by pddlParser#precondition.
    def enterPrecondition(self, ctx:pddlParser.PreconditionContext):
        pass

    # Exit a parse tree produced by pddlParser#precondition.
    def exitPrecondition(self, ctx:pddlParser.PreconditionContext):
        pass


    # Enter a parse tree produced by pddlParser#precondition_formula.
    def enterPrecondition_formula(self, ctx:pddlParser.Precondition_formulaContext):
        pass

    # Exit a parse tree produced by pddlParser#precondition_formula.
    def exitPrecondition_formula(self, ctx:pddlParser.Precondition_formulaContext):
        pass


    # Enter a parse tree produced by pddlParser#effect.
    def enterEffect(self, ctx:pddlParser.EffectContext):
        pass

    # Exit a parse tree produced by pddlParser#effect.
    def exitEffect(self, ctx:pddlParser.EffectContext):
        pass


    # Enter a parse tree produced by pddlParser#effect_formula.
    def enterEffect_formula(self, ctx:pddlParser.Effect_formulaContext):
        pass

    # Exit a parse tree produced by pddlParser#effect_formula.
    def exitEffect_formula(self, ctx:pddlParser.Effect_formulaContext):
        pass


    # Enter a parse tree produced by pddlParser#operation.
    def enterOperation(self, ctx:pddlParser.OperationContext):
        pass

    # Exit a parse tree produced by pddlParser#operation.
    def exitOperation(self, ctx:pddlParser.OperationContext):
        pass


    # Enter a parse tree produced by pddlParser#processDef.
    def enterProcessDef(self, ctx:pddlParser.ProcessDefContext):
        pass

    # Exit a parse tree produced by pddlParser#processDef.
    def exitProcessDef(self, ctx:pddlParser.ProcessDefContext):
        pass


    # Enter a parse tree produced by pddlParser#eventDef.
    def enterEventDef(self, ctx:pddlParser.EventDefContext):
        pass

    # Exit a parse tree produced by pddlParser#eventDef.
    def exitEventDef(self, ctx:pddlParser.EventDefContext):
        pass


    # Enter a parse tree produced by pddlParser#problem.
    def enterProblem(self, ctx:pddlParser.ProblemContext):
        pass

    # Exit a parse tree produced by pddlParser#problem.
    def exitProblem(self, ctx:pddlParser.ProblemContext):
        pass


    # Enter a parse tree produced by pddlParser#problemDecl.
    def enterProblemDecl(self, ctx:pddlParser.ProblemDeclContext):
        pass

    # Exit a parse tree produced by pddlParser#problemDecl.
    def exitProblemDecl(self, ctx:pddlParser.ProblemDeclContext):
        pass


    # Enter a parse tree produced by pddlParser#problemDomain.
    def enterProblemDomain(self, ctx:pddlParser.ProblemDomainContext):
        pass

    # Exit a parse tree produced by pddlParser#problemDomain.
    def exitProblemDomain(self, ctx:pddlParser.ProblemDomainContext):
        pass


    # Enter a parse tree produced by pddlParser#objectDecl.
    def enterObjectDecl(self, ctx:pddlParser.ObjectDeclContext):
        pass

    # Exit a parse tree produced by pddlParser#objectDecl.
    def exitObjectDecl(self, ctx:pddlParser.ObjectDeclContext):
        pass


    # Enter a parse tree produced by pddlParser#sameTypeNamesList.
    def enterSameTypeNamesList(self, ctx:pddlParser.SameTypeNamesListContext):
        pass

    # Exit a parse tree produced by pddlParser#sameTypeNamesList.
    def exitSameTypeNamesList(self, ctx:pddlParser.SameTypeNamesListContext):
        pass


    # Enter a parse tree produced by pddlParser#init.
    def enterInit(self, ctx:pddlParser.InitContext):
        pass

    # Exit a parse tree produced by pddlParser#init.
    def exitInit(self, ctx:pddlParser.InitContext):
        pass


    # Enter a parse tree produced by pddlParser#atomicNameFormula.
    def enterAtomicNameFormula(self, ctx:pddlParser.AtomicNameFormulaContext):
        pass

    # Exit a parse tree produced by pddlParser#atomicNameFormula.
    def exitAtomicNameFormula(self, ctx:pddlParser.AtomicNameFormulaContext):
        pass


    # Enter a parse tree produced by pddlParser#equalLiteral.
    def enterEqualLiteral(self, ctx:pddlParser.EqualLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#equalLiteral.
    def exitEqualLiteral(self, ctx:pddlParser.EqualLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#initEl.
    def enterInitEl(self, ctx:pddlParser.InitElContext):
        pass

    # Exit a parse tree produced by pddlParser#initEl.
    def exitInitEl(self, ctx:pddlParser.InitElContext):
        pass


    # Enter a parse tree produced by pddlParser#nameLiteral.
    def enterNameLiteral(self, ctx:pddlParser.NameLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#nameLiteral.
    def exitNameLiteral(self, ctx:pddlParser.NameLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#atomName.
    def enterAtomName(self, ctx:pddlParser.AtomNameContext):
        pass

    # Exit a parse tree produced by pddlParser#atomName.
    def exitAtomName(self, ctx:pddlParser.AtomNameContext):
        pass


    # Enter a parse tree produced by pddlParser#groundAtomParameter.
    def enterGroundAtomParameter(self, ctx:pddlParser.GroundAtomParameterContext):
        pass

    # Exit a parse tree produced by pddlParser#groundAtomParameter.
    def exitGroundAtomParameter(self, ctx:pddlParser.GroundAtomParameterContext):
        pass


    # Enter a parse tree produced by pddlParser#liftedAtomParameter.
    def enterLiftedAtomParameter(self, ctx:pddlParser.LiftedAtomParameterContext):
        pass

    # Exit a parse tree produced by pddlParser#liftedAtomParameter.
    def exitLiftedAtomParameter(self, ctx:pddlParser.LiftedAtomParameterContext):
        pass


    # Enter a parse tree produced by pddlParser#atom.
    def enterAtom(self, ctx:pddlParser.AtomContext):
        pass

    # Exit a parse tree produced by pddlParser#atom.
    def exitAtom(self, ctx:pddlParser.AtomContext):
        pass


    # Enter a parse tree produced by pddlParser#positiveLiteral.
    def enterPositiveLiteral(self, ctx:pddlParser.PositiveLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#positiveLiteral.
    def exitPositiveLiteral(self, ctx:pddlParser.PositiveLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#negativeLiteral.
    def enterNegativeLiteral(self, ctx:pddlParser.NegativeLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#negativeLiteral.
    def exitNegativeLiteral(self, ctx:pddlParser.NegativeLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:pddlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:pddlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#modificator.
    def enterModificator(self, ctx:pddlParser.ModificatorContext):
        pass

    # Exit a parse tree produced by pddlParser#modificator.
    def exitModificator(self, ctx:pddlParser.ModificatorContext):
        pass


    # Enter a parse tree produced by pddlParser#operator.
    def enterOperator(self, ctx:pddlParser.OperatorContext):
        pass

    # Exit a parse tree produced by pddlParser#operator.
    def exitOperator(self, ctx:pddlParser.OperatorContext):
        pass


    # Enter a parse tree produced by pddlParser#comparator.
    def enterComparator(self, ctx:pddlParser.ComparatorContext):
        pass

    # Exit a parse tree produced by pddlParser#comparator.
    def exitComparator(self, ctx:pddlParser.ComparatorContext):
        pass


    # Enter a parse tree produced by pddlParser#number.
    def enterNumber(self, ctx:pddlParser.NumberContext):
        pass

    # Exit a parse tree produced by pddlParser#number.
    def exitNumber(self, ctx:pddlParser.NumberContext):
        pass


    # Enter a parse tree produced by pddlParser#delta.
    def enterDelta(self, ctx:pddlParser.DeltaContext):
        pass

    # Exit a parse tree produced by pddlParser#delta.
    def exitDelta(self, ctx:pddlParser.DeltaContext):
        pass


    # Enter a parse tree produced by pddlParser#constant.
    def enterConstant(self, ctx:pddlParser.ConstantContext):
        pass

    # Exit a parse tree produced by pddlParser#constant.
    def exitConstant(self, ctx:pddlParser.ConstantContext):
        pass


    # Enter a parse tree produced by pddlParser#operationSide.
    def enterOperationSide(self, ctx:pddlParser.OperationSideContext):
        pass

    # Exit a parse tree produced by pddlParser#operationSide.
    def exitOperationSide(self, ctx:pddlParser.OperationSideContext):
        pass


    # Enter a parse tree produced by pddlParser#nOperation.
    def enterNOperation(self, ctx:pddlParser.NOperationContext):
        pass

    # Exit a parse tree produced by pddlParser#nOperation.
    def exitNOperation(self, ctx:pddlParser.NOperationContext):
        pass


    # Enter a parse tree produced by pddlParser#comparation.
    def enterComparation(self, ctx:pddlParser.ComparationContext):
        pass

    # Exit a parse tree produced by pddlParser#comparation.
    def exitComparation(self, ctx:pddlParser.ComparationContext):
        pass


    # Enter a parse tree produced by pddlParser#modification.
    def enterModification(self, ctx:pddlParser.ModificationContext):
        pass

    # Exit a parse tree produced by pddlParser#modification.
    def exitModification(self, ctx:pddlParser.ModificationContext):
        pass


    # Enter a parse tree produced by pddlParser#nPrecondition.
    def enterNPrecondition(self, ctx:pddlParser.NPreconditionContext):
        pass

    # Exit a parse tree produced by pddlParser#nPrecondition.
    def exitNPrecondition(self, ctx:pddlParser.NPreconditionContext):
        pass


    # Enter a parse tree produced by pddlParser#nEffect.
    def enterNEffect(self, ctx:pddlParser.NEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#nEffect.
    def exitNEffect(self, ctx:pddlParser.NEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#andPrecondition.
    def enterAndPrecondition(self, ctx:pddlParser.AndPreconditionContext):
        pass

    # Exit a parse tree produced by pddlParser#andPrecondition.
    def exitAndPrecondition(self, ctx:pddlParser.AndPreconditionContext):
        pass


    # Enter a parse tree produced by pddlParser#andEffect.
    def enterAndEffect(self, ctx:pddlParser.AndEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#andEffect.
    def exitAndEffect(self, ctx:pddlParser.AndEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#preconditions.
    def enterPreconditions(self, ctx:pddlParser.PreconditionsContext):
        pass

    # Exit a parse tree produced by pddlParser#preconditions.
    def exitPreconditions(self, ctx:pddlParser.PreconditionsContext):
        pass


    # Enter a parse tree produced by pddlParser#effects.
    def enterEffects(self, ctx:pddlParser.EffectsContext):
        pass

    # Exit a parse tree produced by pddlParser#effects.
    def exitEffects(self, ctx:pddlParser.EffectsContext):
        pass


    # Enter a parse tree produced by pddlParser#goal.
    def enterGoal(self, ctx:pddlParser.GoalContext):
        pass

    # Exit a parse tree produced by pddlParser#goal.
    def exitGoal(self, ctx:pddlParser.GoalContext):
        pass


    # Enter a parse tree produced by pddlParser#metric.
    def enterMetric(self, ctx:pddlParser.MetricContext):
        pass

    # Exit a parse tree produced by pddlParser#metric.
    def exitMetric(self, ctx:pddlParser.MetricContext):
        pass



del pddlParser