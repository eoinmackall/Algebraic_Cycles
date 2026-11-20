import random, json

random.seed(20240517)

# Abstract model of the combinatorics of Fact 2:
# An "integral d-dimensional subvariety" of X x X is an abstract symbol carrying
# (a,b) = (dim p_1, dim p_2), with a,b in [0,d] and a+b >= d (the geometric fact
# Z_i subset p_1(Z_i) x p_2(Z_i) forces a+b >= dim Z_i = d).
# A d-cycle is a finite function from such symbols to nonzero integer coefficients.
# lev(cycle) = max over components of (a+b-d), lev(0) = -1.
# Claim checked: for all cycles A,B (d fixed), lev(A+B) <= max(lev(A), lev(B)).

def lev(cycle, d):
    terms = [a + b - d for (a, b) in cycle if cycle[(a, b)] != 0]
    return max(terms) if terms else -1

def add(A, B):
    D = {}
    for s in set(list(A.keys()) + list(B.keys())):
        c = A.get(s, 0) + B.get(s, 0)
        if c != 0:
            D[s] = c
    return D

def random_cycle(d, max_terms):
    subs = set()
    for _ in range(random.randint(1, max_terms)):
        a = random.randint(0, d)
        b = random.randint(d - a, d)
        subs.add((a, b))
    return {s: random.randint(-3, 3) for s in subs}

trials = 0
max_d = 5
for d in range(0, max_d + 1):
    for _ in range(40000):
        A = random_cycle(d, 6)
        B = random_cycle(d, 6)
        C = add(A, B)
        la, lb, lc = lev(A, d), lev(B, d), lev(C, d)
        assert lc <= max(la, lb), (d, A, B, C, la, lb, lc)
        assert la >= -1 and lb >= -1 and lc >= -1
        trials += 1

# Also verify the "component of A+B is a component of A or B" structural claim:
for d in range(0, max_d + 1):
    for _ in range(20000):
        A = random_cycle(d, 6)
        B = random_cycle(d, 6)
        C = add(A, B)
        for s in C:
            assert s in A or s in B, (d, A, B, C, s)
        trials += 1

print("RESULT: " + json.dumps({"ok": True, "trials": trials, "max_d": max_d}, sort_keys=True))
