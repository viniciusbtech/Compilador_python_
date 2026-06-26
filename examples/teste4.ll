; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"a" = internal global i32 0
define void @"__jss_global_init"()
{
entry:
  %"b" = alloca i32
  br label %"while_cond"
while_cond:
  %"a" = load i32, i32* @"a"
  %".3" = icmp slt i32 %"a", 2
  br i1 %".3", label %"while_body", label %"while_end"
while_body:
  store i32 0, i32* %"b"
  br label %"while_cond.1"
while_end:
  ret void
while_cond.1:
  %"b.1" = load i32, i32* %"b"
  %".7" = icmp slt i32 %"b.1", 3
  br i1 %".7", label %"while_body.1", label %"while_end.1"
while_body.1:
  %"strptr" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %"a.1" = load i32, i32* @"a"
  %"strptr.1" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.1", i32 0, i32 0
  %"b.2" = load i32, i32* %"b"
  %"strptr.2" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.2", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %"strptr.2", i8* %"strptr", i32 %"a.1", i8* %"strptr.1", i32 %"b.2")
  %"b.3" = load i32, i32* %"b"
  %".10" = add i32 %"b.3", 1
  store i32 %".10", i32* %"b"
  br label %"while_cond.1"
while_end.1:
  %"a.2" = load i32, i32* @"a"
  %".13" = add i32 %"a.2", 1
  store i32 %".13", i32* @"a"
  br label %"while_cond"
}

@"str" = private constant [3 x i8] c"a:\00"
@"str.1" = private constant [3 x i8] c"b:\00"
@"str.2" = private constant [13 x i8] c"%s %d %s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
