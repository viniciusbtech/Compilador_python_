; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"j" = internal global i32 0
define void @"__jss_global_init"()
{
entry:
  br label %"while_cond"
while_cond:
  br i1 1, label %"while_body", label %"while_end"
while_body:
  %"j" = load i32, i32* @"j"
  %".4" = icmp eq i32 %"j", 3
  br i1 %".4", label %"if_then", label %"if_else"
while_end:
  ret void
if_then:
  br label %"while_end"
if_else:
  br label %"if_merge"
if_merge:
  %"strptr" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %"j.1" = load i32, i32* @"j"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.1", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", i32 %"j.1")
  %"j.2" = load i32, i32* @"j"
  %".9" = add i32 %"j.2", 1
  store i32 %".9", i32* @"j"
  br label %"while_cond"
}

@"str" = private constant [3 x i8] c"j:\00"
@"str.1" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
