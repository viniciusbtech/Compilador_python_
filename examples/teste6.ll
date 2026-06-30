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

define i32 @"soma"(i32 %".1", i32 %".2")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  %"a.1" = load i32, i32* %"a"
  %"b.1" = load i32, i32* %"b"
  %".6" = add i32 %"a.1", %"b.1"
  ret i32 %".6"
}

define void @"imprimirMensagem"(i8* %".1")
{
entry:
  %"msg" = alloca i8*
  store i8* %".1", i8** %"msg"
  %"strptr" = getelementptr inbounds [10 x i8], [10 x i8]* @"str", i32 0, i32 0
  %"msg.1" = load i8*, i8** %"msg"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.1", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", i8* %"msg.1")
  ret void
}

define double @"calcularMedia"(i32 %".1", i32 %".2", i32 %".3")
{
entry:
  %"soma" = alloca i32
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  %"c" = alloca i32
  store i32 %".3", i32* %"c"
  %"a.1" = load i32, i32* %"a"
  %"b.1" = load i32, i32* %"b"
  %".8" = add i32 %"a.1", %"b.1"
  %"c.1" = load i32, i32* %"c"
  %".9" = add i32 %".8", %"c.1"
  store i32 %".9", i32* %"soma"
  %"soma.1" = load i32, i32* %"soma"
  %".11" = sitofp i32 %"soma.1" to double
  %".12" = fdiv double %".11", 0x4008000000000000
  ret double %".12"
}

define i1 @"ehPar"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %"n.1" = load i32, i32* %"n"
  %".4" = srem i32 %"n.1", 2
  %".5" = icmp eq i32 %".4", 0
  ret i1 %".5"
}

define i8* @"getNomeCompleto"(i8* %".1", i8* %".2")
{
entry:
  %"nome" = alloca i8*
  store i8* %".1", i8** %"nome"
  %"sobrenome" = alloca i8*
  store i8* %".2", i8** %"sobrenome"
  %"nome.1" = load i8*, i8** %"nome"
  %"strptr" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.2", i32 0, i32 0
  %"slen1" = call i64 @"strlen"(i8* %"nome.1")
  %"slen2" = call i64 @"strlen"(i8* %"strptr")
  %".6" = add i64 %"slen1", %"slen2"
  %"slen_total" = add i64 %".6", 1
  %"sbuf" = call i8* @"malloc"(i64 %"slen_total")
  %".7" = call i8* @"strcpy"(i8* %"sbuf", i8* %"nome.1")
  %".8" = call i8* @"strcat"(i8* %"sbuf", i8* %"strptr")
  %"sobrenome.1" = load i8*, i8** %"sobrenome"
  %"slen1.1" = call i64 @"strlen"(i8* %"sbuf")
  %"slen2.1" = call i64 @"strlen"(i8* %"sobrenome.1")
  %".9" = add i64 %"slen1.1", %"slen2.1"
  %"slen_total.1" = add i64 %".9", 1
  %"sbuf.1" = call i8* @"malloc"(i64 %"slen_total.1")
  %".10" = call i8* @"strcpy"(i8* %"sbuf.1", i8* %"sbuf")
  %".11" = call i8* @"strcat"(i8* %"sbuf.1", i8* %"sobrenome.1")
  ret i8* %"sbuf.1"
}

define i32 @"somarArray"(i32* %".1")
{
entry:
  %"total" = alloca i32
  %"i" = alloca i32
  %"arr" = alloca i32*
  store i32* %".1", i32** %"arr"
  store i32 0, i32* %"total"
  store i32 0, i32* %"i"
  br label %"for_cond"
for_cond:
  %"i.1" = load i32, i32* %"i"
  %".7" = icmp slt i32 %"i.1", 5
  br i1 %".7", label %"for_body", label %"for_end"
for_body:
  %"i.2" = load i32, i32* %"i"
  %".9" = load i32*, i32** %"arr"
  %".10" = getelementptr inbounds i32, i32* %".9", i32 %"i.2"
  %".11" = load i32, i32* %".10"
  %"total.1" = load i32, i32* %"total"
  %".12" = add i32 %"total.1", %".11"
  store i32 %".12", i32* %"total"
  %"i.3" = load i32, i32* %"i"
  %".14" = add i32 %"i.3", 1
  store i32 %".14", i32* %"i"
  br label %"for_cond"
for_end:
  %"total.2" = load i32, i32* %"total"
  ret i32 %"total.2"
}

define i32 @"fatorial"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %"n.1" = load i32, i32* %"n"
  %".4" = icmp sle i32 %"n.1", 1
  br i1 %".4", label %"if_then", label %"if_else"
if_then:
  ret i32 1
if_else:
  br label %"if_merge"
if_merge:
  %"n.2" = load i32, i32* %"n"
  %"n.3" = load i32, i32* %"n"
  %".8" = sub i32 %"n.3", 1
  %".9" = call i32 @"fatorial"(i32 %".8")
  %".10" = mul i32 %"n.2", %".9"
  ret i32 %".10"
}

define void @"processar"()
{
entry:
  %"strptr" = getelementptr inbounds [15 x i8], [15 x i8]* @"str.3", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.4", i32 0, i32 0
  %".2" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr")
  ret void
}

