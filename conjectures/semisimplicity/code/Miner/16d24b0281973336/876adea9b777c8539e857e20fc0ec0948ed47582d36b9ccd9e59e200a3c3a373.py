
# Verify degree bookkeeping for the Gysin map i_!: H^{2d-3}(Y) -> H^{2d-1}(X)
# and the Poincare-duality adjoint degree.
for d in range(3, 8):
    n = 2*d - 3          # source degree of i_!
    n_out = n + 2        # target degree of i_!
    # Spark lemma: i_! in degree n injective iff i^* in degree 2d-n-2 surjective
    deg_i_star = 2*d - n - 2
    # Poincare duality:
    #   X (dim d): H^{n_out}(X) pairs with H^{2d - n_out}(X)
    #   Y (dim d-1): H^n(Y) pairs with H^{2(d-1) - n}(Y)
    dual_X = 2*d - n_out
    dual_Y = 2*(d-1) - n
    print(f"d={d}: i_!: H^{n}(Y)->H^{n_out}(X); Spark dual deg={deg_i_star}; "
          f"PD dual of H^{n_out}(X) is H^{dual_X}(X); PD dual of H^{n}(Y) is H^{dual_Y}(Y)")
    assert n_out == 2*d - 1
    assert deg_i_star == 1
    assert dual_X == 1
    assert dual_Y == 1
    assert 0 <= n <= 2*d - 2      # Spark lemma range
    assert 0 <= 1 <= d - 2        # fdc534/d35572 range (needs d>=3)
print("All degree bookkeeping checks passed.")
print("RESULT: " + __import__("json").dumps({"ok": True}))
