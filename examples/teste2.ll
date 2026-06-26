; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"n1" = internal global i32 10
@"n2" = internal global i32 5
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [7 x i8], [7 x i8]* @"str", i32 0, i32 0
  %"n1" = load i32, i32* @"n1"
  %"n2" = load i32, i32* @"n2"
  %".2" = icmp sgt i32 %"n1", %"n2"
  %"strptr.1" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.1", i32 0, i32 0
  %"strptr.2" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.2", i32 0, i32 0
  %".3" = select  i1 %".2", i8* %"strptr.1", i8* %"strptr.2"
  %"strptr.3" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.3", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i8* %"strptr", i8* %".3")
  %"strptr.4" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.4", i32 0, i32 0
  %"n1.1" = load i32, i32* @"n1"
  %"n2.1" = load i32, i32* @"n2"
  %".5" = icmp slt i32 %"n1.1", %"n2.1"
  %"strptr.5" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.5", i32 0, i32 0
  %"strptr.6" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.6", i32 0, i32 0
  %".6" = select  i1 %".5", i8* %"strptr.5", i8* %"strptr.6"
  %"strptr.7" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.7", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.4", i8* %".6")
  %"strptr.8" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.8", i32 0, i32 0
  %"n1.2" = load i32, i32* @"n1"
  %"n2.2" = load i32, i32* @"n2"
  %".8" = icmp eq i32 %"n1.2", %"n2.2"
  %"strptr.9" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.9", i32 0, i32 0
  %"strptr.10" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.10", i32 0, i32 0
  %".9" = select  i1 %".8", i8* %"strptr.9", i8* %"strptr.10"
  %"strptr.11" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.11", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %"strptr.11", i8* %"strptr.8", i8* %".9")
  %"strptr.12" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.12", i32 0, i32 0
  %"n1.3" = load i32, i32* @"n1"
  %"n2.3" = load i32, i32* @"n2"
  %".11" = icmp ne i32 %"n1.3", %"n2.3"
  %"strptr.13" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.13", i32 0, i32 0
  %"strptr.14" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.14", i32 0, i32 0
  %".12" = select  i1 %".11", i8* %"strptr.13", i8* %"strptr.14"
  %"strptr.15" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.15", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %"strptr.15", i8* %"strptr.12", i8* %".12")
  %"strptr.16" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.16", i32 0, i32 0
  %"n1.4" = load i32, i32* @"n1"
  %"n2.4" = load i32, i32* @"n2"
  %".14" = icmp sge i32 %"n1.4", %"n2.4"
  %"strptr.17" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.17", i32 0, i32 0
  %"strptr.18" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.18", i32 0, i32 0
  %".15" = select  i1 %".14", i8* %"strptr.17", i8* %"strptr.18"
  %"strptr.19" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.19", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"strptr.19", i8* %"strptr.16", i8* %".15")
  %"strptr.20" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.20", i32 0, i32 0
  %"n1.5" = load i32, i32* @"n1"
  %"n2.5" = load i32, i32* @"n2"
  %".17" = icmp sle i32 %"n1.5", %"n2.5"
  %"strptr.21" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.21", i32 0, i32 0
  %"strptr.22" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.22", i32 0, i32 0
  %".18" = select  i1 %".17", i8* %"strptr.21", i8* %"strptr.22"
  %"strptr.23" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.23", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %"strptr.23", i8* %"strptr.20", i8* %".18")
  ret void
}

@"str" = private constant [7 x i8] c"Maior:\00"
@"str.1" = private constant [5 x i8] c"true\00"
@"str.2" = private constant [6 x i8] c"false\00"
@"str.3" = private constant [7 x i8] c"%s %s\0a\00"
@"str.4" = private constant [7 x i8] c"Menor:\00"
@"str.5" = private constant [5 x i8] c"true\00"
@"str.6" = private constant [6 x i8] c"false\00"
@"str.7" = private constant [7 x i8] c"%s %s\0a\00"
@"str.8" = private constant [7 x i8] c"Igual:\00"
@"str.9" = private constant [5 x i8] c"true\00"
@"str.10" = private constant [6 x i8] c"false\00"
@"str.11" = private constant [7 x i8] c"%s %s\0a\00"
@"str.12" = private constant [11 x i8] c"Diferente:\00"
@"str.13" = private constant [5 x i8] c"true\00"
@"str.14" = private constant [6 x i8] c"false\00"
@"str.15" = private constant [7 x i8] c"%s %s\0a\00"
@"str.16" = private constant [12 x i8] c"MaiorIgual:\00"
@"str.17" = private constant [5 x i8] c"true\00"
@"str.18" = private constant [6 x i8] c"false\00"
@"str.19" = private constant [7 x i8] c"%s %s\0a\00"
@"str.20" = private constant [12 x i8] c"MenorIgual:\00"
@"str.21" = private constant [5 x i8] c"true\00"
@"str.22" = private constant [6 x i8] c"false\00"
@"str.23" = private constant [7 x i8] c"%s %s\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