define void @"__jss_user_main"()
{
entry:
  %"resultado" = alloca i32
  %"media" = alloca double
  %"par" = alloca i1
  %"nomeCompleto" = alloca i8*
  %"numeros" = alloca [5 x i32]
  %"total" = alloca i32
  %"fat5" = alloca i32
  %".2" = call i32 @"soma"(i32 5, i32 3)
  store i32 %".2", i32* %"resultado"
  %"strptr" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.5", i32 0, i32 0
  %"resultado.1" = load i32, i32* %"resultado"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.6", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", i32 %"resultado.1")
  %"strptr.2" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.7", i32 0, i32 0
  call void @"imprimirMensagem"(i8* %"strptr.2")
  %".6" = call double @"calcularMedia"(i32 8, i32 7, i32 9)
  store double %".6", double* %"media"
  %"strptr.3" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.8", i32 0, i32 0
  %"media.1" = load double, double* %"media"
  %"strptr.4" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.9", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %"strptr.4", i8* %"strptr.3", double %"media.1")
  %".9" = call i1 @"ehPar"(i32 10)
  store i1 %".9", i1* %"par"
  %"strptr.5" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.10", i32 0, i32 0
  %"par.1" = load i1, i1* %"par"
  %"strptr.6" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.11", i32 0, i32 0
  %"strptr.7" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.12", i32 0, i32 0
  %".11" = select  i1 %"par.1", i8* %"strptr.6", i8* %"strptr.7"
  %"strptr.8" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.13", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.8", i8* %"strptr.5", i8* %".11")
  %"strptr.9" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.14", i32 0, i32 0
  %"strptr.10" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.15", i32 0, i32 0
  %".13" = call i8* @"getNomeCompleto"(i8* %"strptr.9", i8* %"strptr.10")
  store i8* %".13", i8** %"nomeCompleto"
  %"strptr.11" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.16", i32 0, i32 0
  %"nomeCompleto.1" = load i8*, i8** %"nomeCompleto"
  %"strptr.12" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.17", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %"strptr.12", i8* %"strptr.11", i8* %"nomeCompleto.1")
  %".16" = getelementptr inbounds [5 x i32], [5 x i32]* %"numeros", i32 0, i32 0
  store i32 10, i32* %".16"
  %".18" = getelementptr inbounds [5 x i32], [5 x i32]* %"numeros", i32 0, i32 1
  store i32 20, i32* %".18"
  %".20" = getelementptr inbounds [5 x i32], [5 x i32]* %"numeros", i32 0, i32 2
  store i32 30, i32* %".20"
  %".22" = getelementptr inbounds [5 x i32], [5 x i32]* %"numeros", i32 0, i32 3
  store i32 40, i32* %".22"
  %".24" = getelementptr inbounds [5 x i32], [5 x i32]* %"numeros", i32 0, i32 4
  store i32 50, i32* %".24"
  %".26" = getelementptr inbounds [5 x i32], [5 x i32]* %"numeros", i32 0, i32 0
  %".27" = call i32 @"somarArray"(i32* %".26")
  store i32 %".27", i32* %"total"
  %"strptr.13" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.18", i32 0, i32 0
  %"total.1" = load i32, i32* %"total"
  %"strptr.14" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.19", i32 0, i32 0
  %".29" = call i32 (i8*, ...) @"printf"(i8* %"strptr.14", i8* %"strptr.13", i32 %"total.1")
  %".30" = call i32 @"fatorial"(i32 5)
  store i32 %".30", i32* %"fat5"
  %"strptr.15" = getelementptr inbounds [15 x i8], [15 x i8]* @"str.20", i32 0, i32 0
  %"fat5.1" = load i32, i32* %"fat5"
  %"strptr.16" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.21", i32 0, i32 0
  %".32" = call i32 (i8*, ...) @"printf"(i8* %"strptr.16", i8* %"strptr.15", i32 %"fat5.1")
  call void @"processar"()
  ret void
}

@"str" = private constant [10 x i8] c"Mensagem:\00"
@"str.1" = private constant [7 x i8] c"%s %s\0a\00"
@"str.2" = private constant [2 x i8] c" \00"
@"str.3" = private constant [15 x i8] c"Processando...\00"
@"str.4" = private constant [4 x i8] c"%s\0a\00"
@"str.5" = private constant [6 x i8] c"Soma:\00"
@"str.6" = private constant [7 x i8] c"%s %d\0a\00"
@"str.7" = private constant [10 x i8] c"Ola Mundo\00"
@"str.8" = private constant [7 x i8] c"Media:\00"
@"str.9" = private constant [7 x i8] c"%s %f\0a\00"
@"str.10" = private constant [11 x i8] c"10 eh par?\00"
@"str.11" = private constant [5 x i8] c"true\00"
@"str.12" = private constant [6 x i8] c"false\00"
@"str.13" = private constant [7 x i8] c"%s %s\0a\00"
@"str.14" = private constant [5 x i8] c"Joao\00"
@"str.15" = private constant [6 x i8] c"Silva\00"
@"str.16" = private constant [6 x i8] c"Nome:\00"
@"str.17" = private constant [7 x i8] c"%s %s\0a\00"
@"str.18" = private constant [7 x i8] c"Total:\00"
@"str.19" = private constant [7 x i8] c"%s %d\0a\00"
@"str.20" = private constant [15 x i8] c"Fatorial de 5:\00"
@"str.21" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_user_main"()
  ret i32 0
}
