"""6.WAP TO ENTER TWO DIFFERENT SETS WITH STRING ELEMNTS COMBINE BOTH THE SETS REMOVE ANY DUPLICATES R PRESENT,PRINT NEW SET"""
def combine_sets(s1, s2):
    new_set = s1.union(s2)
    return new_set


set1 = eval(input("Enter First Set: "))
set2 = eval(input("Enter Second Set: "))

result = combine_sets(set1, set2)

print("New Set after combining:", result)