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

@"valor_int" = internal global i32 42
@"valor_real" = internal global double              0.000000e+00
@"pi" = internal global double 0x40091eb851eb851f
@"pi_int" = internal global i32 0
@"num_str" = internal global i8* null
@"zero" = internal global i32 0
@"nao_zero" = internal global i32 5
@"falso" = internal global i1 0
@"verdadeiro" = internal global i1 0
@"result" = internal global i32 0
define void @"__jss_global_init"()
{
entry:
  %"valor_int" = load i32, i32* @"valor_int"
  %".2" = sitofp i32 %"valor_int" to double
  store double %".2", double* @"valor_real"
  %"strptr" = getelementptr inbounds [11 x i8], [11 x i8]* @"str", i32 0, i32 0
  %"valor_int.1" = load i32, i32* @"valor_int"
  %"strptr.1" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.1", i32 0, i32 0
  %"valor_real" = load double, double* @"valor_real"
  %"strptr.2" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.2", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.2", i8* %"strptr", i32 %"valor_int.1", i8* %"strptr.1", double %"valor_real")
  %"pi" = load double, double* @"pi"
  %".5" = fptosi double %"pi" to i32
  store i32 %".5", i32* @"pi_int"
  %"strptr.3" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.3", i32 0, i32 0
  %"pi.1" = load double, double* @"pi"
  %"strptr.4" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.4", i32 0, i32 0
  %"pi_int" = load i32, i32* @"pi_int"
  %"strptr.5" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.5", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"strptr.5", i8* %"strptr.3", double %"pi.1", i8* %"strptr.4", i32 %"pi_int")
  %"valor_int.2" = load i32, i32* @"valor_int"
  %"str_buf" = call i8* @"malloc"(i64 64)
  %"strptr.6" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.6", i32 0, i32 0
  %".8" = call i32 (i8*, i8*, ...) @"sprintf"(i8* %"str_buf", i8* %"strptr.6", i32 %"valor_int.2")
  store i8* %"str_buf", i8** @"num_str"
  %"strptr.7" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.7", i32 0, i32 0
  %"num_str" = load i8*, i8** @"num_str"
  %"strptr.8" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.8", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %"strptr.8", i8* %"strptr.7", i8* %"num_str")
  %"zero" = load i32, i32* @"zero"
  %".11" = icmp ne i32 %"zero", 0
  store i1 %".11", i1* @"falso"
  %"nao_zero" = load i32, i32* @"nao_zero"
  %".13" = icmp ne i32 %"nao_zero", 0
  store i1 %".13", i1* @"verdadeiro"
  %"strptr.9" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.9", i32 0, i32 0
  %"falso" = load i1, i1* @"falso"
  %"strptr.10" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.10", i32 0, i32 0
  %"strptr.11" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.11", i32 0, i32 0
  %".15" = select  i1 %"falso", i8* %"strptr.10", i8* %"strptr.11"
  %"verdadeiro" = load i1, i1* @"verdadeiro"
  %"strptr.12" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.12", i32 0, i32 0
  %"strptr.13" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.13", i32 0, i32 0
  %".16" = select  i1 %"verdadeiro", i8* %"strptr.12", i8* %"strptr.13"
  %"strptr.14" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.14", i32 0, i32 0
  %".17" = call i32 (i8*, ...) @"printf"(i8* %"strptr.14", i8* %"strptr.9", i8* %".15", i8* %".16")
  %".18" = fadd double 0x4016000000000000, 0x4012000000000000
  %".19" = fptosi double %".18" to i32
  store i32 %".19", i32* @"result"
  %"strptr.15" = getelementptr inbounds [16 x i8], [16 x i8]* @"str.15", i32 0, i32 0
  %"result" = load i32, i32* @"result"
  %"strptr.16" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.16", i32 0, i32 0
  %".21" = call i32 (i8*, ...) @"printf"(i8* %"strptr.16", i8* %"strptr.15", i32 %"result")
  ret void
}

@"str" = private constant [11 x i8] c"Int->Real:\00"
@"str.1" = private constant [3 x i8] c"->\00"
@"str.2" = private constant [13 x i8] c"%s %d %s %f\0a\00"
@"str.3" = private constant [11 x i8] c"Real->Int:\00"
@"str.4" = private constant [3 x i8] c"->\00"
@"str.5" = private constant [13 x i8] c"%s %f %s %d\0a\00"
@"str.6" = private constant [3 x i8] c"%d\00"
@"str.7" = private constant [13 x i8] c"Int->String:\00"
@"str.8" = private constant [7 x i8] c"%s %s\0a\00"
@"str.9" = private constant [11 x i8] c"Int->Bool:\00"
@"str.10" = private constant [5 x i8] c"true\00"
@"str.11" = private constant [6 x i8] c"false\00"
@"str.12" = private constant [5 x i8] c"true\00"
@"str.13" = private constant [6 x i8] c"false\00"
@"str.14" = private constant [10 x i8] c"%s %s %s\0a\00"
@"str.15" = private constant [16 x i8] c"Cast expressao:\00"
@"str.16" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_global_init"()
  ret i32 0
}
