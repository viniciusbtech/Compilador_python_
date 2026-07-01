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

@"a" = internal global i32 0
@"b" = internal global i32 0
@"c" = internal global i32 0
@"d" = internal global i32 0
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [19 x i8], [19 x i8]* @"str", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr")
  %"strptr.2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.2", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.2", i32* @"a")
  %"strptr.3" = getelementptr inbounds [23 x i8], [23 x i8]* @"str.3", i32 0, i32 0
  %"strptr.4" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.4", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.4", i8* %"strptr.3")
  %"strptr.5" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.5", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.5", i32* @"b")
  %"strptr.6" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.6", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.6", i32* @"c")
  %"strptr.7" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.7", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.7", i32* @"d")
  %"strptr.8" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.8", i32 0, i32 0
  %"a" = load i32, i32* @"a"
  %"b" = load i32, i32* @"b"
  %".8" = add i32 %"a", %"b"
  %"c" = load i32, i32* @"c"
  %".9" = add i32 %".8", %"c"
  %"d" = load i32, i32* @"d"
  %".10" = add i32 %".9", %"d"
  %"strptr.9" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.9", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %"strptr.9", i8* %"strptr.8", i32 %".10")
  %"strptr.10" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.10", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.10")
  %".13" = fptosi double 0x400f333333333333 to i32
  %"strptr.11" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.11", i32 0, i32 0
  %".14" = call i32 (i8*, ...) @"printf"(i8* %"strptr.11", i32 %".13")
  %".15" = zext i1 1 to i32
  %"strptr.12" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.12", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"strptr.12", i32 %".15")
  %".17" = sitofp i32 10 to double
  %"strptr.13" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.13", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %"strptr.13", double %".17")
  %".19" = zext i1 1 to i32
  %".20" = sitofp i32 %".19" to double
  %"strptr.14" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.14", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %"strptr.14", double %".20")
  %".22" = icmp ne i32 1, 0
  %"strptr.15" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.15", i32 0, i32 0
  %"strptr.16" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.16", i32 0, i32 0
  %".23" = select  i1 %".22", i8* %"strptr.15", i8* %"strptr.16"
  %"strptr.17" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.17", i32 0, i32 0
  %".24" = call i32 (i8*, ...) @"printf"(i8* %"strptr.17", i8* %".23")
  %".25" = fcmp one double              0.000000e+00,              0x0
  %"strptr.18" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.18", i32 0, i32 0
  %"strptr.19" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.19", i32 0, i32 0
  %".26" = select  i1 %".25", i8* %"strptr.18", i8* %"strptr.19"
  %"strptr.20" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.20", i32 0, i32 0
  %".27" = call i32 (i8*, ...) @"printf"(i8* %"strptr.20", i8* %".26")
  %".28" = add i32 10, 5
  %"str_buf" = call i8* @"malloc"(i64 64)
  %"strptr.21" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.21", i32 0, i32 0
  %".29" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %"str_buf", i8* %"strptr.21", i32 %".28")
  %"strptr.22" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.22", i32 0, i32 0
  %".30" = call i32 (i8*, ...) @"printf"(i8* %"strptr.22", i8* %"str_buf")
  ret void
}

@"str" = private constant [19 x i8] c"Digite um n\c3\bamero \00"
@"str.1" = private constant [4 x i8] c"%s\0a\00"
@"str.2" = private constant [3 x i8] c"%d\00"
@"str.3" = private constant [23 x i8] c"Digite tr\c3\aas n\c3\bameros \00"
@"str.4" = private constant [4 x i8] c"%s\0a\00"
@"str.5" = private constant [3 x i8] c"%d\00"
@"str.6" = private constant [3 x i8] c"%d\00"
@"str.7" = private constant [3 x i8] c"%d\00"
@"str.8" = private constant [7 x i8] c"Soma: \00"
@"str.9" = private constant [7 x i8] c"%s %d\0a\00"
@"str.10" = private constant [2 x i8] c"\0a\00"
@"str.11" = private constant [4 x i8] c"%d\0a\00"
@"str.12" = private constant [4 x i8] c"%d\0a\00"
@"str.13" = private constant [4 x i8] c"%f\0a\00"
@"str.14" = private constant [4 x i8] c"%f\0a\00"
@"str.15" = private constant [5 x i8] c"true\00"
@"str.16" = private constant [6 x i8] c"false\00"
@"str.17" = private constant [4 x i8] c"%s\0a\00"
@"str.18" = private constant [5 x i8] c"true\00"
@"str.19" = private constant [6 x i8] c"false\00"
@"str.20" = private constant [4 x i8] c"%s\0a\00"
@"str.21" = private constant [3 x i8] c"%d\00"
@"str.22" = private constant [4 x i8] c"%s\0a\00"
define i32 @"main"()
{
entry:
  %".2" = call i32 @"SetConsoleOutputCP"(i32 65001)
  call void @"__jss_global_init"()
  ret i32 0
}
