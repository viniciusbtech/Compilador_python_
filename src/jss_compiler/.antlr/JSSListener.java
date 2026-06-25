// Generated from c:/Users/Vinicius/Desktop/profissional/Universidade/semestre 6/Compiladores/Trabalhofinalcompiladores/jss-compiler/src/jss_compiler/JSS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JSSParser}.
 */
public interface JSSListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JSSParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(JSSParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(JSSParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(JSSParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(JSSParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(JSSParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(JSSParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#constDecl}.
	 * @param ctx the parse tree
	 */
	void enterConstDecl(JSSParser.ConstDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#constDecl}.
	 * @param ctx the parse tree
	 */
	void exitConstDecl(JSSParser.ConstDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#arrayTypeDim}.
	 * @param ctx the parse tree
	 */
	void enterArrayTypeDim(JSSParser.ArrayTypeDimContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#arrayTypeDim}.
	 * @param ctx the parse tree
	 */
	void exitArrayTypeDim(JSSParser.ArrayTypeDimContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#declarator}.
	 * @param ctx the parse tree
	 */
	void enterDeclarator(JSSParser.DeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#declarator}.
	 * @param ctx the parse tree
	 */
	void exitDeclarator(JSSParser.DeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(JSSParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(JSSParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(JSSParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(JSSParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(JSSParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(JSSParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#returnType}.
	 * @param ctx the parse tree
	 */
	void enterReturnType(JSSParser.ReturnTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#returnType}.
	 * @param ctx the parse tree
	 */
	void exitReturnType(JSSParser.ReturnTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#type_}.
	 * @param ctx the parse tree
	 */
	void enterType_(JSSParser.Type_Context ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#type_}.
	 * @param ctx the parse tree
	 */
	void exitType_(JSSParser.Type_Context ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(JSSParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(JSSParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#classMember}.
	 * @param ctx the parse tree
	 */
	void enterClassMember(JSSParser.ClassMemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#classMember}.
	 * @param ctx the parse tree
	 */
	void exitClassMember(JSSParser.ClassMemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#constructorDecl}.
	 * @param ctx the parse tree
	 */
	void enterConstructorDecl(JSSParser.ConstructorDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#constructorDecl}.
	 * @param ctx the parse tree
	 */
	void exitConstructorDecl(JSSParser.ConstructorDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(JSSParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(JSSParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(JSSParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(JSSParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(JSSParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(JSSParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(JSSParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(JSSParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(JSSParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(JSSParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(JSSParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(JSSParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(JSSParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(JSSParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(JSSParser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(JSSParser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void enterExprStmt(JSSParser.ExprStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void exitExprStmt(JSSParser.ExprStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(JSSParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(JSSParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(JSSParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(JSSParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#assignOp}.
	 * @param ctx the parse tree
	 */
	void enterAssignOp(JSSParser.AssignOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#assignOp}.
	 * @param ctx the parse tree
	 */
	void exitAssignOp(JSSParser.AssignOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#logicalOr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOr(JSSParser.LogicalOrContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#logicalOr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOr(JSSParser.LogicalOrContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#logicalAnd}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAnd(JSSParser.LogicalAndContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#logicalAnd}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAnd(JSSParser.LogicalAndContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#equalityRel}.
	 * @param ctx the parse tree
	 */
	void enterEqualityRel(JSSParser.EqualityRelContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#equalityRel}.
	 * @param ctx the parse tree
	 */
	void exitEqualityRel(JSSParser.EqualityRelContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#addition}.
	 * @param ctx the parse tree
	 */
	void enterAddition(JSSParser.AdditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#addition}.
	 * @param ctx the parse tree
	 */
	void exitAddition(JSSParser.AdditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#multiplication}.
	 * @param ctx the parse tree
	 */
	void enterMultiplication(JSSParser.MultiplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#multiplication}.
	 * @param ctx the parse tree
	 */
	void exitMultiplication(JSSParser.MultiplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#exponentiation}.
	 * @param ctx the parse tree
	 */
	void enterExponentiation(JSSParser.ExponentiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#exponentiation}.
	 * @param ctx the parse tree
	 */
	void exitExponentiation(JSSParser.ExponentiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#unary}.
	 * @param ctx the parse tree
	 */
	void enterUnary(JSSParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#unary}.
	 * @param ctx the parse tree
	 */
	void exitUnary(JSSParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#postfix}.
	 * @param ctx the parse tree
	 */
	void enterPostfix(JSSParser.PostfixContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#postfix}.
	 * @param ctx the parse tree
	 */
	void exitPostfix(JSSParser.PostfixContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#postfixOp}.
	 * @param ctx the parse tree
	 */
	void enterPostfixOp(JSSParser.PostfixOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#postfixOp}.
	 * @param ctx the parse tree
	 */
	void exitPostfixOp(JSSParser.PostfixOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link JSSParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(JSSParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSSParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(JSSParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litInt}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterLitInt(JSSParser.LitIntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litInt}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitLitInt(JSSParser.LitIntContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litReal}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterLitReal(JSSParser.LitRealContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litReal}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitLitReal(JSSParser.LitRealContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litStr}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterLitStr(JSSParser.LitStrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litStr}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitLitStr(JSSParser.LitStrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litTrue}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterLitTrue(JSSParser.LitTrueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litTrue}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitLitTrue(JSSParser.LitTrueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litFalse}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterLitFalse(JSSParser.LitFalseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litFalse}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitLitFalse(JSSParser.LitFalseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litNull}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterLitNull(JSSParser.LitNullContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litNull}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitLitNull(JSSParser.LitNullContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryThis}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryThis(JSSParser.PrimaryThisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryThis}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryThis(JSSParser.PrimaryThisContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryId}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryId(JSSParser.PrimaryIdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryId}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryId(JSSParser.PrimaryIdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryInput}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryInput(JSSParser.PrimaryInputContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryInput}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryInput(JSSParser.PrimaryInputContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryConsoleLog}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryConsoleLog(JSSParser.PrimaryConsoleLogContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryConsoleLog}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryConsoleLog(JSSParser.PrimaryConsoleLogContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryNew}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryNew(JSSParser.PrimaryNewContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryNew}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryNew(JSSParser.PrimaryNewContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryParen}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryParen(JSSParser.PrimaryParenContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryParen}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryParen(JSSParser.PrimaryParenContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryCast}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryCast(JSSParser.PrimaryCastContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryCast}
	 * labeled alternative in {@link JSSParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryCast(JSSParser.PrimaryCastContext ctx);
}