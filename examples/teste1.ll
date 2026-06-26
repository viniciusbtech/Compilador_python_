; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"t" = internal global i1 1
@"f" = internal global i1 0
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [5 x i8], [5 x i8]* @"str", i32 0, i32 0
  %"t" = load i1, i1* @"t"
  br i1 %"t", label %"and_rhs", label %"and_end"
and_rhs:
  %"f" = load i1, i1* @"f"
  br label %"and_end"
and_end:
  %"andtmp" = phi  i1 [0, %"entry"], [%"f", %"and_rhs"]
  %"strptr.1" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.1", i32 0, i32 0
  %"strptr.2" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.2", i32 0, i32 0
  %".4" = select  i1 %"andtmp", i8* %"strptr.1", i8* %"strptr.2"
  %"strptr.3" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.3", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i8* %"strptr", i8* %".4")
  %"strptr.4" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.4", i32 0, i32 0
  %"t.1" = load i1, i1* @"t"
  br i1 %"t.1", label %"or_end", label %"or_rhs"
or_rhs:
  %"f.1" = load i1, i1* @"f"
  br label %"or_end"
or_end:
  %"ortmp" = phi  i1 [1, %"and_end"], [%"f.1", %"or_rhs"]
  %"strptr.5" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.5", i32 0, i32 0
  %"strptr.6" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.6", i32 0, i32 0
  %".8" = select  i1 %"ortmp", i8* %"strptr.5", i8* %"strptr.6"
  %"strptr.7" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.7", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.4", i8* %".8")
  %"strptr.8" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.8", i32 0, i32 0
  %"t.2" = load i1, i1* @"t"
  %".10" = xor i1 %"t.2", -1
  %"strptr.9" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.9", i32 0, i32 0
  %"strptr.10" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.10", i32 0, i32 0
  %".11" = select  i1 %".10", i8* %"strptr.9", i8* %"strptr.10"
  %"strptr.11" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.11", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.11", i8* %"strptr.8", i8* %".11")
  ret void
}

@"str" = private constant [5 x i8] c"AND:\00"
@"str.1" = private constant [5 x i8] c"true\00"
@"str.2" = private constant [6 x i8] c"false\00"
@"str.3" = private constant [7 x i8] c"%s %s\0a\00"
@"str.4" = private constant [4 x i8] c"OR:\00"
@"str.5" = private constant [5 x i8] c"true\00"
@"str.6" = private constant [6 x i8] c"false\00"
@"str.7" = private constant [7 x i8] c"%s %s\0a\00"
@"str.8" = private constant [5 x i8] c"NOT:\00"
@"str.9" = private constant [5 x i8] c"true\00"
@"str.10" = private constant [6 x i8] c"false\00"
@"str.11" = private constant [7 x i8] c"%s %s\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
