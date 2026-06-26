; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

@"val" = internal global i32 10
define void @"__jss_global_init"()
{
entry:
  %"val" = load i32, i32* @"val"
  %".2" = add i32 %"val", 5
  store i32 %".2", i32* @"val"
  %"strptr" = getelementptr inbounds [3 x i8], [3 x i8]* @"str", i32 0, i32 0
  %"val.1" = load i32, i32* @"val"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.1", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", i32 %"val.1")
  %"val.2" = load i32, i32* @"val"
  %".5" = sub i32 %"val.2", 3
  store i32 %".5", i32* @"val"
  %"strptr.2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.2", i32 0, i32 0
  %"val.3" = load i32, i32* @"val"
  %"strptr.3" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.3", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i8* %"strptr.2", i32 %"val.3")
  %"val.4" = load i32, i32* @"val"
  %".8" = mul i32 %"val.4", 2
  store i32 %".8", i32* @"val"
  %"strptr.4" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.4", i32 0, i32 0
  %"val.5" = load i32, i32* @"val"
  %"strptr.5" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.5", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %"strptr.5", i8* %"strptr.4", i32 %"val.5")
  %"val.6" = load i32, i32* @"val"
  %".11" = sdiv i32 %"val.6", 4
  store i32 %".11", i32* @"val"
  %"strptr.6" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.6", i32 0, i32 0
  %"val.7" = load i32, i32* @"val"
  %"strptr.7" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.7", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.6", i32 %"val.7")
  %"val.8" = load i32, i32* @"val"
  %".14" = srem i32 %"val.8", 4
  store i32 %".14", i32* @"val"
  %"strptr.8" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.8", i32 0, i32 0
  %"val.9" = load i32, i32* @"val"
  %"strptr.9" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.9", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"strptr.9", i8* %"strptr.8", i32 %"val.9")
  ret void
}

@"str" = private constant [3 x i8] c"+=\00"
@"str.1" = private constant [7 x i8] c"%s %d\0a\00"
@"str.2" = private constant [3 x i8] c"-=\00"
@"str.3" = private constant [7 x i8] c"%s %d\0a\00"
@"str.4" = private constant [3 x i8] c"*=\00"
@"str.5" = private constant [7 x i8] c"%s %d\0a\00"
@"str.6" = private constant [3 x i8] c"/=\00"
@"str.7" = private constant [7 x i8] c"%s %d\0a\00"
@"str.8" = private constant [3 x i8] c"%=\00"
@"str.9" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
