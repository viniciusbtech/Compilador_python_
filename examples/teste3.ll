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

@"idade" = internal global i32 20
@"nota" = internal global i32 7
@"soma" = internal global i32 0
@"numeros" = internal global [5 x i32] zeroinitializer
@"contador" = internal global i32 0
@"j" = internal global i32 0
@"a" = internal global i32 0
define void @"__jss_global_init"()
{
entry:
  %"i" = alloca i32
  %"x" = alloca i32
  %"y" = alloca i32
  %"b" = alloca i32
  %"idade" = load i32, i32* @"idade"
  %".2" = icmp sge i32 %"idade", 18
  br i1 %".2", label %"if_then", label %"if_else"
if_then:
  %"strptr" = getelementptr inbounds [15 x i8], [15 x i8]* @"str", i32 0, i32 0
  %"strptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.1", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr")
  br label %"if_merge"
if_else:
  %"strptr.2" = getelementptr inbounds [15 x i8], [15 x i8]* @"str.2", i32 0, i32 0
  %"strptr.3" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.3", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i8* %"strptr.2")
  br label %"if_merge"
if_merge:
  %"nota" = load i32, i32* @"nota"
  %".8" = icmp sge i32 %"nota", 9
  br i1 %".8", label %"if_then.1", label %"if_else.1"
if_then.1:
  %"strptr.4" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.4", i32 0, i32 0
  %"strptr.5" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.5", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %"strptr.5", i8* %"strptr.4")
  br label %"if_merge.1"
if_else.1:
  %"nota.1" = load i32, i32* @"nota"
  %".12" = icmp sge i32 %"nota.1", 7
  br i1 %".12", label %"if_then.2", label %"if_else.2"
if_merge.1:
  store i32 1, i32* %"i"
  br label %"for_cond"
if_then.2:
  %"strptr.6" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.6", i32 0, i32 0
  %"strptr.7" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.7", i32 0, i32 0
  %".14" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.6")
  br label %"if_merge.2"
if_else.2:
  %"nota.2" = load i32, i32* @"nota"
  %".16" = icmp sge i32 %"nota.2", 5
  br i1 %".16", label %"if_then.3", label %"if_else.3"
if_merge.2:
  br label %"if_merge.1"
if_then.3:
  %"strptr.8" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.8", i32 0, i32 0
  %"strptr.9" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.9", i32 0, i32 0
  %".18" = call i32 (i8*, ...) @"printf"(i8* %"strptr.9", i8* %"strptr.8")
  br label %"if_merge.3"
if_else.3:
  %"strptr.10" = getelementptr inbounds [2 x i8], [2 x i8]* @"str.10", i32 0, i32 0
  %"strptr.11" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.11", i32 0, i32 0
  %".20" = call i32 (i8*, ...) @"printf"(i8* %"strptr.11", i8* %"strptr.10")
  br label %"if_merge.3"
if_merge.3:
  br label %"if_merge.2"
for_cond:
  %"i.1" = load i32, i32* %"i"
  %".26" = icmp sle i32 %"i.1", 10
  br i1 %".26", label %"for_body", label %"for_end"
for_body:
  %"i.2" = load i32, i32* %"i"
  %"soma" = load i32, i32* @"soma"
  %".28" = add i32 %"soma", %"i.2"
  store i32 %".28", i32* @"soma"
  %"i.3" = load i32, i32* %"i"
  %".30" = add i32 %"i.3", 1
  store i32 %".30", i32* %"i"
  br label %"for_cond"
for_end:
  %"strptr.12" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.12", i32 0, i32 0
  %"soma.1" = load i32, i32* @"soma"
  %"strptr.13" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.13", i32 0, i32 0
  %".33" = call i32 (i8*, ...) @"printf"(i8* %"strptr.13", i8* %"strptr.12", i32 %"soma.1")
  store i32 0, i32* %"x"
  br label %"for_cond.1"
for_cond.1:
  %"x.1" = load i32, i32* %"x"
  %".36" = icmp slt i32 %"x.1", 3
  br i1 %".36", label %"for_body.1", label %"for_end.1"
for_body.1:
  store i32 0, i32* %"y"
  br label %"for_cond.2"
for_end.1:
  store i32 0, i32* %"i"
  br label %"for_cond.3"
for_cond.2:
  %"y.1" = load i32, i32* %"y"
  %".40" = icmp slt i32 %"y.1", 2
  br i1 %".40", label %"for_body.2", label %"for_end.2"
for_body.2:
  %"strptr.14" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.14", i32 0, i32 0
  %"x.2" = load i32, i32* %"x"
  %"strptr.15" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.15", i32 0, i32 0
  %"y.2" = load i32, i32* %"y"
  %"strptr.16" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.16", i32 0, i32 0
  %".42" = call i32 (i8*, ...) @"printf"(i8* %"strptr.16", i8* %"strptr.14", i32 %"x.2", i8* %"strptr.15", i32 %"y.2")
  %"y.3" = load i32, i32* %"y"
  %".43" = add i32 %"y.3", 1
  store i32 %".43", i32* %"y"
  br label %"for_cond.2"
for_end.2:
  %"x.3" = load i32, i32* %"x"
  %".46" = add i32 %"x.3", 1
  store i32 %".46", i32* %"x"
  br label %"for_cond.1"
for_cond.3:
  %"i.4" = load i32, i32* %"i"
  %".51" = icmp slt i32 %"i.4", 5
  br i1 %".51", label %"for_body.3", label %"for_end.3"
for_body.3:
  %"i.5" = load i32, i32* %"i"
  %"i.6" = load i32, i32* %"i"
  %".53" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 %"i.6"
  store i32 %"i.5", i32* %".53"
  %"strptr.17" = getelementptr inbounds [9 x i8], [9 x i8]* @"str.17", i32 0, i32 0
  %"i.7" = load i32, i32* %"i"
  %"strptr.18" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.18", i32 0, i32 0
  %"i.8" = load i32, i32* %"i"
  %".55" = getelementptr inbounds [5 x i32], [5 x i32]* @"numeros", i32 0, i32 %"i.8"
  %".56" = load i32, i32* %".55"
  %"strptr.19" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.19", i32 0, i32 0
  %".57" = call i32 (i8*, ...) @"printf"(i8* %"strptr.19", i8* %"strptr.17", i32 %"i.7", i8* %"strptr.18", i32 %".56")
  %"i.9" = load i32, i32* %"i"
  %".58" = add i32 %"i.9", 1
  store i32 %".58", i32* %"i"
  br label %"for_cond.3"
for_end.3:
  br label %"while_cond"
while_cond:
  %"contador" = load i32, i32* @"contador"
  %".62" = icmp slt i32 %"contador", 5
  br i1 %".62", label %"while_body", label %"while_end"
while_body:
  %"strptr.20" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.20", i32 0, i32 0
  %"contador.1" = load i32, i32* @"contador"
  %"strptr.21" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.21", i32 0, i32 0
  %".64" = call i32 (i8*, ...) @"printf"(i8* %"strptr.21", i8* %"strptr.20", i32 %"contador.1")
  %"contador.2" = load i32, i32* @"contador"
  %".65" = add i32 %"contador.2", 1
  store i32 %".65", i32* @"contador"
  br label %"while_cond"
while_end:
  br label %"while_cond.1"
while_cond.1:
  br i1 1, label %"while_body.1", label %"while_end.1"
while_body.1:
  %"j" = load i32, i32* @"j"
  %".70" = icmp eq i32 %"j", 3
  br i1 %".70", label %"if_then.4", label %"if_else.4"
while_end.1:
  br label %"while_cond.2"
if_then.4:
  br label %"while_end.1"
if_else.4:
  br label %"if_merge.4"
if_merge.4:
  %"strptr.22" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.22", i32 0, i32 0
  %"j.1" = load i32, i32* @"j"
  %"strptr.23" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.23", i32 0, i32 0
  %".74" = call i32 (i8*, ...) @"printf"(i8* %"strptr.23", i8* %"strptr.22", i32 %"j.1")
  %"j.2" = load i32, i32* @"j"
  %".75" = add i32 %"j.2", 1
  store i32 %".75", i32* @"j"
  br label %"while_cond.1"
while_cond.2:
  %"a" = load i32, i32* @"a"
  %".79" = icmp slt i32 %"a", 2
  br i1 %".79", label %"while_body.2", label %"while_end.2"
while_body.2:
  store i32 0, i32* %"b"
  br label %"while_cond.3"
while_end.2:
  ret void
while_cond.3:
  %"b.1" = load i32, i32* %"b"
  %".83" = icmp slt i32 %"b.1", 3
  br i1 %".83", label %"while_body.3", label %"while_end.3"
while_body.3:
  %"strptr.24" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.24", i32 0, i32 0
  %"a.1" = load i32, i32* @"a"
  %"strptr.25" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.25", i32 0, i32 0
  %"b.2" = load i32, i32* %"b"
  %"strptr.26" = getelementptr inbounds [13 x i8], [13 x i8]* @"str.26", i32 0, i32 0
  %".85" = call i32 (i8*, ...) @"printf"(i8* %"strptr.26", i8* %"strptr.24", i32 %"a.1", i8* %"strptr.25", i32 %"b.2")
  %"b.3" = load i32, i32* %"b"
  %".86" = add i32 %"b.3", 1
  store i32 %".86", i32* %"b"
  br label %"while_cond.3"
while_end.3:
  %"a.2" = load i32, i32* @"a"
  %".89" = add i32 %"a.2", 1
  store i32 %".89", i32* @"a"
  br label %"while_cond.2"
}

