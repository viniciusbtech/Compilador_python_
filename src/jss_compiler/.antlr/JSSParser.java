// Generated from c:/Users/Vinicius/Desktop/profissional/Universidade/semestre 6/Compiladores/Trabalhofinalcompiladores/jss-compiler/src/jss_compiler/JSS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class JSSParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, CONST=2, FUNCTION=3, VOID=4, IF=5, ELSE=6, WHILE=7, FOR=8, BREAK=9, 
		RETURN=10, CLASS=11, CONSTRUCTOR=12, NEW=13, THIS=14, TRUE=15, FALSE=16, 
		NULL=17, INPUT=18, CONSOLE_LOG=19, TYPE_INT=20, TYPE_REAL=21, TYPE_STR=22, 
		TYPE_BOOL=23, REAL_LITERAL=24, INTEGER_LITERAL=25, STRING_LITERAL=26, 
		IDENTIFIER=27, POWER_ASSIGN=28, POWER=29, EQUAL_EQUAL=30, BANG_EQUAL=31, 
		GREATER_EQUAL=32, LESS_EQUAL=33, AND_AND=34, OR_OR=35, PLUS_PLUS=36, MINUS_MINUS=37, 
		PLUS_ASSIGN=38, MINUS_ASSIGN=39, STAR_ASSIGN=40, SLASH_ASSIGN=41, PERCENT_ASSIGN=42, 
		ASSIGN=43, PLUS=44, MINUS=45, STAR=46, SLASH=47, PERCENT=48, BANG=49, 
		GREATER=50, LESS=51, LEFT_PAREN=52, RIGHT_PAREN=53, LEFT_BRACE=54, RIGHT_BRACE=55, 
		LEFT_BRACKET=56, RIGHT_BRACKET=57, SEMICOLON=58, COMMA=59, DOT=60, WS=61, 
		COMMENT=62;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_varDecl = 2, RULE_constDecl = 3, 
		RULE_arrayTypeDim = 4, RULE_declarator = 5, RULE_functionDecl = 6, RULE_parameters = 7, 
		RULE_parameter = 8, RULE_returnType = 9, RULE_type_ = 10, RULE_classDecl = 11, 
		RULE_classMember = 12, RULE_constructorDecl = 13, RULE_block = 14, RULE_statement = 15, 
		RULE_ifStmt = 16, RULE_whileStmt = 17, RULE_forStmt = 18, RULE_forInit = 19, 
		RULE_returnStmt = 20, RULE_breakStmt = 21, RULE_exprStmt = 22, RULE_expr = 23, 
		RULE_assignment = 24, RULE_assignOp = 25, RULE_logicalOr = 26, RULE_logicalAnd = 27, 
		RULE_equalityRel = 28, RULE_addition = 29, RULE_multiplication = 30, RULE_exponentiation = 31, 
		RULE_unary = 32, RULE_postfix = 33, RULE_postfixOp = 34, RULE_argumentList = 35, 
		RULE_primary = 36;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "varDecl", "constDecl", "arrayTypeDim", "declarator", 
			"functionDecl", "parameters", "parameter", "returnType", "type_", "classDecl", 
			"classMember", "constructorDecl", "block", "statement", "ifStmt", "whileStmt", 
			"forStmt", "forInit", "returnStmt", "breakStmt", "exprStmt", "expr", 
			"assignment", "assignOp", "logicalOr", "logicalAnd", "equalityRel", "addition", 
			"multiplication", "exponentiation", "unary", "postfix", "postfixOp", 
			"argumentList", "primary"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'const'", "'function'", "'void'", "'if'", "'else'", "'while'", 
			"'for'", "'break'", "'return'", "'class'", "'constructor'", "'new'", 
			"'this'", "'true'", "'false'", "'null'", "'input'", "'console.log'", 
			"'int'", "'real'", "'str'", "'bool'", null, null, null, null, "'**='", 
			"'**'", "'=='", "'!='", "'>='", "'<='", "'&&'", "'||'", "'++'", "'--'", 
			"'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'!'", "'>'", "'<'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
			"';'", "','", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "CONST", "FUNCTION", "VOID", "IF", "ELSE", "WHILE", "FOR", 
			"BREAK", "RETURN", "CLASS", "CONSTRUCTOR", "NEW", "THIS", "TRUE", "FALSE", 
			"NULL", "INPUT", "CONSOLE_LOG", "TYPE_INT", "TYPE_REAL", "TYPE_STR", 
			"TYPE_BOOL", "REAL_LITERAL", "INTEGER_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
			"POWER_ASSIGN", "POWER", "EQUAL_EQUAL", "BANG_EQUAL", "GREATER_EQUAL", 
			"LESS_EQUAL", "AND_AND", "OR_OR", "PLUS_PLUS", "MINUS_MINUS", "PLUS_ASSIGN", 
			"MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", "PERCENT_ASSIGN", "ASSIGN", 
			"PLUS", "MINUS", "STAR", "SLASH", "PERCENT", "BANG", "GREATER", "LESS", 
			"LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE", "LEFT_BRACKET", 
			"RIGHT_BRACKET", "SEMICOLON", "COMMA", "DOT", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "JSS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JSSParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(JSSParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565784590L) != 0)) {
				{
				{
				setState(74);
				declaration();
				}
				}
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(80);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public ConstDeclContext constDecl() {
			return getRuleContext(ConstDeclContext.class,0);
		}
		public FunctionDeclContext functionDecl() {
			return getRuleContext(FunctionDeclContext.class,0);
		}
		public ClassDeclContext classDecl() {
			return getRuleContext(ClassDeclContext.class,0);
		}
		public ExprStmtContext exprStmt() {
			return getRuleContext(ExprStmtContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(87);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				varDecl();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				constDecl();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 3);
				{
				setState(84);
				functionDecl();
				}
				break;
			case CLASS:
				enterOuterAlt(_localctx, 4);
				{
				setState(85);
				classDecl();
				}
				break;
			case NEW:
			case THIS:
			case TRUE:
			case FALSE:
			case NULL:
			case INPUT:
			case CONSOLE_LOG:
			case TYPE_INT:
			case TYPE_REAL:
			case TYPE_STR:
			case TYPE_BOOL:
			case REAL_LITERAL:
			case INTEGER_LITERAL:
			case STRING_LITERAL:
			case IDENTIFIER:
			case PLUS_PLUS:
			case MINUS_MINUS:
			case PLUS:
			case MINUS:
			case BANG:
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(86);
				exprStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(JSSParser.LET, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public List<DeclaratorContext> declarator() {
			return getRuleContexts(DeclaratorContext.class);
		}
		public DeclaratorContext declarator(int i) {
			return getRuleContext(DeclaratorContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public ArrayTypeDimContext arrayTypeDim() {
			return getRuleContext(ArrayTypeDimContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(JSSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JSSParser.COMMA, i);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(LET);
			setState(90);
			type_();
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFT_BRACKET) {
				{
				setState(91);
				arrayTypeDim();
				}
			}

			setState(94);
			declarator();
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(95);
				match(COMMA);
				setState(96);
				declarator();
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(102);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstDeclContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(JSSParser.CONST, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public List<DeclaratorContext> declarator() {
			return getRuleContexts(DeclaratorContext.class);
		}
		public DeclaratorContext declarator(int i) {
			return getRuleContext(DeclaratorContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public ArrayTypeDimContext arrayTypeDim() {
			return getRuleContext(ArrayTypeDimContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(JSSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JSSParser.COMMA, i);
		}
		public ConstDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constDecl; }
	}

	public final ConstDeclContext constDecl() throws RecognitionException {
		ConstDeclContext _localctx = new ConstDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_constDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(CONST);
			setState(105);
			type_();
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFT_BRACKET) {
				{
				setState(106);
				arrayTypeDim();
				}
			}

			setState(109);
			declarator();
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(110);
				match(COMMA);
				setState(111);
				declarator();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayTypeDimContext extends ParserRuleContext {
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(JSSParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(JSSParser.LEFT_BRACKET, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(JSSParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(JSSParser.RIGHT_BRACKET, i);
		}
		public ArrayTypeDimContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayTypeDim; }
	}

	public final ArrayTypeDimContext arrayTypeDim() throws RecognitionException {
		ArrayTypeDimContext _localctx = new ArrayTypeDimContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_arrayTypeDim);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(LEFT_BRACKET);
			setState(120);
			expr();
			setState(121);
			match(RIGHT_BRACKET);
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFT_BRACKET) {
				{
				setState(122);
				match(LEFT_BRACKET);
				setState(123);
				expr();
				setState(124);
				match(RIGHT_BRACKET);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaratorContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(JSSParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(JSSParser.LEFT_BRACKET, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(JSSParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(JSSParser.RIGHT_BRACKET, i);
		}
		public TerminalNode ASSIGN() { return getToken(JSSParser.ASSIGN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(JSSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JSSParser.COMMA, i);
		}
		public DeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarator; }
	}

	public final DeclaratorContext declarator() throws RecognitionException {
		DeclaratorContext _localctx = new DeclaratorContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declarator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(IDENTIFIER);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LEFT_BRACKET) {
				{
				setState(129);
				match(LEFT_BRACKET);
				setState(130);
				expr();
				setState(131);
				match(RIGHT_BRACKET);
				}
			}

			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(135);
				match(ASSIGN);
				setState(149);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LEFT_BRACKET:
					{
					setState(136);
					match(LEFT_BRACKET);
					setState(145);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
						{
						setState(137);
						expr();
						setState(142);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(138);
							match(COMMA);
							setState(139);
							expr();
							}
							}
							setState(144);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
					}

					setState(147);
					match(RIGHT_BRACKET);
					}
					break;
				case NEW:
				case THIS:
				case TRUE:
				case FALSE:
				case NULL:
				case INPUT:
				case CONSOLE_LOG:
				case TYPE_INT:
				case TYPE_REAL:
				case TYPE_STR:
				case TYPE_BOOL:
				case REAL_LITERAL:
				case INTEGER_LITERAL:
				case STRING_LITERAL:
				case IDENTIFIER:
				case PLUS_PLUS:
				case MINUS_MINUS:
				case PLUS:
				case MINUS:
				case BANG:
				case LEFT_PAREN:
					{
					setState(148);
					expr();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(JSSParser.FUNCTION, 0); }
		public ReturnTypeContext returnType() {
			return getRuleContext(ReturnTypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FunctionDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDecl; }
	}

	public final FunctionDeclContext functionDecl() throws RecognitionException {
		FunctionDeclContext _localctx = new FunctionDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_functionDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(FUNCTION);
			setState(154);
			returnType();
			setState(155);
			match(IDENTIFIER);
			setState(156);
			parameters();
			setState(157);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(JSSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JSSParser.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(LEFT_PAREN);
			setState(168);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 149946368L) != 0)) {
				{
				setState(160);
				parameter();
				setState(165);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(161);
					match(COMMA);
					setState(162);
					parameter();
					}
					}
					setState(167);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(170);
			match(RIGHT_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			type_();
			setState(173);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnTypeContext extends ParserRuleContext {
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode VOID() { return getToken(JSSParser.VOID, 0); }
		public ReturnTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnType; }
	}

	public final ReturnTypeContext returnType() throws RecognitionException {
		ReturnTypeContext _localctx = new ReturnTypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_returnType);
		try {
			setState(177);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE_INT:
			case TYPE_REAL:
			case TYPE_STR:
			case TYPE_BOOL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(175);
				type_();
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(176);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Type_Context extends ParserRuleContext {
		public TerminalNode TYPE_INT() { return getToken(JSSParser.TYPE_INT, 0); }
		public TerminalNode TYPE_REAL() { return getToken(JSSParser.TYPE_REAL, 0); }
		public TerminalNode TYPE_STR() { return getToken(JSSParser.TYPE_STR, 0); }
		public TerminalNode TYPE_BOOL() { return getToken(JSSParser.TYPE_BOOL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public Type_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_; }
	}

	public final Type_Context type_() throws RecognitionException {
		Type_Context _localctx = new Type_Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_type_);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 149946368L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassDeclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(JSSParser.CLASS, 0); }
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public TerminalNode LEFT_BRACE() { return getToken(JSSParser.LEFT_BRACE, 0); }
		public TerminalNode RIGHT_BRACE() { return getToken(JSSParser.RIGHT_BRACE, 0); }
		public List<ClassMemberContext> classMember() {
			return getRuleContexts(ClassMemberContext.class);
		}
		public ClassMemberContext classMember(int i) {
			return getRuleContext(ClassMemberContext.class,i);
		}
		public ClassDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDecl; }
	}

	public final ClassDeclContext classDecl() throws RecognitionException {
		ClassDeclContext _localctx = new ClassDeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_classDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(CLASS);
			setState(182);
			match(IDENTIFIER);
			setState(183);
			match(LEFT_BRACE);
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 149946384L) != 0)) {
				{
				{
				setState(184);
				classMember();
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(190);
			match(RIGHT_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassMemberContext extends ParserRuleContext {
		public ConstructorDeclContext constructorDecl() {
			return getRuleContext(ConstructorDeclContext.class,0);
		}
		public ReturnTypeContext returnType() {
			return getRuleContext(ReturnTypeContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public ClassMemberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classMember; }
	}

	public final ClassMemberContext classMember() throws RecognitionException {
		ClassMemberContext _localctx = new ClassMemberContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_classMember);
		try {
			setState(202);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(192);
				constructorDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(193);
				returnType();
				setState(194);
				match(IDENTIFIER);
				setState(195);
				parameters();
				setState(196);
				block();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(198);
				type_();
				setState(199);
				match(IDENTIFIER);
				setState(200);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstructorDeclContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public TerminalNode CONSTRUCTOR() { return getToken(JSSParser.CONSTRUCTOR, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ConstructorDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructorDecl; }
	}

	public final ConstructorDeclContext constructorDecl() throws RecognitionException {
		ConstructorDeclContext _localctx = new ConstructorDeclContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_constructorDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(IDENTIFIER);
			setState(205);
			match(CONSTRUCTOR);
			setState(206);
			parameters();
			setState(207);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACE() { return getToken(JSSParser.LEFT_BRACE, 0); }
		public TerminalNode RIGHT_BRACE() { return getToken(JSSParser.RIGHT_BRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(LEFT_BRACE);
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 23133931075266470L) != 0)) {
				{
				{
				setState(210);
				statement();
				}
				}
				setState(215);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(216);
			match(RIGHT_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public ConstDeclContext constDecl() {
			return getRuleContext(ConstDeclContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
		}
		public ReturnStmtContext returnStmt() {
			return getRuleContext(ReturnStmtContext.class,0);
		}
		public BreakStmtContext breakStmt() {
			return getRuleContext(BreakStmtContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ExprStmtContext exprStmt() {
			return getRuleContext(ExprStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_statement);
		try {
			setState(227);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(218);
				varDecl();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(219);
				constDecl();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(220);
				ifStmt();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(221);
				whileStmt();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(222);
				forStmt();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 6);
				{
				setState(223);
				returnStmt();
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 7);
				{
				setState(224);
				breakStmt();
				}
				break;
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 8);
				{
				setState(225);
				block();
				}
				break;
			case NEW:
			case THIS:
			case TRUE:
			case FALSE:
			case NULL:
			case INPUT:
			case CONSOLE_LOG:
			case TYPE_INT:
			case TYPE_REAL:
			case TYPE_STR:
			case TYPE_BOOL:
			case REAL_LITERAL:
			case INTEGER_LITERAL:
			case STRING_LITERAL:
			case IDENTIFIER:
			case PLUS_PLUS:
			case MINUS_MINUS:
			case PLUS:
			case MINUS:
			case BANG:
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 9);
				{
				setState(226);
				exprStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(JSSParser.IF, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(JSSParser.ELSE, 0); }
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(IF);
			setState(230);
			match(LEFT_PAREN);
			setState(231);
			expr();
			setState(232);
			match(RIGHT_PAREN);
			setState(233);
			block();
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(234);
				match(ELSE);
				setState(237);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LEFT_BRACE:
					{
					setState(235);
					block();
					}
					break;
				case IF:
					{
					setState(236);
					ifStmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(JSSParser.WHILE, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_whileStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(WHILE);
			setState(242);
			match(LEFT_PAREN);
			setState(243);
			expr();
			setState(244);
			match(RIGHT_PAREN);
			setState(245);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(JSSParser.FOR, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public ForInitContext forInit() {
			return getRuleContext(ForInitContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_forStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(FOR);
			setState(248);
			match(LEFT_PAREN);
			setState(249);
			forInit();
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
				{
				setState(250);
				expr();
				}
			}

			setState(253);
			match(SEMICOLON);
			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
				{
				setState(254);
				expr();
				}
			}

			setState(257);
			match(RIGHT_PAREN);
			setState(258);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForInitContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public ConstDeclContext constDecl() {
			return getRuleContext(ConstDeclContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public ForInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forInit; }
	}

	public final ForInitContext forInit() throws RecognitionException {
		ForInitContext _localctx = new ForInitContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_forInit);
		try {
			setState(266);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(260);
				varDecl();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(261);
				constDecl();
				}
				break;
			case NEW:
			case THIS:
			case TRUE:
			case FALSE:
			case NULL:
			case INPUT:
			case CONSOLE_LOG:
			case TYPE_INT:
			case TYPE_REAL:
			case TYPE_STR:
			case TYPE_BOOL:
			case REAL_LITERAL:
			case INTEGER_LITERAL:
			case STRING_LITERAL:
			case IDENTIFIER:
			case PLUS_PLUS:
			case MINUS_MINUS:
			case PLUS:
			case MINUS:
			case BANG:
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 3);
				{
				setState(262);
				expr();
				setState(263);
				match(SEMICOLON);
				}
				break;
			case SEMICOLON:
				enterOuterAlt(_localctx, 4);
				{
				setState(265);
				match(SEMICOLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(JSSParser.RETURN, 0); }
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStmt; }
	}

	public final ReturnStmtContext returnStmt() throws RecognitionException {
		ReturnStmtContext _localctx = new ReturnStmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_returnStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(RETURN);
			setState(270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
				{
				setState(269);
				expr();
				}
			}

			setState(272);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakStmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(JSSParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public BreakStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStmt; }
	}

	public final BreakStmtContext breakStmt() throws RecognitionException {
		BreakStmtContext _localctx = new BreakStmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_breakStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			match(BREAK);
			setState(275);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprStmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(JSSParser.SEMICOLON, 0); }
		public ExprStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprStmt; }
	}

	public final ExprStmtContext exprStmt() throws RecognitionException {
		ExprStmtContext _localctx = new ExprStmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_exprStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			expr();
			setState(278);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			assignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public LogicalOrContext logicalOr() {
			return getRuleContext(LogicalOrContext.class,0);
		}
		public AssignOpContext assignOp() {
			return getRuleContext(AssignOpContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			logicalOr();
			setState(286);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17317576572928L) != 0)) {
				{
				setState(283);
				assignOp();
				setState(284);
				assignment();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignOpContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(JSSParser.ASSIGN, 0); }
		public TerminalNode PLUS_ASSIGN() { return getToken(JSSParser.PLUS_ASSIGN, 0); }
		public TerminalNode MINUS_ASSIGN() { return getToken(JSSParser.MINUS_ASSIGN, 0); }
		public TerminalNode STAR_ASSIGN() { return getToken(JSSParser.STAR_ASSIGN, 0); }
		public TerminalNode SLASH_ASSIGN() { return getToken(JSSParser.SLASH_ASSIGN, 0); }
		public TerminalNode PERCENT_ASSIGN() { return getToken(JSSParser.PERCENT_ASSIGN, 0); }
		public TerminalNode POWER_ASSIGN() { return getToken(JSSParser.POWER_ASSIGN, 0); }
		public AssignOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignOp; }
	}

	public final AssignOpContext assignOp() throws RecognitionException {
		AssignOpContext _localctx = new AssignOpContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_assignOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17317576572928L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrContext extends ParserRuleContext {
		public List<LogicalAndContext> logicalAnd() {
			return getRuleContexts(LogicalAndContext.class);
		}
		public LogicalAndContext logicalAnd(int i) {
			return getRuleContext(LogicalAndContext.class,i);
		}
		public List<TerminalNode> OR_OR() { return getTokens(JSSParser.OR_OR); }
		public TerminalNode OR_OR(int i) {
			return getToken(JSSParser.OR_OR, i);
		}
		public LogicalOrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOr; }
	}

	public final LogicalOrContext logicalOr() throws RecognitionException {
		LogicalOrContext _localctx = new LogicalOrContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_logicalOr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			logicalAnd();
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR_OR) {
				{
				{
				setState(291);
				match(OR_OR);
				setState(292);
				logicalAnd();
				}
				}
				setState(297);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndContext extends ParserRuleContext {
		public List<EqualityRelContext> equalityRel() {
			return getRuleContexts(EqualityRelContext.class);
		}
		public EqualityRelContext equalityRel(int i) {
			return getRuleContext(EqualityRelContext.class,i);
		}
		public List<TerminalNode> AND_AND() { return getTokens(JSSParser.AND_AND); }
		public TerminalNode AND_AND(int i) {
			return getToken(JSSParser.AND_AND, i);
		}
		public LogicalAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAnd; }
	}

	public final LogicalAndContext logicalAnd() throws RecognitionException {
		LogicalAndContext _localctx = new LogicalAndContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_logicalAnd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			equalityRel();
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND_AND) {
				{
				{
				setState(299);
				match(AND_AND);
				setState(300);
				equalityRel();
				}
				}
				setState(305);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityRelContext extends ParserRuleContext {
		public List<AdditionContext> addition() {
			return getRuleContexts(AdditionContext.class);
		}
		public AdditionContext addition(int i) {
			return getRuleContext(AdditionContext.class,i);
		}
		public List<TerminalNode> EQUAL_EQUAL() { return getTokens(JSSParser.EQUAL_EQUAL); }
		public TerminalNode EQUAL_EQUAL(int i) {
			return getToken(JSSParser.EQUAL_EQUAL, i);
		}
		public List<TerminalNode> BANG_EQUAL() { return getTokens(JSSParser.BANG_EQUAL); }
		public TerminalNode BANG_EQUAL(int i) {
			return getToken(JSSParser.BANG_EQUAL, i);
		}
		public List<TerminalNode> GREATER() { return getTokens(JSSParser.GREATER); }
		public TerminalNode GREATER(int i) {
			return getToken(JSSParser.GREATER, i);
		}
		public List<TerminalNode> GREATER_EQUAL() { return getTokens(JSSParser.GREATER_EQUAL); }
		public TerminalNode GREATER_EQUAL(int i) {
			return getToken(JSSParser.GREATER_EQUAL, i);
		}
		public List<TerminalNode> LESS() { return getTokens(JSSParser.LESS); }
		public TerminalNode LESS(int i) {
			return getToken(JSSParser.LESS, i);
		}
		public List<TerminalNode> LESS_EQUAL() { return getTokens(JSSParser.LESS_EQUAL); }
		public TerminalNode LESS_EQUAL(int i) {
			return getToken(JSSParser.LESS_EQUAL, i);
		}
		public EqualityRelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityRel; }
	}

	public final EqualityRelContext equalityRel() throws RecognitionException {
		EqualityRelContext _localctx = new EqualityRelContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_equalityRel);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			addition();
			setState(311);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3377715826655232L) != 0)) {
				{
				{
				setState(307);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3377715826655232L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(308);
				addition();
				}
				}
				setState(313);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditionContext extends ParserRuleContext {
		public List<MultiplicationContext> multiplication() {
			return getRuleContexts(MultiplicationContext.class);
		}
		public MultiplicationContext multiplication(int i) {
			return getRuleContext(MultiplicationContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(JSSParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(JSSParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(JSSParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(JSSParser.MINUS, i);
		}
		public AdditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addition; }
	}

	public final AdditionContext addition() throws RecognitionException {
		AdditionContext _localctx = new AdditionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_addition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			multiplication();
			setState(319);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(315);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(316);
				multiplication();
				}
				}
				setState(321);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicationContext extends ParserRuleContext {
		public List<ExponentiationContext> exponentiation() {
			return getRuleContexts(ExponentiationContext.class);
		}
		public ExponentiationContext exponentiation(int i) {
			return getRuleContext(ExponentiationContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(JSSParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(JSSParser.STAR, i);
		}
		public List<TerminalNode> SLASH() { return getTokens(JSSParser.SLASH); }
		public TerminalNode SLASH(int i) {
			return getToken(JSSParser.SLASH, i);
		}
		public List<TerminalNode> PERCENT() { return getTokens(JSSParser.PERCENT); }
		public TerminalNode PERCENT(int i) {
			return getToken(JSSParser.PERCENT, i);
		}
		public MultiplicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplication; }
	}

	public final MultiplicationContext multiplication() throws RecognitionException {
		MultiplicationContext _localctx = new MultiplicationContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_multiplication);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			exponentiation();
			setState(327);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 492581209243648L) != 0)) {
				{
				{
				setState(323);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 492581209243648L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(324);
				exponentiation();
				}
				}
				setState(329);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExponentiationContext extends ParserRuleContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TerminalNode POWER() { return getToken(JSSParser.POWER, 0); }
		public ExponentiationContext exponentiation() {
			return getRuleContext(ExponentiationContext.class,0);
		}
		public ExponentiationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exponentiation; }
	}

	public final ExponentiationContext exponentiation() throws RecognitionException {
		ExponentiationContext _localctx = new ExponentiationContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_exponentiation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(330);
			unary();
			setState(333);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==POWER) {
				{
				setState(331);
				match(POWER);
				setState(332);
				exponentiation();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryContext extends ParserRuleContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TerminalNode BANG() { return getToken(JSSParser.BANG, 0); }
		public TerminalNode PLUS() { return getToken(JSSParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(JSSParser.MINUS, 0); }
		public TerminalNode PLUS_PLUS() { return getToken(JSSParser.PLUS_PLUS, 0); }
		public TerminalNode MINUS_MINUS() { return getToken(JSSParser.MINUS_MINUS, 0); }
		public PostfixContext postfix() {
			return getRuleContext(PostfixContext.class,0);
		}
		public UnaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary; }
	}

	public final UnaryContext unary() throws RecognitionException {
		UnaryContext _localctx = new UnaryContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_unary);
		int _la;
		try {
			setState(338);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS_PLUS:
			case MINUS_MINUS:
			case PLUS:
			case MINUS:
			case BANG:
				enterOuterAlt(_localctx, 1);
				{
				setState(335);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 615932669984768L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(336);
				unary();
				}
				break;
			case NEW:
			case THIS:
			case TRUE:
			case FALSE:
			case NULL:
			case INPUT:
			case CONSOLE_LOG:
			case TYPE_INT:
			case TYPE_REAL:
			case TYPE_STR:
			case TYPE_BOOL:
			case REAL_LITERAL:
			case INTEGER_LITERAL:
			case STRING_LITERAL:
			case IDENTIFIER:
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(337);
				postfix();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PostfixContext extends ParserRuleContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public List<PostfixOpContext> postfixOp() {
			return getRuleContexts(PostfixOpContext.class);
		}
		public PostfixOpContext postfixOp(int i) {
			return getRuleContext(PostfixOpContext.class,i);
		}
		public PostfixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfix; }
	}

	public final PostfixContext postfix() throws RecognitionException {
		PostfixContext _localctx = new PostfixContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_postfix);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
			primary();
			setState(344);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1229482698272145408L) != 0)) {
				{
				{
				setState(341);
				postfixOp();
				}
				}
				setState(346);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PostfixOpContext extends ParserRuleContext {
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public TerminalNode LEFT_BRACKET() { return getToken(JSSParser.LEFT_BRACKET, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(JSSParser.RIGHT_BRACKET, 0); }
		public TerminalNode DOT() { return getToken(JSSParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public PostfixOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfixOp; }
	}

	public final PostfixOpContext postfixOp() throws RecognitionException {
		PostfixOpContext _localctx = new PostfixOpContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_postfixOp);
		int _la;
		try {
			setState(358);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(LEFT_PAREN);
				setState(349);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
					{
					setState(348);
					argumentList();
					}
				}

				setState(351);
				match(RIGHT_PAREN);
				}
				break;
			case LEFT_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(352);
				match(LEFT_BRACKET);
				setState(353);
				expr();
				setState(354);
				match(RIGHT_BRACKET);
				}
				break;
			case DOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(356);
				match(DOT);
				setState(357);
				match(IDENTIFIER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(JSSParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(JSSParser.COMMA, i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
			expr();
			setState(365);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(361);
				match(COMMA);
				setState(362);
				expr();
				}
				}
				setState(367);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	 
		public PrimaryContext() { }
		public void copyFrom(PrimaryContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitRealContext extends PrimaryContext {
		public TerminalNode REAL_LITERAL() { return getToken(JSSParser.REAL_LITERAL, 0); }
		public LitRealContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryCastContext extends PrimaryContext {
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public TerminalNode TYPE_INT() { return getToken(JSSParser.TYPE_INT, 0); }
		public TerminalNode TYPE_REAL() { return getToken(JSSParser.TYPE_REAL, 0); }
		public TerminalNode TYPE_BOOL() { return getToken(JSSParser.TYPE_BOOL, 0); }
		public TerminalNode TYPE_STR() { return getToken(JSSParser.TYPE_STR, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public PrimaryCastContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryConsoleLogContext extends PrimaryContext {
		public TerminalNode CONSOLE_LOG() { return getToken(JSSParser.CONSOLE_LOG, 0); }
		public PrimaryConsoleLogContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryThisContext extends PrimaryContext {
		public TerminalNode THIS() { return getToken(JSSParser.THIS, 0); }
		public PrimaryThisContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitFalseContext extends PrimaryContext {
		public TerminalNode FALSE() { return getToken(JSSParser.FALSE, 0); }
		public LitFalseContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitNullContext extends PrimaryContext {
		public TerminalNode NULL() { return getToken(JSSParser.NULL, 0); }
		public LitNullContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryIdContext extends PrimaryContext {
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public PrimaryIdContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitIntContext extends PrimaryContext {
		public TerminalNode INTEGER_LITERAL() { return getToken(JSSParser.INTEGER_LITERAL, 0); }
		public LitIntContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryParenContext extends PrimaryContext {
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public PrimaryParenContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitStrContext extends PrimaryContext {
		public TerminalNode STRING_LITERAL() { return getToken(JSSParser.STRING_LITERAL, 0); }
		public LitStrContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryInputContext extends PrimaryContext {
		public TerminalNode INPUT() { return getToken(JSSParser.INPUT, 0); }
		public PrimaryInputContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryNewContext extends PrimaryContext {
		public TerminalNode NEW() { return getToken(JSSParser.NEW, 0); }
		public TerminalNode IDENTIFIER() { return getToken(JSSParser.IDENTIFIER, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(JSSParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(JSSParser.RIGHT_PAREN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public PrimaryNewContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitTrueContext extends PrimaryContext {
		public TerminalNode TRUE() { return getToken(JSSParser.TRUE, 0); }
		public LitTrueContext(PrimaryContext ctx) { copyFrom(ctx); }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_primary);
		int _la;
		try {
			setState(395);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LITERAL:
				_localctx = new LitIntContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(368);
				match(INTEGER_LITERAL);
				}
				break;
			case REAL_LITERAL:
				_localctx = new LitRealContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(369);
				match(REAL_LITERAL);
				}
				break;
			case STRING_LITERAL:
				_localctx = new LitStrContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(370);
				match(STRING_LITERAL);
				}
				break;
			case TRUE:
				_localctx = new LitTrueContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(371);
				match(TRUE);
				}
				break;
			case FALSE:
				_localctx = new LitFalseContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(372);
				match(FALSE);
				}
				break;
			case NULL:
				_localctx = new LitNullContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(373);
				match(NULL);
				}
				break;
			case THIS:
				_localctx = new PrimaryThisContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(374);
				match(THIS);
				}
				break;
			case IDENTIFIER:
				_localctx = new PrimaryIdContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(375);
				match(IDENTIFIER);
				}
				break;
			case INPUT:
				_localctx = new PrimaryInputContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(376);
				match(INPUT);
				}
				break;
			case CONSOLE_LOG:
				_localctx = new PrimaryConsoleLogContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(377);
				match(CONSOLE_LOG);
				}
				break;
			case NEW:
				_localctx = new PrimaryNewContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(378);
				match(NEW);
				setState(379);
				match(IDENTIFIER);
				setState(380);
				match(LEFT_PAREN);
				setState(382);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
					{
					setState(381);
					argumentList();
					}
				}

				setState(384);
				match(RIGHT_PAREN);
				}
				break;
			case LEFT_PAREN:
				_localctx = new PrimaryParenContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(385);
				match(LEFT_PAREN);
				setState(386);
				expr();
				setState(387);
				match(RIGHT_PAREN);
				}
				break;
			case TYPE_INT:
			case TYPE_REAL:
			case TYPE_STR:
			case TYPE_BOOL:
				_localctx = new PrimaryCastContext(_localctx);
				enterOuterAlt(_localctx, 13);
				{
				setState(389);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15728640L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(390);
				match(LEFT_PAREN);
				setState(392);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 5119532565782528L) != 0)) {
					{
					setState(391);
					argumentList();
					}
				}

				setState(394);
				match(RIGHT_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001>\u018e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0001\u0000\u0005\u0000L\b\u0000\n\u0000\f\u0000"+
		"O\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001X\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002]\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u0002b\b\u0002\n\u0002\f\u0002e\t\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003l\b\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0005\u0003q\b\u0003\n\u0003\f\u0003t\t\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u007f\b\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u0086\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005"+
		"\u008d\b\u0005\n\u0005\f\u0005\u0090\t\u0005\u0003\u0005\u0092\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005\u0096\b\u0005\u0003\u0005\u0098\b"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u00a4"+
		"\b\u0007\n\u0007\f\u0007\u00a7\t\u0007\u0003\u0007\u00a9\b\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0003\t\u00b2"+
		"\b\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005"+
		"\u000b\u00ba\b\u000b\n\u000b\f\u000b\u00bd\t\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0003\f\u00cb\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0005\u000e\u00d4\b\u000e\n\u000e\f\u000e\u00d7\t\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00e4\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00ee\b\u0010\u0003\u0010"+
		"\u00f0\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012"+
		"\u00fc\b\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u0100\b\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u010b\b\u0013\u0001\u0014\u0001"+
		"\u0014\u0003\u0014\u010f\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u011f"+
		"\b\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0005"+
		"\u001a\u0126\b\u001a\n\u001a\f\u001a\u0129\t\u001a\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0005\u001b\u012e\b\u001b\n\u001b\f\u001b\u0131\t\u001b\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0005\u001c\u0136\b\u001c\n\u001c\f\u001c"+
		"\u0139\t\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0005\u001d\u013e\b"+
		"\u001d\n\u001d\f\u001d\u0141\t\u001d\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0005\u001e\u0146\b\u001e\n\u001e\f\u001e\u0149\t\u001e\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0003\u001f\u014e\b\u001f\u0001 \u0001 \u0001 \u0003"+
		" \u0153\b \u0001!\u0001!\u0005!\u0157\b!\n!\f!\u015a\t!\u0001\"\u0001"+
		"\"\u0003\"\u015e\b\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0003\"\u0167\b\"\u0001#\u0001#\u0001#\u0005#\u016c\b#\n#\f#\u016f"+
		"\t#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0001$\u0001$\u0001$\u0003$\u017f\b$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0001$\u0001$\u0001$\u0003$\u0189\b$\u0001$\u0003$\u018c\b$\u0001"+
		"$\u0000\u0000%\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFH\u0000\u0007\u0002\u0000"+
		"\u0014\u0017\u001b\u001b\u0002\u0000\u001c\u001c&+\u0002\u0000\u001e!"+
		"23\u0001\u0000,-\u0001\u0000.0\u0003\u0000$%,-11\u0001\u0000\u0014\u0017"+
		"\u01a9\u0000M\u0001\u0000\u0000\u0000\u0002W\u0001\u0000\u0000\u0000\u0004"+
		"Y\u0001\u0000\u0000\u0000\u0006h\u0001\u0000\u0000\u0000\bw\u0001\u0000"+
		"\u0000\u0000\n\u0080\u0001\u0000\u0000\u0000\f\u0099\u0001\u0000\u0000"+
		"\u0000\u000e\u009f\u0001\u0000\u0000\u0000\u0010\u00ac\u0001\u0000\u0000"+
		"\u0000\u0012\u00b1\u0001\u0000\u0000\u0000\u0014\u00b3\u0001\u0000\u0000"+
		"\u0000\u0016\u00b5\u0001\u0000\u0000\u0000\u0018\u00ca\u0001\u0000\u0000"+
		"\u0000\u001a\u00cc\u0001\u0000\u0000\u0000\u001c\u00d1\u0001\u0000\u0000"+
		"\u0000\u001e\u00e3\u0001\u0000\u0000\u0000 \u00e5\u0001\u0000\u0000\u0000"+
		"\"\u00f1\u0001\u0000\u0000\u0000$\u00f7\u0001\u0000\u0000\u0000&\u010a"+
		"\u0001\u0000\u0000\u0000(\u010c\u0001\u0000\u0000\u0000*\u0112\u0001\u0000"+
		"\u0000\u0000,\u0115\u0001\u0000\u0000\u0000.\u0118\u0001\u0000\u0000\u0000"+
		"0\u011a\u0001\u0000\u0000\u00002\u0120\u0001\u0000\u0000\u00004\u0122"+
		"\u0001\u0000\u0000\u00006\u012a\u0001\u0000\u0000\u00008\u0132\u0001\u0000"+
		"\u0000\u0000:\u013a\u0001\u0000\u0000\u0000<\u0142\u0001\u0000\u0000\u0000"+
		">\u014a\u0001\u0000\u0000\u0000@\u0152\u0001\u0000\u0000\u0000B\u0154"+
		"\u0001\u0000\u0000\u0000D\u0166\u0001\u0000\u0000\u0000F\u0168\u0001\u0000"+
		"\u0000\u0000H\u018b\u0001\u0000\u0000\u0000JL\u0003\u0002\u0001\u0000"+
		"KJ\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000"+
		"\u0000MN\u0001\u0000\u0000\u0000NP\u0001\u0000\u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000PQ\u0005\u0000\u0000\u0001Q\u0001\u0001\u0000\u0000\u0000"+
		"RX\u0003\u0004\u0002\u0000SX\u0003\u0006\u0003\u0000TX\u0003\f\u0006\u0000"+
		"UX\u0003\u0016\u000b\u0000VX\u0003,\u0016\u0000WR\u0001\u0000\u0000\u0000"+
		"WS\u0001\u0000\u0000\u0000WT\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000"+
		"\u0000WV\u0001\u0000\u0000\u0000X\u0003\u0001\u0000\u0000\u0000YZ\u0005"+
		"\u0001\u0000\u0000Z\\\u0003\u0014\n\u0000[]\u0003\b\u0004\u0000\\[\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000"+
		"^c\u0003\n\u0005\u0000_`\u0005;\u0000\u0000`b\u0003\n\u0005\u0000a_\u0001"+
		"\u0000\u0000\u0000be\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000"+
		"cd\u0001\u0000\u0000\u0000df\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000"+
		"\u0000fg\u0005:\u0000\u0000g\u0005\u0001\u0000\u0000\u0000hi\u0005\u0002"+
		"\u0000\u0000ik\u0003\u0014\n\u0000jl\u0003\b\u0004\u0000kj\u0001\u0000"+
		"\u0000\u0000kl\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mr\u0003"+
		"\n\u0005\u0000no\u0005;\u0000\u0000oq\u0003\n\u0005\u0000pn\u0001\u0000"+
		"\u0000\u0000qt\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000rs\u0001"+
		"\u0000\u0000\u0000su\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000"+
		"uv\u0005:\u0000\u0000v\u0007\u0001\u0000\u0000\u0000wx\u00058\u0000\u0000"+
		"xy\u0003.\u0017\u0000y~\u00059\u0000\u0000z{\u00058\u0000\u0000{|\u0003"+
		".\u0017\u0000|}\u00059\u0000\u0000}\u007f\u0001\u0000\u0000\u0000~z\u0001"+
		"\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\t\u0001\u0000"+
		"\u0000\u0000\u0080\u0085\u0005\u001b\u0000\u0000\u0081\u0082\u00058\u0000"+
		"\u0000\u0082\u0083\u0003.\u0017\u0000\u0083\u0084\u00059\u0000\u0000\u0084"+
		"\u0086\u0001\u0000\u0000\u0000\u0085\u0081\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0001\u0000\u0000\u0000\u0086\u0097\u0001\u0000\u0000\u0000\u0087"+
		"\u0095\u0005+\u0000\u0000\u0088\u0091\u00058\u0000\u0000\u0089\u008e\u0003"+
		".\u0017\u0000\u008a\u008b\u0005;\u0000\u0000\u008b\u008d\u0003.\u0017"+
		"\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008d\u0090\u0001\u0000\u0000"+
		"\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000"+
		"\u0000\u008f\u0092\u0001\u0000\u0000\u0000\u0090\u008e\u0001\u0000\u0000"+
		"\u0000\u0091\u0089\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000"+
		"\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0096\u00059\u0000\u0000"+
		"\u0094\u0096\u0003.\u0017\u0000\u0095\u0088\u0001\u0000\u0000\u0000\u0095"+
		"\u0094\u0001\u0000\u0000\u0000\u0096\u0098\u0001\u0000\u0000\u0000\u0097"+
		"\u0087\u0001\u0000\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098"+
		"\u000b\u0001\u0000\u0000\u0000\u0099\u009a\u0005\u0003\u0000\u0000\u009a"+
		"\u009b\u0003\u0012\t\u0000\u009b\u009c\u0005\u001b\u0000\u0000\u009c\u009d"+
		"\u0003\u000e\u0007\u0000\u009d\u009e\u0003\u001c\u000e\u0000\u009e\r\u0001"+
		"\u0000\u0000\u0000\u009f\u00a8\u00054\u0000\u0000\u00a0\u00a5\u0003\u0010"+
		"\b\u0000\u00a1\u00a2\u0005;\u0000\u0000\u00a2\u00a4\u0003\u0010\b\u0000"+
		"\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a4\u00a7\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000"+
		"\u00a8\u00a0\u0001\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000"+
		"\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u00ab\u00055\u0000\u0000\u00ab"+
		"\u000f\u0001\u0000\u0000\u0000\u00ac\u00ad\u0003\u0014\n\u0000\u00ad\u00ae"+
		"\u0005\u001b\u0000\u0000\u00ae\u0011\u0001\u0000\u0000\u0000\u00af\u00b2"+
		"\u0003\u0014\n\u0000\u00b0\u00b2\u0005\u0004\u0000\u0000\u00b1\u00af\u0001"+
		"\u0000\u0000\u0000\u00b1\u00b0\u0001\u0000\u0000\u0000\u00b2\u0013\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b4\u0007\u0000\u0000\u0000\u00b4\u0015\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b6\u0005\u000b\u0000\u0000\u00b6\u00b7\u0005"+
		"\u001b\u0000\u0000\u00b7\u00bb\u00056\u0000\u0000\u00b8\u00ba\u0003\u0018"+
		"\f\u0000\u00b9\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000"+
		"\u0000\u00bc\u00be\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000\u0000"+
		"\u0000\u00be\u00bf\u00057\u0000\u0000\u00bf\u0017\u0001\u0000\u0000\u0000"+
		"\u00c0\u00cb\u0003\u001a\r\u0000\u00c1\u00c2\u0003\u0012\t\u0000\u00c2"+
		"\u00c3\u0005\u001b\u0000\u0000\u00c3\u00c4\u0003\u000e\u0007\u0000\u00c4"+
		"\u00c5\u0003\u001c\u000e\u0000\u00c5\u00cb\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c7\u0003\u0014\n\u0000\u00c7\u00c8\u0005\u001b\u0000\u0000\u00c8\u00c9"+
		"\u0005:\u0000\u0000\u00c9\u00cb\u0001\u0000\u0000\u0000\u00ca\u00c0\u0001"+
		"\u0000\u0000\u0000\u00ca\u00c1\u0001\u0000\u0000\u0000\u00ca\u00c6\u0001"+
		"\u0000\u0000\u0000\u00cb\u0019\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005"+
		"\u001b\u0000\u0000\u00cd\u00ce\u0005\f\u0000\u0000\u00ce\u00cf\u0003\u000e"+
		"\u0007\u0000\u00cf\u00d0\u0003\u001c\u000e\u0000\u00d0\u001b\u0001\u0000"+
		"\u0000\u0000\u00d1\u00d5\u00056\u0000\u0000\u00d2\u00d4\u0003\u001e\u000f"+
		"\u0000\u00d3\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d7\u0001\u0000\u0000"+
		"\u0000\u00d5\u00d3\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000"+
		"\u0000\u00d6\u00d8\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001\u0000\u0000"+
		"\u0000\u00d8\u00d9\u00057\u0000\u0000\u00d9\u001d\u0001\u0000\u0000\u0000"+
		"\u00da\u00e4\u0003\u0004\u0002\u0000\u00db\u00e4\u0003\u0006\u0003\u0000"+
		"\u00dc\u00e4\u0003 \u0010\u0000\u00dd\u00e4\u0003\"\u0011\u0000\u00de"+
		"\u00e4\u0003$\u0012\u0000\u00df\u00e4\u0003(\u0014\u0000\u00e0\u00e4\u0003"+
		"*\u0015\u0000\u00e1\u00e4\u0003\u001c\u000e\u0000\u00e2\u00e4\u0003,\u0016"+
		"\u0000\u00e3\u00da\u0001\u0000\u0000\u0000\u00e3\u00db\u0001\u0000\u0000"+
		"\u0000\u00e3\u00dc\u0001\u0000\u0000\u0000\u00e3\u00dd\u0001\u0000\u0000"+
		"\u0000\u00e3\u00de\u0001\u0000\u0000\u0000\u00e3\u00df\u0001\u0000\u0000"+
		"\u0000\u00e3\u00e0\u0001\u0000\u0000\u0000\u00e3\u00e1\u0001\u0000\u0000"+
		"\u0000\u00e3\u00e2\u0001\u0000\u0000\u0000\u00e4\u001f\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e6\u0005\u0005\u0000\u0000\u00e6\u00e7\u00054\u0000\u0000"+
		"\u00e7\u00e8\u0003.\u0017\u0000\u00e8\u00e9\u00055\u0000\u0000\u00e9\u00ef"+
		"\u0003\u001c\u000e\u0000\u00ea\u00ed\u0005\u0006\u0000\u0000\u00eb\u00ee"+
		"\u0003\u001c\u000e\u0000\u00ec\u00ee\u0003 \u0010\u0000\u00ed\u00eb\u0001"+
		"\u0000\u0000\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ee\u00f0\u0001"+
		"\u0000\u0000\u0000\u00ef\u00ea\u0001\u0000\u0000\u0000\u00ef\u00f0\u0001"+
		"\u0000\u0000\u0000\u00f0!\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005\u0007"+
		"\u0000\u0000\u00f2\u00f3\u00054\u0000\u0000\u00f3\u00f4\u0003.\u0017\u0000"+
		"\u00f4\u00f5\u00055\u0000\u0000\u00f5\u00f6\u0003\u001c\u000e\u0000\u00f6"+
		"#\u0001\u0000\u0000\u0000\u00f7\u00f8\u0005\b\u0000\u0000\u00f8\u00f9"+
		"\u00054\u0000\u0000\u00f9\u00fb\u0003&\u0013\u0000\u00fa\u00fc\u0003."+
		"\u0017\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fb\u00fc\u0001\u0000"+
		"\u0000\u0000\u00fc\u00fd\u0001\u0000\u0000\u0000\u00fd\u00ff\u0005:\u0000"+
		"\u0000\u00fe\u0100\u0003.\u0017\u0000\u00ff\u00fe\u0001\u0000\u0000\u0000"+
		"\u00ff\u0100\u0001\u0000\u0000\u0000\u0100\u0101\u0001\u0000\u0000\u0000"+
		"\u0101\u0102\u00055\u0000\u0000\u0102\u0103\u0003\u001c\u000e\u0000\u0103"+
		"%\u0001\u0000\u0000\u0000\u0104\u010b\u0003\u0004\u0002\u0000\u0105\u010b"+
		"\u0003\u0006\u0003\u0000\u0106\u0107\u0003.\u0017\u0000\u0107\u0108\u0005"+
		":\u0000\u0000\u0108\u010b\u0001\u0000\u0000\u0000\u0109\u010b\u0005:\u0000"+
		"\u0000\u010a\u0104\u0001\u0000\u0000\u0000\u010a\u0105\u0001\u0000\u0000"+
		"\u0000\u010a\u0106\u0001\u0000\u0000\u0000\u010a\u0109\u0001\u0000\u0000"+
		"\u0000\u010b\'\u0001\u0000\u0000\u0000\u010c\u010e\u0005\n\u0000\u0000"+
		"\u010d\u010f\u0003.\u0017\u0000\u010e\u010d\u0001\u0000\u0000\u0000\u010e"+
		"\u010f\u0001\u0000\u0000\u0000\u010f\u0110\u0001\u0000\u0000\u0000\u0110"+
		"\u0111\u0005:\u0000\u0000\u0111)\u0001\u0000\u0000\u0000\u0112\u0113\u0005"+
		"\t\u0000\u0000\u0113\u0114\u0005:\u0000\u0000\u0114+\u0001\u0000\u0000"+
		"\u0000\u0115\u0116\u0003.\u0017\u0000\u0116\u0117\u0005:\u0000\u0000\u0117"+
		"-\u0001\u0000\u0000\u0000\u0118\u0119\u00030\u0018\u0000\u0119/\u0001"+
		"\u0000\u0000\u0000\u011a\u011e\u00034\u001a\u0000\u011b\u011c\u00032\u0019"+
		"\u0000\u011c\u011d\u00030\u0018\u0000\u011d\u011f\u0001\u0000\u0000\u0000"+
		"\u011e\u011b\u0001\u0000\u0000\u0000\u011e\u011f\u0001\u0000\u0000\u0000"+
		"\u011f1\u0001\u0000\u0000\u0000\u0120\u0121\u0007\u0001\u0000\u0000\u0121"+
		"3\u0001\u0000\u0000\u0000\u0122\u0127\u00036\u001b\u0000\u0123\u0124\u0005"+
		"#\u0000\u0000\u0124\u0126\u00036\u001b\u0000\u0125\u0123\u0001\u0000\u0000"+
		"\u0000\u0126\u0129\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000"+
		"\u0000\u0127\u0128\u0001\u0000\u0000\u0000\u01285\u0001\u0000\u0000\u0000"+
		"\u0129\u0127\u0001\u0000\u0000\u0000\u012a\u012f\u00038\u001c\u0000\u012b"+
		"\u012c\u0005\"\u0000\u0000\u012c\u012e\u00038\u001c\u0000\u012d\u012b"+
		"\u0001\u0000\u0000\u0000\u012e\u0131\u0001\u0000\u0000\u0000\u012f\u012d"+
		"\u0001\u0000\u0000\u0000\u012f\u0130\u0001\u0000\u0000\u0000\u01307\u0001"+
		"\u0000\u0000\u0000\u0131\u012f\u0001\u0000\u0000\u0000\u0132\u0137\u0003"+
		":\u001d\u0000\u0133\u0134\u0007\u0002\u0000\u0000\u0134\u0136\u0003:\u001d"+
		"\u0000\u0135\u0133\u0001\u0000\u0000\u0000\u0136\u0139\u0001\u0000\u0000"+
		"\u0000\u0137\u0135\u0001\u0000\u0000\u0000\u0137\u0138\u0001\u0000\u0000"+
		"\u0000\u01389\u0001\u0000\u0000\u0000\u0139\u0137\u0001\u0000\u0000\u0000"+
		"\u013a\u013f\u0003<\u001e\u0000\u013b\u013c\u0007\u0003\u0000\u0000\u013c"+
		"\u013e\u0003<\u001e\u0000\u013d\u013b\u0001\u0000\u0000\u0000\u013e\u0141"+
		"\u0001\u0000\u0000\u0000\u013f\u013d\u0001\u0000\u0000\u0000\u013f\u0140"+
		"\u0001\u0000\u0000\u0000\u0140;\u0001\u0000\u0000\u0000\u0141\u013f\u0001"+
		"\u0000\u0000\u0000\u0142\u0147\u0003>\u001f\u0000\u0143\u0144\u0007\u0004"+
		"\u0000\u0000\u0144\u0146\u0003>\u001f\u0000\u0145\u0143\u0001\u0000\u0000"+
		"\u0000\u0146\u0149\u0001\u0000\u0000\u0000\u0147\u0145\u0001\u0000\u0000"+
		"\u0000\u0147\u0148\u0001\u0000\u0000\u0000\u0148=\u0001\u0000\u0000\u0000"+
		"\u0149\u0147\u0001\u0000\u0000\u0000\u014a\u014d\u0003@ \u0000\u014b\u014c"+
		"\u0005\u001d\u0000\u0000\u014c\u014e\u0003>\u001f\u0000\u014d\u014b\u0001"+
		"\u0000\u0000\u0000\u014d\u014e\u0001\u0000\u0000\u0000\u014e?\u0001\u0000"+
		"\u0000\u0000\u014f\u0150\u0007\u0005\u0000\u0000\u0150\u0153\u0003@ \u0000"+
		"\u0151\u0153\u0003B!\u0000\u0152\u014f\u0001\u0000\u0000\u0000\u0152\u0151"+
		"\u0001\u0000\u0000\u0000\u0153A\u0001\u0000\u0000\u0000\u0154\u0158\u0003"+
		"H$\u0000\u0155\u0157\u0003D\"\u0000\u0156\u0155\u0001\u0000\u0000\u0000"+
		"\u0157\u015a\u0001\u0000\u0000\u0000\u0158\u0156\u0001\u0000\u0000\u0000"+
		"\u0158\u0159\u0001\u0000\u0000\u0000\u0159C\u0001\u0000\u0000\u0000\u015a"+
		"\u0158\u0001\u0000\u0000\u0000\u015b\u015d\u00054\u0000\u0000\u015c\u015e"+
		"\u0003F#\u0000\u015d\u015c\u0001\u0000\u0000\u0000\u015d\u015e\u0001\u0000"+
		"\u0000\u0000\u015e\u015f\u0001\u0000\u0000\u0000\u015f\u0167\u00055\u0000"+
		"\u0000\u0160\u0161\u00058\u0000\u0000\u0161\u0162\u0003.\u0017\u0000\u0162"+
		"\u0163\u00059\u0000\u0000\u0163\u0167\u0001\u0000\u0000\u0000\u0164\u0165"+
		"\u0005<\u0000\u0000\u0165\u0167\u0005\u001b\u0000\u0000\u0166\u015b\u0001"+
		"\u0000\u0000\u0000\u0166\u0160\u0001\u0000\u0000\u0000\u0166\u0164\u0001"+
		"\u0000\u0000\u0000\u0167E\u0001\u0000\u0000\u0000\u0168\u016d\u0003.\u0017"+
		"\u0000\u0169\u016a\u0005;\u0000\u0000\u016a\u016c\u0003.\u0017\u0000\u016b"+
		"\u0169\u0001\u0000\u0000\u0000\u016c\u016f\u0001\u0000\u0000\u0000\u016d"+
		"\u016b\u0001\u0000\u0000\u0000\u016d\u016e\u0001\u0000\u0000\u0000\u016e"+
		"G\u0001\u0000\u0000\u0000\u016f\u016d\u0001\u0000\u0000\u0000\u0170\u018c"+
		"\u0005\u0019\u0000\u0000\u0171\u018c\u0005\u0018\u0000\u0000\u0172\u018c"+
		"\u0005\u001a\u0000\u0000\u0173\u018c\u0005\u000f\u0000\u0000\u0174\u018c"+
		"\u0005\u0010\u0000\u0000\u0175\u018c\u0005\u0011\u0000\u0000\u0176\u018c"+
		"\u0005\u000e\u0000\u0000\u0177\u018c\u0005\u001b\u0000\u0000\u0178\u018c"+
		"\u0005\u0012\u0000\u0000\u0179\u018c\u0005\u0013\u0000\u0000\u017a\u017b"+
		"\u0005\r\u0000\u0000\u017b\u017c\u0005\u001b\u0000\u0000\u017c\u017e\u0005"+
		"4\u0000\u0000\u017d\u017f\u0003F#\u0000\u017e\u017d\u0001\u0000\u0000"+
		"\u0000\u017e\u017f\u0001\u0000\u0000\u0000\u017f\u0180\u0001\u0000\u0000"+
		"\u0000\u0180\u018c\u00055\u0000\u0000\u0181\u0182\u00054\u0000\u0000\u0182"+
		"\u0183\u0003.\u0017\u0000\u0183\u0184\u00055\u0000\u0000\u0184\u018c\u0001"+
		"\u0000\u0000\u0000\u0185\u0186\u0007\u0006\u0000\u0000\u0186\u0188\u0005"+
		"4\u0000\u0000\u0187\u0189\u0003F#\u0000\u0188\u0187\u0001\u0000\u0000"+
		"\u0000\u0188\u0189\u0001\u0000\u0000\u0000\u0189\u018a\u0001\u0000\u0000"+
		"\u0000\u018a\u018c\u00055\u0000\u0000\u018b\u0170\u0001\u0000\u0000\u0000"+
		"\u018b\u0171\u0001\u0000\u0000\u0000\u018b\u0172\u0001\u0000\u0000\u0000"+
		"\u018b\u0173\u0001\u0000\u0000\u0000\u018b\u0174\u0001\u0000\u0000\u0000"+
		"\u018b\u0175\u0001\u0000\u0000\u0000\u018b\u0176\u0001\u0000\u0000\u0000"+
		"\u018b\u0177\u0001\u0000\u0000\u0000\u018b\u0178\u0001\u0000\u0000\u0000"+
		"\u018b\u0179\u0001\u0000\u0000\u0000\u018b\u017a\u0001\u0000\u0000\u0000"+
		"\u018b\u0181\u0001\u0000\u0000\u0000\u018b\u0185\u0001\u0000\u0000\u0000"+
		"\u018cI\u0001\u0000\u0000\u0000(MW\\ckr~\u0085\u008e\u0091\u0095\u0097"+
		"\u00a5\u00a8\u00b1\u00bb\u00ca\u00d5\u00e3\u00ed\u00ef\u00fb\u00ff\u010a"+
		"\u010e\u011e\u0127\u012f\u0137\u013f\u0147\u014d\u0152\u0158\u015d\u0166"+
		"\u016d\u017e\u0188\u018b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}