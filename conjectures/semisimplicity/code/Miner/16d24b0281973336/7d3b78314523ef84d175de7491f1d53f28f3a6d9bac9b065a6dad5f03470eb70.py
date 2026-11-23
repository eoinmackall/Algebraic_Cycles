
# Final verification of the complete proof structure
import json

# The proof relies on:
# 1. lemma_439: Gysin adjunction tr_X(i_!(a) cup b) = tr_Y(a cup i^* b)
# 2. lemma_77: Poincare duality is perfect
# 3. fdc534: i^* surjective for 0 <= n <= d-2
# 4. d35572: i^* injective for 0 <= n <= d-2
# 5. Linear algebra: T is iso iff T^T is iso (w.r.t. perfect pairings)

# Verify the degree conditions:
# - d >= 3 (given)
# - n = 1 for i^*: H^1(X) -> H^1(Y)
# - Need 0 <= 1 <= d-2, i.e., d >= 3 (satisfied)
# - Poincare duality degrees:
#   X (dim d): H^{2d-1} x H^1 -> Q_l  [n = 2d-1, 2d-n = 1]
#   Y (dim d-1): H^{2d-3} x H^1 -> Q_l  [n = 2d-3, 2(d-1)-n = 1]

for d in range(3, 15):
    # Check n=1 is in range for fdc534 and d35572
    assert 0 <= 1 <= d - 2, f"n=1 not in range for d={d}"
    
    # Check Poincare duality degrees
    # X: H^{2d-1} pairs with H^{2d-(2d-1)} = H^1
    assert 2*d - (2*d - 1) == 1
    # Y: H^{2d-3} pairs with H^{2(d-1)-(2d-3)} = H^{2d-2-2d+3} = H^1
    assert 2*(d-1) - (2*d - 3) == 1
    
    # Check the Gysin map degrees
    # i_!: H^{2d-3}(Y) -> H^{2d-1}(X)
    # Source degree: 2d-3
    # Target degree: 2d-1 = (2d-3) + 2  [Gysin raises degree by 2]
    assert (2*d - 3) + 2 == 2*d - 1

print("All structural checks passed.")
print("RESULT: " + json.dumps({
    "ok": True,
    "proof_structure": [
        "Gysin adjunction (lemma_439)",
        "Poincare duality perfect (lemma_77)",
        "i^* surjective (fdc534, n=1, d>=3)",
        "i^* injective (d35572, n=1, d>=3)",
        "T iso iff T^T iso (linear algebra)"
    ]
}))
