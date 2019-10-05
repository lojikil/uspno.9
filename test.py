import uspno9

print "Variable declaration tests\n====="

f = uspno9.VariableDecAST("f", uspno9.ValueAST(int, 10), int)
print f.to_sexpr()
g = uspno9.VariableDecAST("g", uspno9.ValueAST(int), int)
h = uspno9.VariableDecAST("h", vtype=int)
print g.to_sexpr()
print h.to_sexpr()
j = uspno9.VariableDecAST("j")
print j.to_sexpr()

print "\nif-form test\n====="

cond0 = uspno9.FunctionCallAST("<", [uspno9.VarRefAST("f", int),
                                     uspno9.VarRefAST("g", int,
                                                      symbolic=True)],
                                     bool)
then0 = uspno9.FunctionCallAST("print", [uspno9.ValueAST(str, "then")], str)
else0 = uspno9.FunctionCallAST("print", [uspno9.ValueAST(str, "else")], str)
if0 = uspno9.IfAST(cond0, then0, else0)

print if0.to_sexpr()

print "\ninteger logic tests\n======"

a = uspno9.ValueAST.new_integer(9)
s = uspno9.ValueAST.new_integer(10)

z = a < s
x = a > s
c = a <= s
v = a >= s
b = a != s
n = a == s

res = [z,x,c,v,b,n]

for r in res:
    print r.value, r.trace


print "\narithmatic tests\n====="

jj = uspno9.ValueAST.new_symbolic_integer()

cg = a + s
ch = a + cg
cj = jj + a
ck = cj + ch

print cg.value, cg.trace
print ch.value, ch.trace
print cj.value, cj.trace
print ck.value, ck.trace
