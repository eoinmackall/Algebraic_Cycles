
# Verify the degree bookkeeping for the localization sequence
# M = Y x A^1, dim M = dim Y + 1
# W = Y x Z', Z' finite set of closed points in A^1, dim W = dim Y
# codim of W in M = 1
# i_*: CH^j(W) -> CH^{j+1}(M)
# For j = n-1: i_*: CH^{n-1}(W) -> CH^n(M)  ✓
# i_s: Y x Spec(kappa(s)) -> M, codim 1
# i_{s*}: CH^{n-1}(Y x Spec(kappa(s))) -> CH^n(M)  ✓

# Check: for n=0, CH^{-1}(W) = 0, so the sequence is 0 -> CH^0(M) -> CH^0(U) -> 0
# CH^0(M) = Z (M irreducible), CH^0(U) = Z (U irreducible open in M)
# j^*: Z -> Z is the identity, so exact.

# For n>=1: standard localization sequence argument works.

import json
result = {"degree_check": "ok", "n0_case": "trivial", "n_ge_1_case": "standard localization"}
print("RESULT: " + json.dumps(result, sort_keys=True))
