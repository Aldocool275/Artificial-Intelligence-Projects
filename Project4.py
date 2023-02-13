E={0,1,2,3,4,5}
N={2,4,6,8}
union=E.union(N)
intersection=E.intersection(N)
diff=N.difference(E)
symm_diff=E.symmetric_difference(N)
print("Union of E and N is",union)
print("Intersection of E and N is",intersection)
print("Difference of E and N is",diff)
print("Symmetric Difference of E and N is",symm_diff)
