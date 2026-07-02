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
@"y" = internal global double 0x40091eb851eb851f
@"nome" = internal global i8* getelementptr ([5 x i8], [5 x i8]* @"str", i32 0, i32 0)
@"str" = private constant [5 x i8] c"Joao\00"
@"ativo" = internal global i1 1
@"a" = internal global i32 0
@"b" = internal global i32 0
@"c" = internal global i32 0
@"MAX" = internal global i32 100
@"PI" = internal global double 0x400921f9f01b866e
@"MSG" = internal global i8* getelementptr ([10 x i8], [10 x i8]* @"str.1", i32 0, i32 0)
@"str.1" = private constant [10 x i8] c"Constante\00"
@"numeros" = internal global [5 x i32] zeroinitializer
@"matriz" = internal global [3 x [3 x i32]] zeroinitializer
@"arr" = internal global [3 x i32] zeroinitializer
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.2", i32 0, i32 0
  %"x" = load i32, i32* @"x"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.3", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", i32 %"x")
  %"strptr.2" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.4", i32 0, i32 0
  %"y" = load double, double* @"y"
  %"strptr.3" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.5", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i8* %"strptr.2", double %"y")
  %"strptr.4" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.6", i32 0, i32 0
  %"nome" = load i8*, i8** @"nome"
  %"strptr.5" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.7", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.5", i8* %"strptr.4", i8* %"nome")
  %"strptr.6" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.8", i32 0, i32 0
  %"ativo" = load i1, i1* @"ativo"
  %"strptr.7" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.9", i32 0, i32 0
  %"strptr.8" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.10", i32 0, i32 0
  %".5" = select  i1 %"ativo", i8* %"strptr.7", i8* %"strptr.8"
  %"strptr.9" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.11", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"strptr.9", i8* %"strptr.6", i8* %".5")
  store i32 5, i32* @"a"
  store i32 10, i32* @"b"
  %"a" = load i32, i32* @"a"
  %"b" = load i32, i32* @"b"
  %".9" = add i32 %"a", %"b"
  store i32 %".9", i32* @"c"
  %"strptr.10" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.12", i32 0, i32 0
  %"c" = load i32, i32* @"c"
  %"strptr.11" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.13", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %"strptr.11", i8* %"strptr.10", i32 %"c")
  %"strptr.12" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.14", i32 0, i32 0
  %"MAX" = load i32, i32* @"MAX"
  %"PI" = load double, double* @"PI"
  %"MSG" = load i8*, i8** @"MSG"
  %"strptr.13" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.15", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.13", i8* %"strptr.12", i32 %"MAX", double %"PI", i8* %"MSG")
  %".13" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 0
  store i32 10, i32* %".13"
  %".15" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 1
  store i32 20, i32* %".15"
  %".17" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 2
  store i32 30, i32* %".17"
  %".19" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 3
  store i32 40, i32* %".19"
  %".21" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 4
  store i32 50, i32* %".21"
  %"strptr.14" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.16", i32 0, i32 0
  %".23" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 0
  %".24" = load i32, i32* %".23"
  %"strptr.15" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.17", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %"strptr.15", i8* %"strptr.14", i32 %".24")
  %"strptr.16" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.18", i32 0, i32 0
  %".26" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 4
  %".27" = load i32, i32* %".26"
  %"strptr.17" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.19", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %"strptr.17", i8* %"strptr.16", i32 %".27")
  %".29" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 0, i32 0
  store i32 1, i32* %".29"
  %".31" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 0, i32 1
  store i32 2, i32* %".31"
  %".33" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 0, i32 2
  store i32 3, i32* %".33"
  %".35" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 1, i32 0
  store i32 4, i32* %".35"
  %".37" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 1, i32 1
  store i32 5, i32* %".37"
  %".39" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 1, i32 2
  store i32 6, i32* %".39"
  %".41" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 2, i32 0
  store i32 7, i32* %".41"
  %".43" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 2, i32 1
  store i32 8, i32* %".43"
  %".45" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 2, i32 2
  store i32 9, i32* %".45"
  %"strptr.18" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.20", i32 0, i32 0
  %".47" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* @"matriz", i32 0, i32 1, i32 1
  %".48" = load i32, i32* %".47"
  %"strptr.19" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.21", i32 0, i32 0
  %".49" = call i32 (i8*, ...) @"printf"(i8* %"strptr.19", i8* %"strptr.18", i32 %".48")
  %".50" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 0
  store i32 10, i32* %".50"
  %".52" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 0
  %".53" = load i32, i32* %".52"
  %".54" = add i32 %".53", 5
  %".55" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 0
  store i32 %".54", i32* %".55"
  %"strptr.20" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.22", i32 0, i32 0
  %".57" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 0
  %".58" = load i32, i32* %".57"
  %"strptr.21" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.23", i32 0, i32 0
  %".59" = call i32 (i8*, ...) @"printf"(i8* %"strptr.21", i8* %"strptr.20", i32 %".58")
  %".60" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 1
  store i32 20, i32* %".60"
  %".62" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 1
  %".63" = load i32, i32* %".62"
  %".64" = mul i32 %".63", 2
  %".65" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 1
  store i32 %".64", i32* %".65"
  %"strptr.22" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.24", i32 0, i32 0
  %".67" = getelementptr inbounds [3 x i32], [3 x i32]* @"arr", i32 0, i32 1
  %".68" = load i32, i32* %".67"
  %"strptr.23" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.25", i32 0, i32 0
  %".69" = call i32 (i8*, ...) @"printf"(i8* %"strptr.23", i8* %"strptr.22", i32 %".68")
  ret void
}

@"str.2" = private constant [5 x i8] c"Int:\00"
@"str.3" = private constant [7 x i8] c"%s %d\0a\00"
@"str.4" = private constant [6 x i8] c"Real:\00"
@"str.5" = private constant [7 x i8] c"%s %f\0a\00"
@"str.6" = private constant [8 x i8] c"String:\00"
@"str.7" = private constant [7 x i8] c"%s %s\0a\00"
@"str.8" = private constant [6 x i8] c"Bool:\00"
@"str.9" = private constant [5 x i8] c"true\00"
@"str.10" = private constant [6 x i8] c"false\00"
@"str.11" = private constant [7 x i8] c"%s %s\0a\00"
@"str.12" = private constant [6 x i8] c"Soma:\00"
@"str.13" = private constant [7 x i8] c"%s %d\0a\00"
@"str.14" = private constant [12 x i8] c"Constantes:\00"
@"str.15" = private constant [13 x i8] c"%s %d %f %s\0a\00"
@"str.16" = private constant [10 x i8] c"Array[0]:\00"
@"str.17" = private constant [7 x i8] c"%s %d\0a\00"
@"str.18" = private constant [10 x i8] c"Array[4]:\00"
@"str.19" = private constant [7 x i8] c"%s %d\0a\00"
@"str.20" = private constant [14 x i8] c"Matriz[1][1]:\00"
@"str.21" = private constant [7 x i8] c"%s %d\0a\00"
@"str.22" = private constant [14 x i8] c"Array com +=:\00"
@"str.23" = private constant [7 x i8] c"%s %d\0a\00"
@"str.24" = private constant [14 x i8] c"Array com *=:\00"
@"str.25" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  %".2" = call i32 @"SetConsoleOutputCP"(i32 65001)
  call void @"__jss_global_init"()
  ret i32 0
}
