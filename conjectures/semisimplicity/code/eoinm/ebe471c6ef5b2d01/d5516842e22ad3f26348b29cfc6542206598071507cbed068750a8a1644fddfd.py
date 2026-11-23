import random, json

p = 2

def rank(M, rows, cols):
    if rows == 0 or cols == 0: return 0
    M = [r[:] for r in M]
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c]: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][c]:
                M[i] = [M[i][j] ^ M[r][j] for j in range(cols)]
        r += 1
        if r == rows: break
    return r

def mul(A,B,ra,ca,cb):
    return [[sum(A[i][t]&B[t][j] for t in range(ca))&1 for j in range(cb)] for i in range(ra)]

def rref(M, rows, cols):
    A=[r[:] for r in M]; piv={} ; r=0
    for c in range(cols):
        pv=None
        for i in range(r,rows):
            if A[i][c]: pv=i;break
        if pv is None: continue
        A[r],A[pv]=A[pv],A[r]
        for i in range(rows):
            if i!=r and A[i][c]: A[i]=[A[i][j]^A[r][j] for j in range(cols)]
        piv[c]=r; r+=1
    return A, piv

def solve(M, rows, cols, rhs):
    # solutions x (cols) of M x = rhs over F2 ; return (particular, list of nullspace basis) or None
    A=[M[i][:]+[rhs[i]] for i in range(rows)]
    A,piv=rref(A,rows,cols+1)
    for i in range(rows):
        if all(v==0 for v in A[i][:cols]) and A[i][cols]==1: return None
    x=[0]*cols
    for c,ri in piv.items(): x[c]=A[ri][cols]
    free=[c for c in range(cols) if c not in piv]
    basis=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for c,ri in piv.items(): v[c]=A[ri][fc]
        basis.append(v)
    return x, basis

def nullspace(M, rows, cols):
    if cols==0: return []
    A,piv=rref(M,rows,cols)
    free=[c for c in range(cols) if c not in piv]
    out=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for c,ri in piv.items(): v[c]=A[ri][fc]
        out.append(v)
    return out

random.seed(20240501)
trials_per=3000
stats={}
for (n0,ne) in [(1,1),(1,2),(2,2),(2,3),(3,3),(2,4),(3,4),(4,4),(3,5)]:
    good=0; checked=0; bad=[]
    att=0
    while good<trials_per and att<200000:
        att+=1
        # random injective Lm (ne x n0)
        Lm=[[random.randrange(p) for _ in range(n0)] for _ in range(ne)]
        if rank(Lm,ne,n0)!=n0: continue
        # random invertible G (n0 x n0)
        G=[[random.randrange(p) for _ in range(n0)] for _ in range(n0)]
        if rank(G,n0,n0)!=n0: continue
        # random Lp (n0 x ne) with Lp*Lm invertible
        Lp=[[random.randrange(p) for _ in range(ne)] for _ in range(n0)]
        if rank(mul(Lp,Lm,n0,ne,n0),n0,n0)!=n0: continue
        M=mul(G,Lp,n0,n0,ne)          # target n0 x ne
        LmT=[[Lm[i][j] for i in range(ne)] for j in range(n0)]   # n0 x ne
        # solve LmT * B = M columnwise
        sols=[]
        ok=True
        for j in range(ne):
            rhs=[M[i][j] for i in range(n0)]
            s=solve(LmT,n0,ne,rhs)
            if s is None: ok=False;break
            sols.append(s)
        if not ok: continue
        # randomize nullspace parts, require B invertible
        found=None
        for _ in range(60):
            B=[[0]*ne for _ in range(ne)]
            for j in range(ne):
                xp,basis=sols[j]
                col=xp[:]
                for v in basis:
                    if random.randrange(2): col=[col[t]^v[t] for t in range(ne)]
                for i in range(ne): B[i][j]=col[i]
            if rank(B,ne,ne)==ne: found=B;break
        if found is None: continue
        B=found
        # verify adjunction beta(Lm a,b)=gamma(a,Lp b):  Lm^T B == G Lp
        assert mul(LmT,B,n0,ne,ne)==M
        checked+=1
        W=nullspace(Lp,n0,ne)
        k=len(W)
        Gram=[[sum(W[i][x]&B[x][y]&W[j][y] for y in range(ne) for x in range(ne))&1 for j in range(k)] for i in range(k)]
        if k>0 and rank(Gram,k,k)!=k:
            bad.append((n0,ne,k,Lm,Lp,B,G))
        else:
            good+=1
    stats[f"n0={n0},ne={ne}"]={"instances_checked":checked,"nondegenerate":good,"failures":len(bad)}

print("RESULT: "+json.dumps({"prime":p,"seed":20240501,"stats":stats}))
