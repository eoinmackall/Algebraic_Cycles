import random, json
random.seed(0)

def lev(pairs, d):
    if not pairs:
        return -1
    return max(a + b - d for (a, b) in pairs)

def swap(pairs):
    return [(b, a) for (a, b) in pairs]

# Claim 1: lev(s_* Z) = lev(Z) for every d-cycle (modelled by list of (a,b) pairs).
# Claim 2: upper bound a+b-d <= d holds for all pairs with 0<=a,b<=d (so lev <= d).
# Claim 3: for pairs satisfying the geometric constraint a+b>=d (real subvarieties),
#          each term a+b-d is in [0,d], hence lev in [0,d]; lev(0)=-1.
ok = True
for d in range(1, 8):
    for _ in range(50000):
        n = random.randint(0, 6)
        pairs = [(random.randint(0, d), random.randint(0, d)) for _ in range(n)]
        if lev(pairs, d) != lev(swap(pairs), d):
            ok = False; print("FAIL lev invariance", d, pairs)
        if lev(pairs, d) > d:
            ok = False; print("FAIL upper bound", d, pairs)
        # geometrically-realizable pairs: enforce a+b>=d
        gpairs = [(max(a, d-b), b) for (a, b) in pairs]  # push into a+b>=d region
        for (a, b) in gpairs:
            if not (a + b >= d):
                ok = False; print("FAIL geometric constraint", d, a, b)
            if not (0 <= a + b - d <= d):
                ok = False; print("FAIL geometric term range", d, a, b)
        if not (-1 <= lev(gpairs, d) <= d):
            ok = False; print("FAIL geometric lev range", d, gpairs)
print("RESULT:", json.dumps({"lev_invariant_under_swap": ok}))
