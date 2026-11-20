
# Final confirmation of the two inequalities the proof rests on, stated generally.
# (1) If a d-dim component C of X x X is NOT top (i.e. not (dim p1 C = d and dim p2 C = d)),
#     then dim p1 C + dim p2 C <= 2d - 1.
# (2) lev(0) = -1 <= d - 1 for every d >= 0.
for d in range(0, 30):
    for a in range(d+1):
        for b in range(d+1):
            if not (a==d and b==d):
                assert a+b <= 2*d-1, (d,a,b)
    assert -1 <= d-1
print("RESULT: [\"inequalities (1) and (2) hold for all d in 0..29\"]")
