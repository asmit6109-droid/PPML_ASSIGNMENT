"""5.WAP TO ENTER TWO SETS AND PERFORM ALL THE SET OPERATIONS ON IT"""
def set_operations(s1, s2):
    print("Union:", s1.union(s2))
    print("Intersection:", s1.intersection(s2))
    print("Difference (S1 - S2):", s1.difference(s2))
    print("Difference (S2 - S1):", s2.difference(s1))
    print("Symmetric Difference:", s1.symmetric_difference(s2))


set1 = eval(input("Enter First Set: "))
set2 = eval(input("Enter Second Set: "))

set_operations(set1, set2)