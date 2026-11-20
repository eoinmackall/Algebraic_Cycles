
# Final sanity check of the logical structure of the proof:
# target: (beta small in p2) => ell(alpha o beta) <= e
# route:  s_*(alpha o beta) = (s_* beta) o (s_* alpha)
#         s_* beta small in p1 (since p1 o s = p2)
#         73f003: (s_* beta) o (s_* alpha) has ell <= e
#         542b1a: ell(alpha o beta) = ell(s_*(alpha o beta))
# Verify the "smallness transfer" claim p1 o s = p2 on a point set.
def s(x): return (x[1], x[0])
def p1(x): return x[0]
def p2(x): return x[1]
pts = [(a,b) for a in range(3) for b in range(4)]
assert all(p1(s(x)) == p2(x) for x in pts)
print("p1 o s = p2: True")
print("RESULT: {\"p1_s_eq_p2\": true}")
