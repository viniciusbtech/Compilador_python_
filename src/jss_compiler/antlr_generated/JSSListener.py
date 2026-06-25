# Generated from JSS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JSSParser import JSSParser
else:
    from JSSParser import JSSParser

# This class defines a complete listener for a parse tree produced by JSSParser.
class JSSListener(ParseTreeListener):

    # Enter a parse tree produced by JSSParser#program.
    def enterProgram(self, ctx:JSSParser.ProgramContext):
        pass

    # Exit a parse tree produced by JSSParser#program.
    def exitProgram(self, ctx:JSSParser.ProgramContext):
        pass


    # Enter a parse tree produced by JSSParser#declaration.
    def enterDeclaration(self, ctx:JSSParser.DeclarationContext):
        pass

    # Exit a parse tree produced by JSSParser#declaration.
    def exitDeclaration(self, ctx:JSSParser.DeclarationContext):
        pass


    # Enter a parse tree produced by JSSParser#varDecl.
    def enterVarDecl(self, ctx:JSSParser.VarDeclContext):
        pass

    # Exit a parse tree produced by JSSParser#varDecl.
    def exitVarDecl(self, ctx:JSSParser.VarDeclContext):
        pass


    # Enter a parse tree produced by JSSParser#constDecl.
    def enterConstDecl(self, ctx:JSSParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by JSSParser#constDecl.
    def exitConstDecl(self, ctx:JSSParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by JSSParser#arrayTypeDim.
    def enterArrayTypeDim(self, ctx:JSSParser.ArrayTypeDimContext):
        pass

    # Exit a parse tree produced by JSSParser#arrayTypeDim.
    def exitArrayTypeDim(self, ctx:JSSParser.ArrayTypeDimContext):
        pass


    # Enter a parse tree produced by JSSParser#declarator.
    def enterDeclarator(self, ctx:JSSParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by JSSParser#declarator.
    def exitDeclarator(self, ctx:JSSParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by JSSParser#functionDecl.
    def enterFunctionDecl(self, ctx:JSSParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by JSSParser#functionDecl.
    def exitFunctionDecl(self, ctx:JSSParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by JSSParser#parameters.
    def enterParameters(self, ctx:JSSParser.ParametersContext):
        pass

    # Exit a parse tree produced by JSSParser#parameters.
    def exitParameters(self, ctx:JSSParser.ParametersContext):
        pass


    # Enter a parse tree produced by JSSParser#parameter.
    def enterParameter(self, ctx:JSSParser.ParameterContext):
        pass

    # Exit a parse tree produced by JSSParser#parameter.
    def exitParameter(self, ctx:JSSParser.ParameterContext):
        pass


    # Enter a parse tree produced by JSSParser#returnType.
    def enterReturnType(self, ctx:JSSParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by JSSParser#returnType.
    def exitReturnType(self, ctx:JSSParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by JSSParser#type_.
    def enterType_(self, ctx:JSSParser.Type_Context):
        pass

    # Exit a parse tree produced by JSSParser#type_.
    def exitType_(self, ctx:JSSParser.Type_Context):
        pass


    # Enter a parse tree produced by JSSParser#classDecl.
    def enterClassDecl(self, ctx:JSSParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by JSSParser#classDecl.
    def exitClassDecl(self, ctx:JSSParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by JSSParser#classMember.
    def enterClassMember(self, ctx:JSSParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by JSSParser#classMember.
    def exitClassMember(self, ctx:JSSParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by JSSParser#constructorDecl.
    def enterConstructorDecl(self, ctx:JSSParser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by JSSParser#constructorDecl.
    def exitConstructorDecl(self, ctx:JSSParser.ConstructorDeclContext):
        pass


    # Enter a parse tree produced by JSSParser#block.
    def enterBlock(self, ctx:JSSParser.BlockContext):
        pass

    # Exit a parse tree produced by JSSParser#block.
    def exitBlock(self, ctx:JSSParser.BlockContext):
        pass


    # Enter a parse tree produced by JSSParser#statement.
    def enterStatement(self, ctx:JSSParser.StatementContext):
        pass

    # Exit a parse tree produced by JSSParser#statement.
    def exitStatement(self, ctx:JSSParser.StatementContext):
        pass


    # Enter a parse tree produced by JSSParser#ifStmt.
    def enterIfStmt(self, ctx:JSSParser.IfStmtContext):
        pass

    # Exit a parse tree produced by JSSParser#ifStmt.
    def exitIfStmt(self, ctx:JSSParser.IfStmtContext):
        pass


    # Enter a parse tree produced by JSSParser#whileStmt.
    def enterWhileStmt(self, ctx:JSSParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by JSSParser#whileStmt.
    def exitWhileStmt(self, ctx:JSSParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by JSSParser#forStmt.
    def enterForStmt(self, ctx:JSSParser.ForStmtContext):
        pass

    # Exit a parse tree produced by JSSParser#forStmt.
    def exitForStmt(self, ctx:JSSParser.ForStmtContext):
        pass


    # Enter a parse tree produced by JSSParser#forInit.
    def enterForInit(self, ctx:JSSParser.ForInitContext):
        pass

    # Exit a parse tree produced by JSSParser#forInit.
    def exitForInit(self, ctx:JSSParser.ForInitContext):
        pass


    # Enter a parse tree produced by JSSParser#returnStmt.
    def enterReturnStmt(self, ctx:JSSParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by JSSParser#returnStmt.
    def exitReturnStmt(self, ctx:JSSParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by JSSParser#breakStmt.
    def enterBreakStmt(self, ctx:JSSParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by JSSParser#breakStmt.
    def exitBreakStmt(self, ctx:JSSParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by JSSParser#exprStmt.
    def enterExprStmt(self, ctx:JSSParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by JSSParser#exprStmt.
    def exitExprStmt(self, ctx:JSSParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by JSSParser#expr.
    def enterExpr(self, ctx:JSSParser.ExprContext):
        pass

    # Exit a parse tree produced by JSSParser#expr.
    def exitExpr(self, ctx:JSSParser.ExprContext):
        pass


    # Enter a parse tree produced by JSSParser#assignment.
    def enterAssignment(self, ctx:JSSParser.AssignmentContext):
        pass

    # Exit a parse tree produced by JSSParser#assignment.
    def exitAssignment(self, ctx:JSSParser.AssignmentContext):
        pass


    # Enter a parse tree produced by JSSParser#assignOp.
    def enterAssignOp(self, ctx:JSSParser.AssignOpContext):
        pass

    # Exit a parse tree produced by JSSParser#assignOp.
    def exitAssignOp(self, ctx:JSSParser.AssignOpContext):
        pass


    # Enter a parse tree produced by JSSParser#logicalOr.
    def enterLogicalOr(self, ctx:JSSParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by JSSParser#logicalOr.
    def exitLogicalOr(self, ctx:JSSParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by JSSParser#logicalAnd.
    def enterLogicalAnd(self, ctx:JSSParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by JSSParser#logicalAnd.
    def exitLogicalAnd(self, ctx:JSSParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by JSSParser#equalityRel.
    def enterEqualityRel(self, ctx:JSSParser.EqualityRelContext):
        pass

    # Exit a parse tree produced by JSSParser#equalityRel.
    def exitEqualityRel(self, ctx:JSSParser.EqualityRelContext):
        pass


    # Enter a parse tree produced by JSSParser#addition.
    def enterAddition(self, ctx:JSSParser.AdditionContext):
        pass

    # Exit a parse tree produced by JSSParser#addition.
    def exitAddition(self, ctx:JSSParser.AdditionContext):
        pass


    # Enter a parse tree produced by JSSParser#multiplication.
    def enterMultiplication(self, ctx:JSSParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by JSSParser#multiplication.
    def exitMultiplication(self, ctx:JSSParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by JSSParser#exponentiation.
    def enterExponentiation(self, ctx:JSSParser.ExponentiationContext):
        pass

    # Exit a parse tree produced by JSSParser#exponentiation.
    def exitExponentiation(self, ctx:JSSParser.ExponentiationContext):
        pass


    # Enter a parse tree produced by JSSParser#unary.
    def enterUnary(self, ctx:JSSParser.UnaryContext):
        pass

    # Exit a parse tree produced by JSSParser#unary.
    def exitUnary(self, ctx:JSSParser.UnaryContext):
        pass


    # Enter a parse tree produced by JSSParser#postfix.
    def enterPostfix(self, ctx:JSSParser.PostfixContext):
        pass

    # Exit a parse tree produced by JSSParser#postfix.
    def exitPostfix(self, ctx:JSSParser.PostfixContext):
        pass


    # Enter a parse tree produced by JSSParser#postfixOp.
    def enterPostfixOp(self, ctx:JSSParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by JSSParser#postfixOp.
    def exitPostfixOp(self, ctx:JSSParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by JSSParser#argumentList.
    def enterArgumentList(self, ctx:JSSParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by JSSParser#argumentList.
    def exitArgumentList(self, ctx:JSSParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by JSSParser#litInt.
    def enterLitInt(self, ctx:JSSParser.LitIntContext):
        pass

    # Exit a parse tree produced by JSSParser#litInt.
    def exitLitInt(self, ctx:JSSParser.LitIntContext):
        pass


    # Enter a parse tree produced by JSSParser#litReal.
    def enterLitReal(self, ctx:JSSParser.LitRealContext):
        pass

    # Exit a parse tree produced by JSSParser#litReal.
    def exitLitReal(self, ctx:JSSParser.LitRealContext):
        pass


    # Enter a parse tree produced by JSSParser#litStr.
    def enterLitStr(self, ctx:JSSParser.LitStrContext):
        pass

    # Exit a parse tree produced by JSSParser#litStr.
    def exitLitStr(self, ctx:JSSParser.LitStrContext):
        pass


    # Enter a parse tree produced by JSSParser#litTrue.
    def enterLitTrue(self, ctx:JSSParser.LitTrueContext):
        pass

    # Exit a parse tree produced by JSSParser#litTrue.
    def exitLitTrue(self, ctx:JSSParser.LitTrueContext):
        pass


    # Enter a parse tree produced by JSSParser#litFalse.
    def enterLitFalse(self, ctx:JSSParser.LitFalseContext):
        pass

    # Exit a parse tree produced by JSSParser#litFalse.
    def exitLitFalse(self, ctx:JSSParser.LitFalseContext):
        pass


    # Enter a parse tree produced by JSSParser#litNull.
    def enterLitNull(self, ctx:JSSParser.LitNullContext):
        pass

    # Exit a parse tree produced by JSSParser#litNull.
    def exitLitNull(self, ctx:JSSParser.LitNullContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryThis.
    def enterPrimaryThis(self, ctx:JSSParser.PrimaryThisContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryThis.
    def exitPrimaryThis(self, ctx:JSSParser.PrimaryThisContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryId.
    def enterPrimaryId(self, ctx:JSSParser.PrimaryIdContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryId.
    def exitPrimaryId(self, ctx:JSSParser.PrimaryIdContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryInput.
    def enterPrimaryInput(self, ctx:JSSParser.PrimaryInputContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryInput.
    def exitPrimaryInput(self, ctx:JSSParser.PrimaryInputContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryConsoleLog.
    def enterPrimaryConsoleLog(self, ctx:JSSParser.PrimaryConsoleLogContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryConsoleLog.
    def exitPrimaryConsoleLog(self, ctx:JSSParser.PrimaryConsoleLogContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryNew.
    def enterPrimaryNew(self, ctx:JSSParser.PrimaryNewContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryNew.
    def exitPrimaryNew(self, ctx:JSSParser.PrimaryNewContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryParen.
    def enterPrimaryParen(self, ctx:JSSParser.PrimaryParenContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryParen.
    def exitPrimaryParen(self, ctx:JSSParser.PrimaryParenContext):
        pass


    # Enter a parse tree produced by JSSParser#primaryCast.
    def enterPrimaryCast(self, ctx:JSSParser.PrimaryCastContext):
        pass

    # Exit a parse tree produced by JSSParser#primaryCast.
    def exitPrimaryCast(self, ctx:JSSParser.PrimaryCastContext):
        pass



del JSSParser