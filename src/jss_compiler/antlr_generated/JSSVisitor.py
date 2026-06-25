# Generated from src/jss_compiler/JSS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .JSSParser import JSSParser
else:
    from JSSParser import JSSParser

# This class defines a complete generic visitor for a parse tree produced by JSSParser.

class JSSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSSParser#program.
    def visitProgram(self, ctx:JSSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#declaration.
    def visitDeclaration(self, ctx:JSSParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#varDecl.
    def visitVarDecl(self, ctx:JSSParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#constDecl.
    def visitConstDecl(self, ctx:JSSParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#arrayTypeDim.
    def visitArrayTypeDim(self, ctx:JSSParser.ArrayTypeDimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#declarator.
    def visitDeclarator(self, ctx:JSSParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#functionDecl.
    def visitFunctionDecl(self, ctx:JSSParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#parameters.
    def visitParameters(self, ctx:JSSParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#parameter.
    def visitParameter(self, ctx:JSSParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#returnType.
    def visitReturnType(self, ctx:JSSParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#type_.
    def visitType_(self, ctx:JSSParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#classDecl.
    def visitClassDecl(self, ctx:JSSParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#classMember.
    def visitClassMember(self, ctx:JSSParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#constructorDecl.
    def visitConstructorDecl(self, ctx:JSSParser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#block.
    def visitBlock(self, ctx:JSSParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#statement.
    def visitStatement(self, ctx:JSSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#ifStmt.
    def visitIfStmt(self, ctx:JSSParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#whileStmt.
    def visitWhileStmt(self, ctx:JSSParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#forStmt.
    def visitForStmt(self, ctx:JSSParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#forInit.
    def visitForInit(self, ctx:JSSParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#returnStmt.
    def visitReturnStmt(self, ctx:JSSParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#breakStmt.
    def visitBreakStmt(self, ctx:JSSParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#exprStmt.
    def visitExprStmt(self, ctx:JSSParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#expr.
    def visitExpr(self, ctx:JSSParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#assignment.
    def visitAssignment(self, ctx:JSSParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#assignOp.
    def visitAssignOp(self, ctx:JSSParser.AssignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#logicalOr.
    def visitLogicalOr(self, ctx:JSSParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#logicalAnd.
    def visitLogicalAnd(self, ctx:JSSParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#equalityRel.
    def visitEqualityRel(self, ctx:JSSParser.EqualityRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#addition.
    def visitAddition(self, ctx:JSSParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#multiplication.
    def visitMultiplication(self, ctx:JSSParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#exponentiation.
    def visitExponentiation(self, ctx:JSSParser.ExponentiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#unary.
    def visitUnary(self, ctx:JSSParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#postfix.
    def visitPostfix(self, ctx:JSSParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#postfixOp.
    def visitPostfixOp(self, ctx:JSSParser.PostfixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#argumentList.
    def visitArgumentList(self, ctx:JSSParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#litInt.
    def visitLitInt(self, ctx:JSSParser.LitIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#litReal.
    def visitLitReal(self, ctx:JSSParser.LitRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#litStr.
    def visitLitStr(self, ctx:JSSParser.LitStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#litTrue.
    def visitLitTrue(self, ctx:JSSParser.LitTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#litFalse.
    def visitLitFalse(self, ctx:JSSParser.LitFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#litNull.
    def visitLitNull(self, ctx:JSSParser.LitNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryThis.
    def visitPrimaryThis(self, ctx:JSSParser.PrimaryThisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryId.
    def visitPrimaryId(self, ctx:JSSParser.PrimaryIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryInput.
    def visitPrimaryInput(self, ctx:JSSParser.PrimaryInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryConsoleLog.
    def visitPrimaryConsoleLog(self, ctx:JSSParser.PrimaryConsoleLogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryNew.
    def visitPrimaryNew(self, ctx:JSSParser.PrimaryNewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryParen.
    def visitPrimaryParen(self, ctx:JSSParser.PrimaryParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSSParser#primaryCast.
    def visitPrimaryCast(self, ctx:JSSParser.PrimaryCastContext):
        return self.visitChildren(ctx)



del JSSParser