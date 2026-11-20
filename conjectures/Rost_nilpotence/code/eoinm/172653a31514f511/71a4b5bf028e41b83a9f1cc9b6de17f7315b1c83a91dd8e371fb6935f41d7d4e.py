
import json

def s(x): return (x[1], x[0])
def sigma(x): return (x[2], x[1], x[0])
def q13(x): return (x[0], x[2])
def q12(x): return (x[0], x[1])
def q23(x): return (x[1], x[2])

pts = [(a,b,c) for a in range(2) for b in range(3) for c in range(2)]
ok1 = all(s(q13(x)) == q13(sigma(x)) for x in pts)   # s o q13 = q13 o sigma
ok2 = all(q12(sigma(x)) == s(q23(x)) for x in pts)   # q12 o sigma = s o q23
ok3 = all(q23(sigma(x)) == s(q12(x)) for x in pts)   # q23 o sigma = s o q12
assert ok1 and ok2 and ok3
print("RESULT: " + json.dumps({"s_q13_eq_q13_sigma": ok1, "q12_sigma_eq_s_q23": ok2, "q23_sigma_eq_s_q12": ok3}, sort_keys=True))
