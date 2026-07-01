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

@"a" = internal global i32 10
@"b" = internal global i32 3
@"x" = internal global i32 5
@"r" = internal global double 0x400c000000000000
@"t" = internal global i1 1
@"f" = internal global i1 0
@"n1" = internal global i32 10
@"n2" = internal global i32 5
@"val" = internal global i32 10
define void @"__jss_global_init"()
{
entry:
  %"strptr" = getelementptr inbounds [6 x i8], [6 x i8]* @"str", i32 0, i32 0
  %"a" = load i32, i32* @"a"
  %"b" = load i32, i32* @"b"
  %".2" = add i32 %"a", %"b"
  %"strptr.1" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.1", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %"strptr.1", i8* %"strptr", i32 %".2")
  %"strptr.2" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.2", i32 0, i32 0
  %"a.1" = load i32, i32* @"a"
  %"b.1" = load i32, i32* @"b"
  %".4" = sub i32 %"a.1", %"b.1"
  %"strptr.3" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.3", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %"strptr.3", i8* %"strptr.2", i32 %".4")
  %"strptr.4" = getelementptr inbounds [15 x i8], [15 x i8]* @"str.4", i32 0, i32 0
  %"a.2" = load i32, i32* @"a"
  %"b.2" = load i32, i32* @"b"
  %".6" = mul i32 %"a.2", %"b.2"
  %"strptr.5" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.5", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"strptr.5", i8* %"strptr.4", i32 %".6")
  %"strptr.6" = getelementptr inbounds [9 x i8], [9 x i8]* @"str.6", i32 0, i32 0
  %"a.3" = load i32, i32* @"a"
  %"b.3" = load i32, i32* @"b"
  %".8" = sdiv i32 %"a.3", %"b.3"
  %"strptr.7" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.7", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %"strptr.7", i8* %"strptr.6", i32 %".8")
  %"strptr.8" = getelementptr inbounds [8 x i8], [8 x i8]* @"str.8", i32 0, i32 0
  %"a.4" = load i32, i32* @"a"
  %"b.4" = load i32, i32* @"b"
  %".10" = srem i32 %"a.4", %"b.4"
  %"strptr.9" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.9", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %"strptr.9", i8* %"strptr.8", i32 %".10")
  %"strptr.10" = getelementptr inbounds [10 x i8], [10 x i8]* @"str.10", i32 0, i32 0
  %"a.5" = load i32, i32* @"a"
  %"b.5" = load i32, i32* @"b"
  %".12" = call i32 @"__jss_pow_i32"(i32 %"b.5", i32 2)
  %".13" = call i32 @"__jss_pow_i32"(i32 %"a.5", i32 %".12")
  %"strptr.11" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.11", i32 0, i32 0
  %".14" = call i32 (i8*, ...) @"printf"(i8* %"strptr.11", i8* %"strptr.10", i32 %".13")
  %"strptr.12" = getelementptr inbounds [9 x i8], [9 x i8]* @"str.12", i32 0, i32 0
  %"x" = load i32, i32* @"x"
  %".15" = sub i32 0, %"x"
  %"strptr.13" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.13", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"strptr.13", i8* %"strptr.12", i32 %".15")
  %"strptr.14" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.14", i32 0, i32 0
  %"x.1" = load i32, i32* @"x"
  %".17" = add i32 %"x.1", 1
  store i32 %".17", i32* @"x"
  %"strptr.15" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.15", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %"strptr.15", i8* %"strptr.14", i32 %".17")
  %"strptr.16" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.16", i32 0, i32 0
  %"x.2" = load i32, i32* @"x"
  %".20" = sub i32 %"x.2", 1
  store i32 %".20", i32* @"x"
  %"strptr.17" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.17", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"printf"(i8* %"strptr.17", i8* %"strptr.16", i32 %".20")
  %"strptr.18" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.18", i32 0, i32 0
  %"a.6" = load i32, i32* @"a"
  %"r" = load double, double* @"r"
  %".23" = sitofp i32 %"a.6" to double
  %".24" = fadd double %".23", %"r"
  %"strptr.19" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.19", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %"strptr.19", i8* %"strptr.18", double %".24")
  %"strptr.20" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.20", i32 0, i32 0
  %"t" = load i1, i1* @"t"
  br i1 %"t", label %"and_rhs", label %"and_end"
and_rhs:
  %"f" = load i1, i1* @"f"
  br label %"and_end"
and_end:
  %"andtmp" = phi  i1 [0, %"entry"], [%"f", %"and_rhs"]
  %"strptr.21" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.21", i32 0, i32 0
  %"strptr.22" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.22", i32 0, i32 0
  %".28" = select  i1 %"andtmp", i8* %"strptr.21", i8* %"strptr.22"
  %"strptr.23" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.23", i32 0, i32 0
  %".29" = call i32 (i8*, ...) @"printf"(i8* %"strptr.23", i8* %"strptr.20", i8* %".28")
  %"strptr.24" = getelementptr inbounds [4 x i8], [4 x i8]* @"str.24", i32 0, i32 0
  %"t.1" = load i1, i1* @"t"
  br i1 %"t.1", label %"or_end", label %"or_rhs"
or_rhs:
  %"f.1" = load i1, i1* @"f"
  br label %"or_end"
or_end:
  %"ortmp" = phi  i1 [1, %"and_end"], [%"f.1", %"or_rhs"]
  %"strptr.25" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.25", i32 0, i32 0
  %"strptr.26" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.26", i32 0, i32 0
  %".32" = select  i1 %"ortmp", i8* %"strptr.25", i8* %"strptr.26"
  %"strptr.27" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.27", i32 0, i32 0
  %".33" = call i32 (i8*, ...) @"printf"(i8* %"strptr.27", i8* %"strptr.24", i8* %".32")
  %"strptr.28" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.28", i32 0, i32 0
  %"t.2" = load i1, i1* @"t"
  %".34" = xor i1 %"t.2", -1
  %"strptr.29" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.29", i32 0, i32 0
  %"strptr.30" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.30", i32 0, i32 0
  %".35" = select  i1 %".34", i8* %"strptr.29", i8* %"strptr.30"
  %"strptr.31" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.31", i32 0, i32 0
  %".36" = call i32 (i8*, ...) @"printf"(i8* %"strptr.31", i8* %"strptr.28", i8* %".35")
  %"strptr.32" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.32", i32 0, i32 0
  %"n1" = load i32, i32* @"n1"
  %"n2" = load i32, i32* @"n2"
  %".37" = icmp sgt i32 %"n1", %"n2"
  %"strptr.33" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.33", i32 0, i32 0
  %"strptr.34" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.34", i32 0, i32 0
  %".38" = select  i1 %".37", i8* %"strptr.33", i8* %"strptr.34"
  %"strptr.35" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.35", i32 0, i32 0
  %".39" = call i32 (i8*, ...) @"printf"(i8* %"strptr.35", i8* %"strptr.32", i8* %".38")
  %"strptr.36" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.36", i32 0, i32 0
  %"n1.1" = load i32, i32* @"n1"
  %"n2.1" = load i32, i32* @"n2"
  %".40" = icmp slt i32 %"n1.1", %"n2.1"
  %"strptr.37" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.37", i32 0, i32 0
  %"strptr.38" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.38", i32 0, i32 0
  %".41" = select  i1 %".40", i8* %"strptr.37", i8* %"strptr.38"
  %"strptr.39" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.39", i32 0, i32 0
  %".42" = call i32 (i8*, ...) @"printf"(i8* %"strptr.39", i8* %"strptr.36", i8* %".41")
  %"strptr.40" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.40", i32 0, i32 0
  %"n1.2" = load i32, i32* @"n1"
  %"n2.2" = load i32, i32* @"n2"
  %".43" = icmp eq i32 %"n1.2", %"n2.2"
  %"strptr.41" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.41", i32 0, i32 0
  %"strptr.42" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.42", i32 0, i32 0
  %".44" = select  i1 %".43", i8* %"strptr.41", i8* %"strptr.42"
  %"strptr.43" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.43", i32 0, i32 0
  %".45" = call i32 (i8*, ...) @"printf"(i8* %"strptr.43", i8* %"strptr.40", i8* %".44")
  %"strptr.44" = getelementptr inbounds [11 x i8], [11 x i8]* @"str.44", i32 0, i32 0
  %"n1.3" = load i32, i32* @"n1"
  %"n2.3" = load i32, i32* @"n2"
  %".46" = icmp ne i32 %"n1.3", %"n2.3"
  %"strptr.45" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.45", i32 0, i32 0
  %"strptr.46" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.46", i32 0, i32 0
  %".47" = select  i1 %".46", i8* %"strptr.45", i8* %"strptr.46"
  %"strptr.47" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.47", i32 0, i32 0
  %".48" = call i32 (i8*, ...) @"printf"(i8* %"strptr.47", i8* %"strptr.44", i8* %".47")
  %"strptr.48" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.48", i32 0, i32 0
  %"n1.4" = load i32, i32* @"n1"
  %"n2.4" = load i32, i32* @"n2"
  %".49" = icmp sge i32 %"n1.4", %"n2.4"
  %"strptr.49" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.49", i32 0, i32 0
  %"strptr.50" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.50", i32 0, i32 0
  %".50" = select  i1 %".49", i8* %"strptr.49", i8* %"strptr.50"
  %"strptr.51" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.51", i32 0, i32 0
  %".51" = call i32 (i8*, ...) @"printf"(i8* %"strptr.51", i8* %"strptr.48", i8* %".50")
  %"strptr.52" = getelementptr inbounds [12 x i8], [12 x i8]* @"str.52", i32 0, i32 0
  %"n1.5" = load i32, i32* @"n1"
  %"n2.5" = load i32, i32* @"n2"
  %".52" = icmp sle i32 %"n1.5", %"n2.5"
  %"strptr.53" = getelementptr inbounds [5 x i8], [5 x i8]* @"str.53", i32 0, i32 0
  %"strptr.54" = getelementptr inbounds [6 x i8], [6 x i8]* @"str.54", i32 0, i32 0
  %".53" = select  i1 %".52", i8* %"strptr.53", i8* %"strptr.54"
  %"strptr.55" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.55", i32 0, i32 0
  %".54" = call i32 (i8*, ...) @"printf"(i8* %"strptr.55", i8* %"strptr.52", i8* %".53")
  %"val" = load i32, i32* @"val"
  %".55" = add i32 %"val", 5
  store i32 %".55", i32* @"val"
  %"strptr.56" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.56", i32 0, i32 0
  %"val.1" = load i32, i32* @"val"
  %"strptr.57" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.57", i32 0, i32 0
  %".57" = call i32 (i8*, ...) @"printf"(i8* %"strptr.57", i8* %"strptr.56", i32 %"val.1")
  %"val.2" = load i32, i32* @"val"
  %".58" = sub i32 %"val.2", 3
  store i32 %".58", i32* @"val"
  %"strptr.58" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.58", i32 0, i32 0
  %"val.3" = load i32, i32* @"val"
  %"strptr.59" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.59", i32 0, i32 0
  %".60" = call i32 (i8*, ...) @"printf"(i8* %"strptr.59", i8* %"strptr.58", i32 %"val.3")
  %"val.4" = load i32, i32* @"val"
  %".61" = mul i32 %"val.4", 2
  store i32 %".61", i32* @"val"
  %"strptr.60" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.60", i32 0, i32 0
  %"val.5" = load i32, i32* @"val"
  %"strptr.61" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.61", i32 0, i32 0
  %".63" = call i32 (i8*, ...) @"printf"(i8* %"strptr.61", i8* %"strptr.60", i32 %"val.5")
  %"val.6" = load i32, i32* @"val"
  %".64" = sdiv i32 %"val.6", 4
  store i32 %".64", i32* @"val"
  %"strptr.62" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.62", i32 0, i32 0
  %"val.7" = load i32, i32* @"val"
  %"strptr.63" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.63", i32 0, i32 0
  %".66" = call i32 (i8*, ...) @"printf"(i8* %"strptr.63", i8* %"strptr.62", i32 %"val.7")
  %"val.8" = load i32, i32* @"val"
  %".67" = srem i32 %"val.8", 4
  store i32 %".67", i32* @"val"
  %"strptr.64" = getelementptr inbounds [3 x i8], [3 x i8]* @"str.64", i32 0, i32 0
  %"val.9" = load i32, i32* @"val"
  %"strptr.65" = getelementptr inbounds [7 x i8], [7 x i8]* @"str.65", i32 0, i32 0
  %".69" = call i32 (i8*, ...) @"printf"(i8* %"strptr.65", i8* %"strptr.64", i32 %"val.9")
  ret void
}

