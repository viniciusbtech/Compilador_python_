; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"x" = internal global i32 10
@"y" = internal global i32 20
@"nome" = internal global i8* getelementptr ([5 x i8], [5 x i8]* @"str", i32 0, i32 0)
@"str" = private constant [5 x i8] c"Joao\00"
@"idade" = internal global i32 25
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.2", i32 0, i32 0
  %"strptr.2" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.3", i32 0, i32 0
  %"strptr.3" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.4", i32 0, i32 0
  %"strptr.4" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.5", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.4", i8* %"strptr", i8* %"strptr.1", i8* %"strptr.2", i8* %"strptr.3")
  %"strptr.5" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.6", i32 0, i32 0
  %"x" = load i32, i32* @"x"
  %"strptr.6" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.7", i32 0, i32 0
  %"y" = load i32, i32* @"y"
  %"strptr.7" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.8", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.5", i32 %"x", i8* %"strptr.6", i32 %"y")
  %"strptr.8" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.9", i32 0, i32 0
  %"nome" = load i8*, i8** @"nome"
  %"strptr.9" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.10", i32 0, i32 0
  %"idade" = load i32, i32* @"idade"
  %"strptr.10" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.11", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.10", i8* %"strptr.8", i8* %"nome", i8* %"strptr.9", i32 %"idade")
  ret void
}

@"str.1" = private constant [4 x i8] c"Ola\00"
@"str.2" = private constant [2 x i8] c" \00"
@"str.3" = private constant [6 x i8] c"Mundo\00"
@"str.4" = private constant [2 x i8] c"!\00"
@"str.5" = private constant [13 x i8] c"%s %s %s %s\0a\00"
@"str.6" = private constant [4 x i8] c"x =\00"
@"str.7" = private constant [6 x i8] c", y =\00"
@"str.8" = private constant [13 x i8] c"%s %d %s %d\0a\00"
@"str.9" = private constant [6 x i8] c"Nome:\00"
@"str.10" = private constant [7 x i8] c"Idade:\00"
@"str.11" = private constant [13 x i8] c"%s %s %s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
