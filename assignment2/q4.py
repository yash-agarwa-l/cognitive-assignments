# 4. Consider the following two sets, A and B, represen􏰀ng scores of two teams in mul􏰀ple matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23}
# WAP to perform the following opera􏰀ons using set func􏰀ons:
# i. Find the unique scores achieved by both teams (union of sets).
# ii. Iden􏰀fy the scores that are common to both teams (intersec􏰀on of sets).
# iii. Find the scores that are exclusive to each team (symmetric difference).
# iv. Check if the scores of team A are a subset of team B, and if team B's scores are
# a superset of team A.
# v. Remove a specific score 𝑋 (input by the user) from set A if it exists. If not, print
# a message saying it is not present.


A = {34, 56, 78, 90}
B = {78, 45, 90, 23}


unique_scores = A.union(B)
print(f"Unique scores (Union of A and B): {unique_scores}")


common_scores = A.intersection(B)
print(f"Common scores (Intersection of A and B): {common_scores}")


exclusive_scores = A.symmetric_difference(B)
print(f"Exclusive scores (Symmetric Difference): {exclusive_scores}")

is_A_subset_B = A.issubset(B)
is_B_superset_A = B.issuperset(A)
print(f"Is team A's scores a subset of team B? {is_A_subset_B}")
print(f"Is team B's scores a superset of team A? {is_B_superset_A}")


# v.  Remove a specific score 𝑋 (input by the user) from set A if it exists. If not, print a message saying it is not present.
X = int(input("Enter the score to remove from set A: "))
if X in A:
    A.remove(X)
    print(f"Score {X} removed from set A. Updated set A: {A}")
else:
    print(f"Score {X} is not present in set A.")
