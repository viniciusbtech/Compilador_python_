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

define i32 @"fatorial"(i32 %".1")
{
entry:
  %"fat" = alloca i32
  store i32 %".1", i32* %"fat"
  %"fat.1" = load i32, i32* %"fat"
  %".4" = icmp sgt i32 %"fat.1", 1
  br i1 %".4", label %"if_then", label %"if_else"
if_then:
  %"fat.2" = load i32, i32* %"fat"
  %"strptr" = getelementptr inbounds [4 x i8], [4 x i8]* @"str", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"strptr", i32 %"fat.2")
  %"fat.3" = load i32, i32* %"fat"
  %"fat.4" = load i32, i32* %"fat"
  %".7" = sub i32 %"fat.4", 1
  %".8" = call i32 @"fatorial"(i32 %".7")
  %".9" = mul i32 %"fat.3", %".8"
  ret i32 %".9"
if_else:
  ret i32 1
if_merge:
  ret i32 0
}

define void @"printMedia"(i32 %".1", i32 %".2")
{
entry:
  %"x" = alloca double
  %"v1" = alloca i32
  store i32 %".1", i32* %"v1"
  %"v2" = alloca i32
  store i32 %".2", i32* %"v2"
  %"v1.1" = load i32, i32* %"v1"
  %".6" = sitofp i32 %"v1.1" to double
  %"v2.1" = load i32, i32* %"v2"
  %".7" = sitofp i32 %"v2.1" to double
  %".8" = call double @"media"(double %".6", double %".7")
  store double %".8", double* %"x"
  %"strptr" = getelementptr inbounds [14 x i8], [14 x i8]* @"str.1", i32 0, i32 0
  %"x.1" = load double, double* %"x"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.2", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", double %"x.1")
  ret void
}

define double @"media"(double %".1", double %".2")
{
entry:
  %"n1" = alloca double
  store double %".1", double* %"n1"
  %"n2" = alloca double
  store double %".2", double* %"n2"
  %"n1.1" = load double, double* %"n1"
  %"n2.1" = load double, double* %"n2"
  %".6" = fadd double %"n1.1", %"n2.1"
  %".7" = sitofp i32 2 to double
  %".8" = fdiv double %".6", %".7"
  ret double %".8"
}

define void @"__jss_user_main"()
{
entry:
  %"numero" = alloca i32
  %"n1" = alloca i32
  %"n2" = alloca i32
  %"strptr" = getelementptr inbounds [37 x i8], [37 x i8]* @"str.3", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.4", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr")
  %"strptr.2" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.5", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.2", i32* %"numero")
  %"numero.1" = load i32, i32* %"numero"
  %".4" = call i32 @"fatorial"(i32 %"numero.1")
  %"strptr.3" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.6", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i32 %".4")
  %"strptr.4" = getelementptr inbounds [38 x i8], [38 x i8]* @"str.7", i32 0, i32 0
  %"strptr.5" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.8", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"strptr.5", i8* %"strptr.4")
  %"strptr.6" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.9", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.6", i32* %"n1")
  %"strptr.7" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.10", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"scanf"(i8* %"strptr.7", i32* %"n2")
  %"n1.1" = load i32, i32* %"n1"
  %".9" = sitofp i32 %"n1.1" to double
  %"n2.1" = load i32, i32* %"n2"
  %".10" = sitofp i32 %"n2.1" to double
  %".11" = call double @"media"(double %".9", double %".10")
  %"strptr.8" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.11", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.8", double %".11")
  %"strptr.9" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.12", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %"strptr.9", i32 0)
  ret void
}

@"str" = private constant [4 x i8] c"%d\0a\00"
@"str.1" = private constant [14 x i8] c" Resultado : \00"
@"str.2" = private constant [7 x i8] c"%s %f\0a\00"
@"str.3" = private constant [37 x i8] c" Programa Fatorial. Digite o valor: \00"
@"str.4" = private constant [4 x i8] c"%s\0a\00"
@"str.5" = private constant [3 x i8] c"%d\00"
@"str.6" = private constant [4 x i8] c"%d\0a\00"
@"str.7" = private constant [38 x i8] c" Programa Media . Digite os valores: \00"
@"str.8" = private constant [4 x i8] c"%s\0a\00"
@"str.9" = private constant [3 x i8] c"%d\00"
@"str.10" = private constant [3 x i8] c"%d\00"
@"str.11" = private constant [4 x i8] c"%f\0a\00"
@"str.12" = private constant [4 x i8] c"%d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_user_main"()
  ret i32 0
}
