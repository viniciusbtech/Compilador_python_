; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

declare i64 @"strlen"(i8* %".1")

declare i8* @"strcpy"(i8* %".1", i8* %".2")

declare i8* @"strcat"(i8* %".1", i8* %".2")

declare i32 @"SetConsoleOutputCP"(i32 %".1")

@"x" = internal global i32 10
@"y" = internal global i32 20
@"nome" = internal global i8* getelementptr ([5 x i8], [5 x i8]* @"str", i32 0, i32 0)
@"str" = private constant [5 x i8] c"Joao\00"
@"idade" = internal global i32 25
@"saudacao" = internal global i8* null
@"parte1" = internal global i8* getelementptr ([6 x i8], [6 x i8]* @"str.1", i32 0, i32 0)
@"str.1" = private constant [6 x i8] c"Hello\00"
@"parte2" = internal global i8* getelementptr ([6 x i8], [6 x i8]* @"str.2", i32 0, i32 0)
@"str.2" = private constant [6 x i8] c"World\00"
@"completo" = internal global i8* null
@"msg" = internal global i8* null
@"a" = internal global i32 0
@"b" = internal global i32 0
@"c" = internal global i32 0
@"nome1" = internal global i8* null
@"nome2" = internal global i8* null
@"valor_int" = internal global i32 42
@"valor_real" = internal global double              0.000000e+00
@"pi" = internal global double 0x40091eb851eb851f
@"pi_int" = internal global i32 0
@"num_str" = internal global i8* null
@"zero" = internal global i32 0
@"nao_zero" = internal global i32 5
@"falso" = internal global i1 0
@"verdadeiro" = internal global i1 0
@"result" = internal global i32 0
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.3", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.4", i32 0, i32 0
  %"strptr.2" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.5", i32 0, i32 0
  %"strptr.3" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.6", i32 0, i32 0
  %"strptr.4" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.7", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.4", i8* %"strptr", i8* %"strptr.1", i8* %"strptr.2", i8* %"strptr.3")
  %"strptr.5" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.8", i32 0, i32 0
  %"x" = load i32, i32* @"x"
  %"strptr.6" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.9", i32 0, i32 0
  %"y" = load i32, i32* @"y"
  %"strptr.7" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.10", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.5", i32 %"x", i8* %"strptr.6", i32 %"y")
  %"strptr.8" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.11", i32 0, i32 0
  %"nome" = load i8*, i8** @"nome"
  %"strptr.9" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.12", i32 0, i32 0
  %"idade" = load i32, i32* @"idade"
  %"strptr.10" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.13", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.10", i8* %"strptr.8", i8* %"nome", i8* %"strptr.9", i32 %"idade")
  %"strptr.11" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.14", i32 0, i32 0
  %"strptr.12" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.15", i32 0, i32 0
  %"slen1" = call i64 @"strlen"(i8* %"strptr.11")
  %"slen2" = call i64 @"strlen"(i8* %"strptr.12")
  %".5" = add i64 %"slen1", %"slen2"
  %"slen_total" = add i64 %".5", 1
  %"sbuf" = call i8* @"malloc"(i64 %"slen_total")
  %".6" = call i8* @"strcpy"(i8* %"sbuf", i8* %"strptr.11")
  %".7" = call i8* @"strcat"(i8* %"sbuf", i8* %"strptr.12")
  store i8* %"sbuf", i8** @"saudacao"
  %"saudacao" = load i8*, i8** @"saudacao"
  %"strptr.13" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.16", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %"strptr.13", i8* %"saudacao")
  %"parte1" = load i8*, i8** @"parte1"
  %"strptr.14" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.17", i32 0, i32 0
  %"slen1.1" = call i64 @"strlen"(i8* %"parte1")
  %"slen2.1" = call i64 @"strlen"(i8* %"strptr.14")
  %".10" = add i64 %"slen1.1", %"slen2.1"
  %"slen_total.1" = add i64 %".10", 1
  %"sbuf.1" = call i8* @"malloc"(i64 %"slen_total.1")
  %".11" = call i8* @"strcpy"(i8* %"sbuf.1", i8* %"parte1")
  %".12" = call i8* @"strcat"(i8* %"sbuf.1", i8* %"strptr.14")
  %"parte2" = load i8*, i8** @"parte2"
  %"slen1.2" = call i64 @"strlen"(i8* %"sbuf.1")
  %"slen2.2" = call i64 @"strlen"(i8* %"parte2")
  %".13" = add i64 %"slen1.2", %"slen2.2"
  %"slen_total.2" = add i64 %".13", 1
  %"sbuf.2" = call i8* @"malloc"(i64 %"slen_total.2")
  %".14" = call i8* @"strcpy"(i8* %"sbuf.2", i8* %"sbuf.1")
  %".15" = call i8* @"strcat"(i8* %"sbuf.2", i8* %"parte2")
  store i8* %"sbuf.2", i8** @"completo"
  %"completo" = load i8*, i8** @"completo"
  %"strptr.15" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.18", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %"strptr.15", i8* %"completo")
  %"strptr.16" = getelementptr inbounds [19 x i8], [19 x i8]* @"str.19", i32 0, i32 0
  store i8* %"strptr.16", i8** @"msg"
  %"msg" = load i8*, i8** @"msg"
  %"strptr.17" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.20", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %"strptr.17", i8* %"msg", i32 8)
  %"strptr.18" = getelementptr inbounds [21 x i8], [21 x i8]* @"str.21", i32 0, i32 0
  %"strptr.19" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.22", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %"strptr.19", i8* %"strptr.18")
  %"strptr.20" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.23", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.20", i32* @"a")
  %"strptr.21" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.24", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.21", i32* @"b")
  %"strptr.22" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.25", i32 0, i32 0
  %".23" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.22", i32* @"c")
  %"strptr.23" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.26", i32 0, i32 0
  %"a" = load i32, i32* @"a"
  %"b" = load i32, i32* @"b"
  %"c" = load i32, i32* @"c"
  %"strptr.24" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.27", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %"strptr.24", i8* %"strptr.23", i32 %"a", i32 %"b", i32 %"c")
  %"strptr.25" = getelementptr inbounds [19 x i8], [19 x i8]* @"str.28", i32 0, i32 0
  %"strptr.26" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.29", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %"strptr.26", i8* %"strptr.25")
  %"strptr.27" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.30", i32 0, i32 0
  %"input_buf" = call i8* @"malloc"(i64 256)
  store i8* %"input_buf", i8** @"nome1"
  %".27" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.27", i8* %"input_buf")
  %"strptr.28" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.31", i32 0, i32 0
  %"input_buf.1" = call i8* @"malloc"(i64 256)
  store i8* %"input_buf.1", i8** @"nome2"
  %".29" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.28", i8* %"input_buf.1")
  %"strptr.29" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.32", i32 0, i32 0
  %"nome1" = load i8*, i8** @"nome1"
  %"strptr.30" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.33", i32 0, i32 0
  %"nome2" = load i8*, i8** @"nome2"
  %"strptr.31" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.34", i32 0, i32 0
  %".30" = call i32 (i8*, ...) @"printf"(i8* %"strptr.31", i8* %"strptr.29", i8* %"nome1", i8* %"strptr.30", i8* %"nome2")
  %"valor_int" = load i32, i32* @"valor_int"
  %".31" = sitofp i32 %"valor_int" to double
  store double %".31", double* @"valor_real"
  %"strptr.32" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.35", i32 0, i32 0
  %"valor_int.1" = load i32, i32* @"valor_int"
  %"strptr.33" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.36", i32 0, i32 0
  %"valor_real" = load double, double* @"valor_real"
  %"strptr.34" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.37", i32 0, i32 0
  %".33" = call i32 (i8*, ...) @"printf"(i8* %"strptr.34", i8* %"strptr.32", i32 %"valor_int.1", i8* %"strptr.33", double %"valor_real")
  %"pi" = load double, double* @"pi"
  %".34" = fptosi double %"pi" to i32
  store i32 %".34", i32* @"pi_int"
  %"strptr.35" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.38", i32 0, i32 0
  %"pi.1" = load double, double* @"pi"
  %"strptr.36" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.39", i32 0, i32 0
  %"pi_int" = load i32, i32* @"pi_int"
  %"strptr.37" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.40", i32 0, i32 0
  %".36" = call i32 (i8*, ...) @"printf"(i8* %"strptr.37", i8* %"strptr.35", double %"pi.1", i8* %"strptr.36", i32 %"pi_int")
  %"valor_int.2" = load i32, i32* @"valor_int"
  %"str_buf" = call i8* @"malloc"(i64 64)
  %"strptr.38" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.41", i32 0, i32 0
  %".37" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %"str_buf", i8* %"strptr.38", i32 %"valor_int.2")
  store i8* %"str_buf", i8** @"num_str"
  %"strptr.39" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.42", i32 0, i32 0
  %"num_str" = load i8*, i8** @"num_str"
  %"strptr.40" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.43", i32 0, i32 0
  %".39" = call i32 (i8*, ...) @"printf"(i8* %"strptr.40", i8* %"strptr.39", i8* %"num_str")
  %"zero" = load i32, i32* @"zero"
  %".40" = icmp ne i32 %"zero", 0
  store i1 %".40", i1* @"falso"
  %"nao_zero" = load i32, i32* @"nao_zero"
  %".42" = icmp ne i32 %"nao_zero", 0
  store i1 %".42", i1* @"verdadeiro"
  %"strptr.41" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.44", i32 0, i32 0
  %"falso" = load i1, i1* @"falso"
  %"strptr.42" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.45", i32 0, i32 0
  %"strptr.43" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.46", i32 0, i32 0
  %".44" = select  i1 %"falso", i8* %"strptr.42", i8* %"strptr.43"
  %"verdadeiro" = load i1, i1* @"verdadeiro"
  %"strptr.44" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.47", i32 0, i32 0
  %"strptr.45" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.48", i32 0, i32 0
  %".45" = select  i1 %"verdadeiro", i8* %"strptr.44", i8* %"strptr.45"
  %"strptr.46" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.49", i32 0, i32 0
  %".46" = call i32 (i8*, ...) @"printf"(i8* %"strptr.46", i8* %"strptr.41", i8* %".44", i8* %".45")
  %".47" = fadd double 0x4016000000000000, 0x4012000000000000
  %".48" = fptosi double %".47" to i32
  store i32 %".48", i32* @"result"
  %"strptr.47" = getelementptr inbounds [16 x i8], [16 x i8]* @"str.50", i32 0, i32 0
  %"result" = load i32, i32* @"result"
  %"strptr.48" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.51", i32 0, i32 0
  %".50" = call i32 (i8*, ...) @"printf"(i8* %"strptr.48", i8* %"strptr.47", i32 %"result")
  ret void
}

