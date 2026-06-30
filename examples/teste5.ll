; ModuleID = "jss_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

%"Pessoa" = type {i8*, i32}
%"Contador" = type {i32}
%"MatrizHelper" = type {[3 x [3 x i32]]}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i8* @"malloc"(i64 %".1")

declare i32 @"sprintf"(i8* %".1", i8* %".2", ...)

declare i64 @"strlen"(i8* %".1")

declare i8* @"strcpy"(i8* %".1", i8* %".2")

declare i8* @"strcat"(i8* %".1", i8* %".2")

define void @"__jss_user_main"()
{
entry:
  %"p1" = alloca %"Pessoa"*
  %"nome" = alloca i8*
  %"c" = alloca %"Contador"*
  %"mh" = alloca %"MatrizHelper"*
  %"val" = alloca i32
  %"strptr" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.7", i32 0, i32 0
  %".2" = call %"Pessoa"* @"Pessoa.constructor"(i8* %"strptr", i32 30)
  store %"Pessoa"* %".2", %"Pessoa"** %"p1"
  %"p1.1" = load %"Pessoa"*, %"Pessoa"** %"p1"
  call void @"Pessoa.apresentar"(%"Pessoa"* %"p1.1")
  %"p1.2" = load %"Pessoa"*, %"Pessoa"** %"p1"
  %".5" = call i8* @"Pessoa.getNome"(%"Pessoa"* %"p1.2")
  store i8* %".5", i8** %"nome"
  %"strptr.1" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.8", i32 0, i32 0
  %"nome.1" = load i8*, i8** %"nome"
  %"strptr.2" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.9", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"strptr.2", i8* %"strptr.1", i8* %"nome.1")
  %"p1.3" = load %"Pessoa"*, %"Pessoa"** %"p1"
  call void @"Pessoa.aniversario"(%"Pessoa"* %"p1.3")
  %".9" = call %"Contador"* @"Contador.constructor"()
  store %"Contador"* %".9", %"Contador"** %"c"
  %"strptr.3" = getelementptr inbounds [18 x i8], [18 x i8]* @"str.10", i32 0, i32 0
  %"c.1" = load %"Contador"*, %"Contador"** %"c"
  %".11" = call i32 @"Contador.getValor"(%"Contador"* %"c.1")
  %"strptr.4" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.11", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %"strptr.4", i8* %"strptr.3", i32 %".11")
  %"c.2" = load %"Contador"*, %"Contador"** %"c"
  call void @"Contador.incrementar"(%"Contador"* %"c.2")
  %"c.3" = load %"Contador"*, %"Contador"** %"c"
  call void @"Contador.incrementar"(%"Contador"* %"c.3")
  %"strptr.5" = getelementptr inbounds [20 x i8], [20 x i8]* @"str.12", i32 0, i32 0
  %"c.4" = load %"Contador"*, %"Contador"** %"c"
  %".15" = call i32 @"Contador.getValor"(%"Contador"* %"c.4")
  %"strptr.6" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.13", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"strptr.6", i8* %"strptr.5", i32 %".15")
  %"c.5" = load %"Contador"*, %"Contador"** %"c"
  call void @"Contador.decrementar"(%"Contador"* %"c.5")
  %"strptr.7" = getelementptr inbounds [19 x i8], [19 x i8]* @"str.14", i32 0, i32 0
  %"c.6" = load %"Contador"*, %"Contador"** %"c"
  %".18" = call i32 @"Contador.getValor"(%"Contador"* %"c.6")
  %"strptr.8" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.15", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %"strptr.8", i8* %"strptr.7", i32 %".18")
  %".20" = call %"MatrizHelper"* @"MatrizHelper.constructor"()
  store %"MatrizHelper"* %".20", %"MatrizHelper"** %"mh"
  %"mh.1" = load %"MatrizHelper"*, %"MatrizHelper"** %"mh"
  call void @"MatrizHelper.setValor"(%"MatrizHelper"* %"mh.1", i32 0, i32 0, i32 1)
  %"mh.2" = load %"MatrizHelper"*, %"MatrizHelper"** %"mh"
  call void @"MatrizHelper.setValor"(%"MatrizHelper"* %"mh.2", i32 0, i32 1, i32 2)
  %"mh.3" = load %"MatrizHelper"*, %"MatrizHelper"** %"mh"
  call void @"MatrizHelper.setValor"(%"MatrizHelper"* %"mh.3", i32 1, i32 0, i32 3)
  %"mh.4" = load %"MatrizHelper"*, %"MatrizHelper"** %"mh"
  call void @"MatrizHelper.setValor"(%"MatrizHelper"* %"mh.4", i32 1, i32 1, i32 4)
  %"mh.5" = load %"MatrizHelper"*, %"MatrizHelper"** %"mh"
  %".26" = call i32 @"MatrizHelper.getValor"(%"MatrizHelper"* %"mh.5", i32 1, i32 1)
  store i32 %".26", i32* %"val"
  %"strptr.9" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.16", i32 0, i32 0
  %"val.1" = load i32, i32* %"val"
  %"strptr.10" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.17", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %"strptr.10", i8* %"strptr.9", i32 %"val.1")
  %"strptr.11" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.18", i32 0, i32 0
  %"strptr.12" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.19", i32 0, i32 0
  %".29" = call i32 (i8*, ...) @"printf"(i8* %"strptr.12", i8* %"strptr.11")
  %"mh.6" = load %"MatrizHelper"*, %"MatrizHelper"** %"mh"
  call void @"MatrizHelper.imprimir"(%"MatrizHelper"* %"mh.6")
  ret void
}

