import random, json

# Re-verify the two structural claims used in Step 2, now also checking the
# full "ell" statement in the degenerate model where no two distinct cycles are
# rationally equivalent (so the only representative of a class is the class
# itself, and ell(gamma) = lev(gamma)). In that model the target inequality
# ell(A+B) <= max(ell(A), ell(B)) is exactly lev(A+B) <= max(lev(A), lev(B)).
random.seed(987654321)

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
    return {s: random.randint(-5, 5) for s in subs}

trials = 0
for d in range(0, 6):
    for _ in range(30000):
        A = random_cycle(d, 8)
        B = random_cycle(d, 8)
        C = add(A, B)
        # target inequality in the no-equivalence model:
        assert lev(C, d) <= max(lev(A, d), lev(B, d)), (d, A, B)
        # structural claim: every component of A+B is a component of A or B
        for s in C:
            assert s in A or s in B, (d, s, A, B)
        # lower bound lev >= -1
        assert lev(A, d) >= -1 and lev(B, d) >= -1 and lev(C, d) >= -1
        trials += 1

print("RESULT: " + json.dumps({"ok": True, "trials": trials}, sort_keys=True))
