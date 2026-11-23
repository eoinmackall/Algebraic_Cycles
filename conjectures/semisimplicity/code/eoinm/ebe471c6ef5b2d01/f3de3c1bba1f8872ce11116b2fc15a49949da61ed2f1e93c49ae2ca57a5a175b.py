import random, json

p = 7

def rank(M, rows, cols):
    if rows == 0 or cols == 0: return 0
    M = [[x % p for x in r] for r in M]
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p-2, p)
        M[r] = [(x*inv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f*M[r][j]) % p for j in range(cols)]
        r += 1
        if r == rows: break
    return r

def mul(A,B,ra,ca,cb):
    return [[sum(A[i][t]*B[t][j] for t in range(ca)) % p for j in range(cb)] for i in range(ra)]

def rref(M, rows, cols):
    A=[[x%p for x in r] for r in M]; piv={} ; r=0
    for c in range(cols):
        pv=None
        for i in range(r,rows):
            if A[i][c]%p: pv=i;break
        if pv is None: continue
        A[r],A[pv]=A[pv],A[r]
        inv=pow(A[r][c],p-2,p); A[r]=[(x*inv)%p for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(A[i][j]-f*A[r][j])%p for j in range(cols)]
        piv[c]=r; r+=1
    return A, piv

def solve(M, rows, cols, rhs):
    A=[M[i][:]+[rhs[i]] for i in range(rows)]
    A,piv=rref(A,rows,cols+1)
    for i in range(rows):
        if all(v%p==0 for v in A[i][:cols]) and A[i][cols]%p: return None
    x=[0]*cols
    for c,ri in piv.items(): x[c]=A[ri][cols]%p
    free=[c for c in range(cols) if c not in piv]
    basis=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for c,ri in piv.items(): v[c]=(-A[ri][fc]*pow(1,1,p))%p
        basis.append(v)
    return x, basis

def nullspace(M, rows, cols):
    if cols==0: return []
    A,piv=rref(M,rows,cols)
    free=[c for c in range(cols) if c not in piv]
    out=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for c,ri in piv.items(): v[c]=(-A[ri][fc])%p
        out.append(v)
    return out

random.seed(98765)
stats={}
for (n0,ne) in [(1,2),(2,3),(3,4),(2,2),(3,5),(4,5),(4,6)]:
    checked=0; good=0; bad=[]
    att=0
    while checked<800 and att<300000:
        att+=1
        Lm=[[random.randrange(p) for _ in range(n0)] for _ in range(ne)]
        if rank(Lm,ne,n0)!=n0: continue
        G=[[random.randrange(p) for _ in range(n0)] for _ in range(n0)]
        if rank(G,n0,n0)!=n0: continue
        Lp=[[random.randrange(p) for _ in range(ne)] for _ in range(n0)]
        if rank(mul(Lp,Lm,n0,ne,n0),n0,n0)!=n0: continue
        M=mul(G,Lp,n0,n0,ne)
        LmT=[[Lm[i][j] for i in range(ne)] for j in range(n0)]
        sols=[]; ok=True
        for j in range(ne):
            rhs=[M[i][j] for i in range(n0)]
            s=solve(LmT,n0,ne,rhs)
            if s is None: ok=False;break
            sols.append(s)
        if not ok: continue
        B=None
        for _ in range(40):
            Bt=[[0]*ne for _ in range(ne)]
            for j in range(ne):
                xp,basis=sols[j]; col=xp[:]
                for v in basis:
                    c=random.randrange(p)
                    if c: col=[(col[t]+c*v[t])%p for t in range(ne)]
                for i in range(ne): Bt[i][j]=col[i]
            if rank(Bt,ne,ne)==ne: B=Bt;break
        if B is None: continue
        assert mul(LmT,B,n0,ne,ne)==M, "adjunction failed"
        # also assert beta, gamma perfect (invertible) and composite injective
        assert rank(B,ne,ne)==ne and rank(G,n0,n0)==n0 and rank(mul(Lp,Lm,n0,ne,n0),n0,n0)==n0
        checked+=1
        W=nullspace(Lp,n0,ne); k=len(W)
        Gram=[[sum(W[i][x]*B[x][y]*W[j][y] for y in range(ne) for x in range(ne))%p for j in range(k)] for i in range(k)]
        if k>0 and rank(Gram,k,k)!=k: bad.append((n0,ne,k))
        else: good+=1
    stats["n0=%d,ne=%d"%(n0,ne)]={"checked":checked,"nondeg":good,"failures":len(bad)}
print("RESULT: "+json.dumps({"prime":p,"seed":98765,"stats":stats}))
