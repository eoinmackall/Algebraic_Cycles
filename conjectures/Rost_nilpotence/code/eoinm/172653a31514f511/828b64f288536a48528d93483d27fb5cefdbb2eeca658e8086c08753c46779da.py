
import json
def check(d):
    pairs = [(a,b) for a in range(d+1) for b in range(d+1) if a+b >= d]
    for (a,b) in pairs:
        top = (a==d and b==d)
        if top:
            assert a+b == 2*d
        else:
            assert a+b <= 2*d-1, (d,a,b)
    rest_pairs = [(a,b) for (a,b) in pairs if not (a==d and b==d)]
    if rest_pairs:
        levR = max(a+b-d for (a,b) in rest_pairs)
        assert levR <= d-1, (d, levR)
    top_pairs = [(a,b) for (a,b) in pairs if (a==d and b==d)]
    assert top_pairs == [(d,d)]
    assert -1 <= d-1
    return len(pairs)
res = {f"d={d}": check(d) for d in range(0,7)}
print("RESULT: " + json.dumps(res, sort_keys=True))
