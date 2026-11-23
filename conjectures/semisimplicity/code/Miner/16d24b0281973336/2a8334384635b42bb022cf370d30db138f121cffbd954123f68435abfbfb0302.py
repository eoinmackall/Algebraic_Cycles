# Final sanity check of the whole scalar pipeline used in the proof, in exact arithmetic.
from fractions import Fraction
import json
# For y in A: F y = q^{-m} y, F^{-1} y = q^m y.
# G(x,y) = beta(x, q^{-m} y) + q^{2m} beta(x, q^m y) = (q^{-m} + q^{3m}) beta(x,y).
# Check the coefficient simplification and nonvanelling in Q (char 0).
res = {}
for q in [2,3,5]:
    for m in [1,2]:
        coeff = Fraction(1, q**m) + q**(3*m)          # q^{-m} + q^{3m}
        factored = Fraction(1, q**m) * (1 + q**(4*m)) # q^{-m}(1+q^{4m})
        assert coeff == factored
        assert coeff != 0
        # simulate: if beta|_{W x W} nondegenerate, then coeff*beta nondegenerate
        # (radical of cB = radical of B when c != 0)
res["identity"] = "q^{-m}+q^{3m} = q^{-m}(1+q^{4m})"
res["nonzero"] = True
print("RESULT: " + json.dumps(res, sort_keys=True))