@"str.3" = private constant [4 x i8] c"Ola\00"
@"str.4" = private constant [2 x i8] c" \00"
@"str.5" = private constant [6 x i8] c"Mundo\00"
@"str.6" = private constant [2 x i8] c"!\00"
@"str.7" = private constant [13 x i8] c"%s %s %s %s\0a\00"
@"str.8" = private constant [4 x i8] c"x =\00"
@"str.9" = private constant [6 x i8] c", y =\00"
@"str.10" = private constant [13 x i8] c"%s %d %s %d\0a\00"
@"str.11" = private constant [6 x i8] c"Nome:\00"
@"str.12" = private constant [7 x i8] c"Idade:\00"
@"str.13" = private constant [13 x i8] c"%s %s %s %d\0a\00"
@"str.14" = private constant [5 x i8] c"Ola \00"
@"str.15" = private constant [6 x i8] c"Mundo\00"
@"str.16" = private constant [4 x i8] c"%s\0a\00"
@"str.17" = private constant [2 x i8] c" \00"
@"str.18" = private constant [4 x i8] c"%s\0a\00"
@"str.19" = private constant [19 x i8] c"A soma de 5 e 3 e \00"
@"str.20" = private constant [7 x i8] c"%s %d\0a\00"
@"str.21" = private constant [21 x i8] c"Digite tres numeros:\00"
@"str.22" = private constant [4 x i8] c"%s\0a\00"
@"str.23" = private constant [3 x i8] c"%d\00"
@"str.24" = private constant [3 x i8] c"%d\00"
@"str.25" = private constant [3 x i8] c"%d\00"
@"str.26" = private constant [14 x i8] c"Voce digitou:\00"
@"str.27" = private constant [13 x i8] c"%s %d %d %d\0a\00"
@"str.28" = private constant [19 x i8] c"Digite dois nomes:\00"
@"str.29" = private constant [4 x i8] c"%s\0a\00"
@"str.30" = private constant [3 x i8] c"%s\00"
@"str.31" = private constant [3 x i8] c"%s\00"
@"str.32" = private constant [7 x i8] c"Nomes:\00"
@"str.33" = private constant [2 x i8] c"e\00"
@"str.34" = private constant [13 x i8] c"%s %s %s %s\0a\00"
@"str.35" = private constant [11 x i8] c"Int->Real:\00"
@"str.36" = private constant [3 x i8] c"->\00"
@"str.37" = private constant [13 x i8] c"%s %d %s %f\0a\00"
@"str.38" = private constant [11 x i8] c"Real->Int:\00"
@"str.39" = private constant [3 x i8] c"->\00"
@"str.40" = private constant [13 x i8] c"%s %f %s %d\0a\00"
@"str.41" = private constant [3 x i8] c"%d\00"
@"str.42" = private constant [13 x i8] c"Int->String:\00"
@"str.43" = private constant [7 x i8] c"%s %s\0a\00"
@"str.44" = private constant [11 x i8] c"Int->Bool:\00"
@"str.45" = private constant [5 x i8] c"true\00"
@"str.46" = private constant [6 x i8] c"false\00"
@"str.47" = private constant [5 x i8] c"true\00"
@"str.48" = private constant [6 x i8] c"false\00"
@"str.49" = private constant [10 x i8] c"%s %s %s\0a\00"
@"str.50" = private constant [16 x i8] c"Cast expressao:\00"
@"str.51" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  %".2" = call i32 @"SetConsoleOutputCP"(i32 65001)
  call void @"__jss_global_init"()
  ret i32 0
}