@"str" = private constant [6 x i8] c"Soma:\00"
@"str.1" = private constant [7 x i8] c"%s %d\0a\00"
@"str.2" = private constant [11 x i8] c"Subtracao:\00"
@"str.3" = private constant [7 x i8] c"%s %d\0a\00"
@"str.4" = private constant [15 x i8] c"Multiplicacao:\00"
@"str.5" = private constant [7 x i8] c"%s %d\0a\00"
@"str.6" = private constant [9 x i8] c"Divisao:\00"
@"str.7" = private constant [7 x i8] c"%s %d\0a\00"
@"str.8" = private constant [8 x i8] c"Modulo:\00"
@"str.9" = private constant [7 x i8] c"%s %d\0a\00"
@"str.10" = private constant [10 x i8] c"Potencia:\00"
define i32 @"__jss_pow_i32"(i32 %".1", i32 %".2")
{
entry:
  %"result" = alloca i32
  %"i" = alloca i32
  store i32 1, i32* %"result"
  store i32 0, i32* %"i"
  br label %"cond"
cond:
  %"i.1" = load i32, i32* %"i"
  %".7" = icmp slt i32 %"i.1", %".2"
  br i1 %".7", label %"body", label %"exit"
body:
  %"res" = load i32, i32* %"result"
  %"new_res" = mul i32 %"res", %".1"
  store i32 %"new_res", i32* %"result"
  %"i_cur" = load i32, i32* %"i"
  %".10" = add i32 %"i_cur", 1
  store i32 %".10", i32* %"i"
  br label %"cond"
exit:
  %"final" = load i32, i32* %"result"
  ret i32 %"final"
}