define i8* @"Pessoa.getNome"(%"Pessoa"* %".1")
{
entry:
  %"self" = alloca %"Pessoa"*
  store %"Pessoa"* %".1", %"Pessoa"** %"self"
  %"this" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".4" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this", i32 0, i32 0
  %".5" = load i8*, i8** %".4"
  ret i8* %".5"
}

define i32 @"Pessoa.getIdade"(%"Pessoa"* %".1")
{
entry:
  %"self" = alloca %"Pessoa"*
  store %"Pessoa"* %".1", %"Pessoa"** %"self"
  %"this" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".4" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this", i32 0, i32 1
  %".5" = load i32, i32* %".4"
  ret i32 %".5"
}

define void @"Pessoa.apresentar"(%"Pessoa"* %".1")
{
entry:
  %"self" = alloca %"Pessoa"*
  store %"Pessoa"* %".1", %"Pessoa"** %"self"
  %"strptr" = getelementptr inbounds [6 x i8], [6 x i8]* @"str", i32 0, i32 0
  %"this" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".4" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this", i32 0, i32 0
  %".5" = load i8*, i8** %".4"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.1", i32 0, i32 0
  %"this.1" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".6" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this.1", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %"strptr.2" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.2", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %"strptr.2", i8* %"strptr", i8* %".5", i8* %"strptr.1", i32 %".7")
  ret void
}

define void @"Pessoa.aniversario"(%"Pessoa"* %".1")
{
entry:
  %"self" = alloca %"Pessoa"*
  store %"Pessoa"* %".1", %"Pessoa"** %"self"
  %"this" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".4" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this", i32 0, i32 1
  %".5" = load i32, i32* %".4"
  %".6" = add i32 %".5", 1
  %"this.1" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".7" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this.1", i32 0, i32 1
  store i32 %".6", i32* %".7"
  %"this.2" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".9" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this.2", i32 0, i32 0
  %".10" = load i8*, i8** %".9"
  %"strptr" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.3", i32 0, i32 0
  %"this.3" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".11" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this.3", i32 0, i32 1
  %".12" = load i32, i32* %".11"
  %"strptr.1" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.4", i32 0, i32 0
  %"strptr.2" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.5", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %"strptr.2", i8* %".10", i8* %"strptr", i32 %".12", i8* %"strptr.1")
  ret void
}

define %"Pessoa"* @"Pessoa.constructor"(i8* %".1", i32 %".2")
{
entry:
  %"raw" = call i8* @"malloc"(i64 16)
  %"obj" = bitcast i8* %"raw" to %"Pessoa"*
  %"self" = alloca %"Pessoa"*
  store %"Pessoa"* %"obj", %"Pessoa"** %"self"
  %"n" = alloca i8*
  store i8* %".1", i8** %"n"
  %"i" = alloca i32
  store i32 %".2", i32* %"i"
  %"n.1" = load i8*, i8** %"n"
  %"this" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".7" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this", i32 0, i32 0
  store i8* %"n.1", i8** %".7"
  %"i.1" = load i32, i32* %"i"
  %"this.1" = load %"Pessoa"*, %"Pessoa"** %"self"
  %".9" = getelementptr inbounds %"Pessoa", %"Pessoa"* %"this.1", i32 0, i32 1
  store i32 %"i.1", i32* %".9"
  %"ret_obj" = load %"Pessoa"*, %"Pessoa"** %"self"
  ret %"Pessoa"* %"ret_obj"
}

