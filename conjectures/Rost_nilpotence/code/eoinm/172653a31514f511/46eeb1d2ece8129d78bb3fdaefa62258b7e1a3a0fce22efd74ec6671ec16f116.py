
import json
# Final consolidated exact check of the two combinatorial facts the proof uses:
# (1) For d >= 0, every term dim p_1 Z_i + dim p_2 Z_i - d arising from an
#     integral component Z_i of a d-cycle on X x X (dim X = d) lies in {-d..d},
#     so the lev-values over representatives of a fixed class form a nonempty
#     bounded-below subset of Z (hence have a minimum);
# (2) -1 <= d - 1 for all d >= 0, so the zero cycle (lev = -1) gives
#     ell(0) <= -1 <= d - 1.
ok = True
for d in range(0, 100):
    terms = {a + b - d for a in range(0, d + 1) for b in range(0, d + 1)}
    ok &= all(-d <= t <= d for t in terms)
    ok &= (-1 <= d - 1)
print("RESULT: " + json.dumps({"ok": bool(ok)}, sort_keys=True))
