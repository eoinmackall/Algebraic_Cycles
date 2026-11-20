# Final verification of the two structural facts used in the proof, stated cleanly.
import random, json
random.seed(1)

def lev(pairs, d):
    return -1 if not pairs else max(a + b - d for (a, b) in pairs)

def swap(pairs):
    return [(b, a) for (a, b) in pairs]

# Fact A: lev(s_* Z) = lev(Z)  (p1 o s = p2, p2 o s = p1)
# Fact B: the set of representatives of s_* gamma is exactly {s_* Z : Z rep of gamma},
#         which at the lev level means: min over W in swap(Rep) of lev(W)
#         equals min over Z in Rep of lev(s_* Z) = min over Z in Rep of lev(Z).
# We simulate: pick a "Rep" set of cycles, form its swap-image, compare the minima.
ok = True
for d in range(1, 7):
    for _ in range(30000):
        m = random.randint(1, 8)
        Rep = [[(random.randint(0, d), random.randint(0, d)) for _ in range(random.randint(0, 5))]
               for _ in range(m)]
        ell_gamma = min(lev(Z, d) for Z in Rep)
        Rep_s = [swap(Z) for Z in Rep]          # representatives of s_* gamma
        ell_sgamma = min(lev(W, d) for W in Rep_s)
        if ell_gamma != ell_sgamma:
            ok = False; print("FAIL", d, ell_gamma, ell_sgamma)
print("RESULT:", json.dumps({"ell_invariant_under_swap": ok}))