@"str" = private constant [6 x i8] c"Nome:\00"
@"str.1" = private constant [7 x i8] c"Idade:\00"
@"str.2" = private constant [13 x i8] c"%s %s %s %d\0a\00"
@"str.3" = private constant [10 x i8] c"agora tem\00"
@"str.4" = private constant [5 x i8] c"anos\00"
@"str.5" = private constant [13 x i8] c"%s %s %d %s\0a\00"
define void @"Contador.incrementar"(%"Contador"* %".1")
{
entry:
  %"self" = alloca %"Contador"*
  store %"Contador"* %".1", %"Contador"** %"self"
  %"this" = load %"Contador"*, %"Contador"** %"self"
  %".4" = getelementptr inbounds %"Contador", %"Contador"* %"this", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  %".6" = add i32 %".5", 1
  %"this.1" = load %"Contador"*, %"Contador"** %"self"
  %".7" = getelementptr inbounds %"Contador", %"Contador"* %"this.1", i32 0, i32 0
  store i32 %".6", i32* %".7"
  ret void
}

define void @"Contador.decrementar"(%"Contador"* %".1")
{
entry:
  %"self" = alloca %"Contador"*
  store %"Contador"* %".1", %"Contador"** %"self"
  %"this" = load %"Contador"*, %"Contador"** %"self"
  %".4" = getelementptr inbounds %"Contador", %"Contador"* %"this", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  %".6" = sub i32 %".5", 1
  %"this.1" = load %"Contador"*, %"Contador"** %"self"
  %".7" = getelementptr inbounds %"Contador", %"Contador"* %"this.1", i32 0, i32 0
  store i32 %".6", i32* %".7"
  ret void
}

define i32 @"Contador.getValor"(%"Contador"* %".1")
{
entry:
  %"self" = alloca %"Contador"*
  store %"Contador"* %".1", %"Contador"** %"self"
  %"this" = load %"Contador"*, %"Contador"** %"self"
  %".4" = getelementptr inbounds %"Contador", %"Contador"* %"this", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  ret i32 %".5"
}

define %"Contador"* @"Contador.constructor"()
{
entry:
  %"raw" = call i8* @"malloc"(i64 4)
  %"obj" = bitcast i8* %"raw" to %"Contador"*
  %"self" = alloca %"Contador"*
  store %"Contador"* %"obj", %"Contador"** %"self"
  %"this" = load %"Contador"*, %"Contador"** %"self"
  %".3" = getelementptr inbounds %"Contador", %"Contador"* %"this", i32 0, i32 0
  store i32 0, i32* %".3"
  %"ret_obj" = load %"Contador"*, %"Contador"** %"self"
  ret %"Contador"* %"ret_obj"
}

define void @"MatrizHelper.setValor"(%"MatrizHelper"* %".1", i32 %".2", i32 %".3", i32 %".4")
{
entry:
  %"self" = alloca %"MatrizHelper"*
  store %"MatrizHelper"* %".1", %"MatrizHelper"** %"self"
  %"i" = alloca i32
  store i32 %".2", i32* %"i"
  %"j" = alloca i32
  store i32 %".3", i32* %"j"
  %"valor" = alloca i32
  store i32 %".4", i32* %"valor"
  %"valor.1" = load i32, i32* %"valor"
  %"this" = load %"MatrizHelper"*, %"MatrizHelper"** %"self"
  %".10" = getelementptr inbounds %"MatrizHelper", %"MatrizHelper"* %"this", i32 0, i32 0
  %"i.1" = load i32, i32* %"i"
  %"j.1" = load i32, i32* %"j"
  %".11" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* %".10", i32 0, i32 %"i.1", i32 %"j.1"
  store i32 %"valor.1", i32* %".11"
  ret void
}

define i32 @"MatrizHelper.getValor"(%"MatrizHelper"* %".1", i32 %".2", i32 %".3")
{
entry:
  %"self" = alloca %"MatrizHelper"*
  store %"MatrizHelper"* %".1", %"MatrizHelper"** %"self"
  %"i" = alloca i32
  store i32 %".2", i32* %"i"
  %"j" = alloca i32
  store i32 %".3", i32* %"j"
  %"this" = load %"MatrizHelper"*, %"MatrizHelper"** %"self"
  %".8" = getelementptr inbounds %"MatrizHelper", %"MatrizHelper"* %"this", i32 0, i32 0
  %"i.1" = load i32, i32* %"i"
  %"j.1" = load i32, i32* %"j"
  %".9" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* %".8", i32 0, i32 %"i.1", i32 %"j.1"
  %".10" = load i32, i32* %".9"
  ret i32 %".10"
}