@"str.11" = private constant [7 x i8] c"%s %d\0a\00"
@"str.12" = private constant [9 x i8] c"Negacao:\00"
@"str.13" = private constant [7 x i8] c"%s %d\0a\00"
@"str.14" = private constant [12 x i8] c"Incremento:\00"
@"str.15" = private constant [7 x i8] c"%s %d\0a\00"
@"str.16" = private constant [12 x i8] c"Decremento:\00"
@"str.17" = private constant [7 x i8] c"%s %d\0a\00"
@"str.18" = private constant [12 x i8] c"Int + Real:\00"
@"str.19" = private constant [7 x i8] c"%s %f\0a\00"
@"str.20" = private constant [5 x i8] c"AND:\00"
@"str.21" = private constant [5 x i8] c"true\00"
@"str.22" = private constant [6 x i8] c"false\00"
@"str.23" = private constant [7 x i8] c"%s %s\0a\00"
@"str.24" = private constant [4 x i8] c"OR:\00"
@"str.25" = private constant [5 x i8] c"true\00"
@"str.26" = private constant [6 x i8] c"false\00"
@"str.27" = private constant [7 x i8] c"%s %s\0a\00"
@"str.28" = private constant [5 x i8] c"NOT:\00"
@"str.29" = private constant [5 x i8] c"true\00"
@"str.30" = private constant [6 x i8] c"false\00"
@"str.31" = private constant [7 x i8] c"%s %s\0a\00"
@"str.32" = private constant [7 x i8] c"Maior:\00"
@"str.33" = private constant [5 x i8] c"true\00"
@"str.34" = private constant [6 x i8] c"false\00"
@"str.35" = private constant [7 x i8] c"%s %s\0a\00"
@"str.36" = private constant [7 x i8] c"Menor:\00"
@"str.37" = private constant [5 x i8] c"true\00"
@"str.38" = private constant [6 x i8] c"false\00"
@"str.39" = private constant [7 x i8] c"%s %s\0a\00"
@"str.40" = private constant [7 x i8] c"Igual:\00"
@"str.41" = private constant [5 x i8] c"true\00"
@"str.42" = private constant [6 x i8] c"false\00"
@"str.43" = private constant [7 x i8] c"%s %s\0a\00"
@"str.44" = private constant [11 x i8] c"Diferente:\00"
@"str.45" = private constant [5 x i8] c"true\00"
@"str.46" = private constant [6 x i8] c"false\00"
@"str.47" = private constant [7 x i8] c"%s %s\0a\00"
@"str.48" = private constant [12 x i8] c"MaiorIgual:\00"
@"str.49" = private constant [5 x i8] c"true\00"
@"str.50" = private constant [6 x i8] c"false\00"
@"str.51" = private constant [7 x i8] c"%s %s\0a\00"
@"str.52" = private constant [12 x i8] c"MenorIgual:\00"
@"str.53" = private constant [5 x i8] c"true\00"
@"str.54" = private constant [6 x i8] c"false\00"
@"str.55" = private constant [7 x i8] c"%s %s\0a\00"
@"str.56" = private constant [3 x i8] c"+=\00"
@"str.57" = private constant [7 x i8] c"%s %d\0a\00"
@"str.58" = private constant [3 x i8] c"-=\00"
@"str.59" = private constant [7 x i8] c"%s %d\0a\00"
@"str.60" = private constant [3 x i8] c"*=\00"
@"str.61" = private constant [7 x i8] c"%s %d\0a\00"
@"str.62" = private constant [3 x i8] c"/=\00"
@"str.63" = private constant [7 x i8] c"%s %d\0a\00"
@"str.64" = private constant [3 x i8] c"%=\00"
@"str.65" = private constant [7 x i8] c"%s %d\0a\00"
define i32 @"main"()
{
entry:
  %".2" = call i32 @"SetConsoleOutputCP"(i32 65001)
  call void @"__jss_global_init"()
  ret i32 0
}
