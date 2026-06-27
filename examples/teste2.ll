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

@"a" = internal global i32 0
@"b" = internal global i32 0
@"c" = internal global i32 0
@"nome1" = internal global i8* null
@"nome2" = internal global i8* null
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [21 x i8], [21 x i8]* @"str", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr")
  %"strptr.2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.2", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.2", i32* @"a")
  %"strptr.3" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.3", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.3", i32* @"b")
  %"strptr.4" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.4", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.4", i32* @"c")
  %"strptr.5" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.5", i32 0, i32 0
  %"a" = load i32, i32* @"a"
  %"b" = load i32, i32* @"b"
  %"c" = load i32, i32* @"c"
  %"strptr.6" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.6", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"strptr.6", i8* %"strptr.5", i32 %"a", i32 %"b", i32 %"c")
  %"strptr.7" = getelementptr inbounds [19 x i8], [19 x i8]* @"str.7", i32 0, i32 0
  %"strptr.8" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.8", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"strptr.8", i8* %"strptr.7")
  %"strptr.9" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.9", i32 0, i32 0
  %"input_buf" = call i8* @"malloc"(i64 256)
  store i8* %"input_buf", i8** @"nome1"
  %".9" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.9", i8* %"input_buf")
  %"strptr.10" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.10", i32 0, i32 0
  %"input_buf.1" = call i8* @"malloc"(i64 256)
  store i8* %"input_buf.1", i8** @"nome2"
  %".11" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.10", i8* %"input_buf.1")
  %"strptr.11" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.11", i32 0, i32 0
  %"nome1" = load i8*, i8** @"nome1"
  %"strptr.12" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.12", i32 0, i32 0
  %"nome2" = load i8*, i8** @"nome2"
  %"strptr.13" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.13", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.13", i8* %"strptr.11", i8* %"nome1", i8* %"strptr.12", i8* %"nome2")
  ret void
}

@"str" = private constant [21 x i8] c"Digite tres numeros:\00"
@"str.1" = private constant [4 x i8] c"%s\0a\00"
@"str.2" = private constant [3 x i8] c"%d\00"
@"str.3" = private constant [3 x i8] c"%d\00"
@"str.4" = private constant [3 x i8] c"%d\00"
@"str.5" = private constant [14 x i8] c"Voce digitou:\00"
@"str.6" = private constant [13 x i8] c"%s %d %d %d\0a\00"
@"str.7" = private constant [19 x i8] c"Digite dois nomes:\00"
@"str.8" = private constant [4 x i8] c"%s\0a\00"
@"str.9" = private constant [3 x i8] c"%s\00"
@"str.10" = private constant [3 x i8] c"%s\00"
@"str.11" = private constant [7 x i8] c"Nomes:\00"
@"str.12" = private constant [2 x i8] c"e\00"
@"str.13" = private constant [13 x i8] c"%s %s %s %s\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