define void @"MatrizHelper.imprimir"(%"MatrizHelper"* %".1")
{
entry:
  %"i" = alloca i32
  %"j" = alloca i32
  %"self" = alloca %"MatrizHelper"*
  store %"MatrizHelper"* %".1", %"MatrizHelper"** %"self"
  store i32 0, i32* %"i"
  br label %"for_cond"
for_cond:
  %"i.1" = load i32, i32* %"i"
  %".6" = icmp slt i32 %"i.1", 3
  br i1 %".6", label %"for_body", label %"for_end"
for_body:
  store i32 0, i32* %"j"
  br label %"for_cond.1"
for_end:
  ret void
for_cond.1:
  %"j.1" = load i32, i32* %"j"
  %".10" = icmp slt i32 %"j.1", 3
  br i1 %".10", label %"for_body.1", label %"for_end.1"
for_body.1:
  %"this" = load %"MatrizHelper"*, %"MatrizHelper"** %"self"
  %".12" = getelementptr inbounds %"MatrizHelper", %"MatrizHelper"* %"this", i32 0, i32 0
  %"i.2" = load i32, i32* %"i"
  %"j.2" = load i32, i32* %"j"
  %".13" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* %".12", i32 0, i32 %"i.2", i32 %"j.2"
  %".14" = load i32, i32* %".13"
  %"strptr" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.6", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %"strptr", i32 %".14")
  %"j.3" = load i32, i32* %"j"
  %".16" = add i32 %"j.3", 1
  store i32 %".16", i32* %"j"
  br label %"for_cond.1"
for_end.1:
  %"i.3" = load i32, i32* %"i"
  %".19" = add i32 %"i.3", 1
  store i32 %".19", i32* %"i"
  br label %"for_cond"
}

define %"MatrizHelper"* @"MatrizHelper.constructor"()
{
entry:
  %"raw" = call i8* @"malloc"(i64 36)
  %"obj" = bitcast i8* %"raw" to %"MatrizHelper"*
  %"self" = alloca %"MatrizHelper"*
  store %"MatrizHelper"* %"obj", %"MatrizHelper"** %"self"
  %"i" = alloca i32
  %"j" = alloca i32
  store i32 0, i32* %"i"
  br label %"for_cond"
for_cond:
  %"i.1" = load i32, i32* %"i"
  %".5" = icmp slt i32 %"i.1", 3
  br i1 %".5", label %"for_body", label %"for_end"
for_body:
  store i32 0, i32* %"j"
  br label %"for_cond.1"
for_end:
  %"ret_obj" = load %"MatrizHelper"*, %"MatrizHelper"** %"self"
  ret %"MatrizHelper"* %"ret_obj"
for_cond.1:
  %"j.1" = load i32, i32* %"j"
  %".9" = icmp slt i32 %"j.1", 3
  br i1 %".9", label %"for_body.1", label %"for_end.1"
for_body.1:
  %"this" = load %"MatrizHelper"*, %"MatrizHelper"** %"self"
  %".11" = getelementptr inbounds %"MatrizHelper", %"MatrizHelper"* %"this", i32 0, i32 0
  %"i.2" = load i32, i32* %"i"
  %"j.2" = load i32, i32* %"j"
  %".12" = getelementptr inbounds [3 x [3 x i32]], [3 x [3 x i32]]* %".11", i32 0, i32 %"i.2", i32 %"j.2"
  store i32 0, i32* %".12"
  %"j.3" = load i32, i32* %"j"
  %".14" = add i32 %"j.3", 1
  store i32 %".14", i32* %"j"
  br label %"for_cond.1"
for_end.1:
  %"i.3" = load i32, i32* %"i"
  %".17" = add i32 %"i.3", 1
  store i32 %".17", i32* %"i"
  br label %"for_cond"
}

@"str.6" = private constant [4 x i8] c"%d\0a\00"
@"str.7" = private constant [5 x i8] c"Joao\00"
@"str.8" = private constant [13 x i8] c"Nome obtido:\00"
@"str.9" = private constant [7 x i8] c"%s %s\0a\00"
@"str.10" = private constant [18 x i8] c"Contador inicial:\00"
@"str.11" = private constant [7 x i8] c"%s %d\0a\00"
@"str.12" = private constant [20 x i8] c"Apos 2 incrementos:\00"
@"str.13" = private constant [7 x i8] c"%s %d\0a\00"
@"str.14" = private constant [19 x i8] c"Apos 1 decremento:\00"
@"str.15" = private constant [7 x i8] c"%s %d\0a\00"
@"str.16" = private constant [13 x i8] c"Valor[1][1]:\00"
@"str.17" = private constant [7 x i8] c"%s %d\0a\00"
@"str.18" = private constant [8 x i8] c"Matriz:\00"
@"str.19" = private constant [4 x i8] c"%s\0a\00"
define i32 @"main"()
{
entry:
  call void @"__jss_user_main"()
  ret i32 0
}