@"str" = private constant [15 x i8] c"Maior de idade\00"
@"str.1" = private constant [4 x i8] c"%s\0a\00"
@"str.2" = private constant [15 x i8] c"Menor de idade\00"
@"str.3" = private constant [4 x i8] c"%s\0a\00"
@"str.4" = private constant [2 x i8] c"A\00"
@"str.5" = private constant [4 x i8] c"%s\0a\00"
@"str.6" = private constant [2 x i8] c"B\00"
@"str.7" = private constant [4 x i8] c"%s\0a\00"
@"str.8" = private constant [2 x i8] c"C\00"
@"str.9" = private constant [4 x i8] c"%s\0a\00"
@"str.10" = private constant [2 x i8] c"F\00"
@"str.11" = private constant [4 x i8] c"%s\0a\00"
@"str.12" = private constant [11 x i8] c"Soma 1-10:\00"
@"str.13" = private constant [7 x i8] c"%s %d\0a\00"
@"str.14" = private constant [3 x i8] c"x:\00"
@"str.15" = private constant [3 x i8] c"y:\00"
@"str.16" = private constant [13 x i8] c"%s %d %s %d\0a\00"
@"str.17" = private constant [9 x i8] c"numeros[\00"
@"str.18" = private constant [3 x i8] c"]:\00"
@"str.19" = private constant [13 x i8] c"%s %d %s %d\0a\00"
@"str.20" = private constant [10 x i8] c"Contador:\00"
@"str.21" = private constant [7 x i8] c"%s %d\0a\00"
@"str.22" = private constant [3 x i8] c"j:\00"
@"str.23" = private constant [7 x i8] c"%s %d\0a\00"
@"str.24" = private constant [3 x i8] c"a:\00"
@"str.25" = private constant [3 x i8] c"b:\00"
@"str.26" = private constant [13 x i8] c"%s %d %s %d\0a\00"
define i32 @"main"()
{
entry:
  %".2" = call i32 @"SetConsoleOutputCP"(i32 65001)
  call void @"__jss_global_init"()
  ret i32 0
}
