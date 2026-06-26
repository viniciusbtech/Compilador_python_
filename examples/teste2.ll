; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"saudacao" = internal global i8* null
@"parte1" = internal global i8* getelementptr ([6 x i8], [6 x i8]* @"str", i32 0, i32 0)
@"str" = private constant [6 x i8] c"Hello\00"
@"parte2" = internal global i8* getelementptr ([6 x i8], [6 x i8]* @"str.1", i32 0, i32 0)
@"str.1" = private constant [6 x i8] c"World\00"
@"completo" = internal global i8* null
@"msg" = internal global i8* null
define void @"__jss_global_init"()
{
entry:
  %"saudacao" = load i8*, i8** @"saudacao"
  %"strptr" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.2", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr", i8* %"saudacao")
  %"completo" = load i8*, i8** @"completo"
  %"strptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.3", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"completo")
  %"msg" = load i8*, i8** @"msg"
  %"strptr.2" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.4", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.2", i8* %"msg", i32 8)
  ret void
}

@"str.2" = private constant [4 x i8] c"%s\0a\00"
@"str.3" = private constant [4 x i8] c"%s\0a\00"
@"str.4" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
