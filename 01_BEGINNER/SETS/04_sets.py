# 7. Set operations (Most important part) :

# A. union(A U B)

a = {1,2,3,4}
b = {3,4,5,6}

print(a | b)
print(a.union(b))

    # Example:
x = {1,2,3,4,5,6}
y = {2,3,4,5,6,7}

print(x | y)
print(x.union(y))


# B. Intersection (A n B):

print(a & b)
print(a.intersection(b))

# C. Difference (A-B):

print(a - b)
print(a.difference(b))

print(b-a)
print(b.difference(a))


# D. Symmetric Difference:

print(a^b)
print(a.symmetric_difference(b)) # two option


# 8. CHECKING SET RELATIONSHIP:

p = {1,2,3,4,5,6,7,8,9,10} # superset
q = {1,2,3,4,5} # subset

c = {1,2,3,4,5} # superset
d= {1,2,3,4,5} # subset and both have sets equal elements contains.

# A. subset:
print(q.issubset(p))
print(c.issubset(d))

#B. superset:
print(p.issuperset(q))
print(c.issuperset(d))


 # C. Disjoint:

print(p.isdisjoint(q)) # know about the same elements in sets.
print(c.isdisjoint(d)) # output:False , they contain same elements on both sets.

# 9. iterating in sets:

fruits = {"apple","banana","mango","orange"}

for fruit in fruits:
    print(fruit)

# You can also use enumerate: 

for index,value in enumerate(fruits,1):
    print(f"{index}. {value}")


# 10. # A. Removed Duplicated:

fruits_01 = ["apple","mango","banana","apple","mango","orange"]

result = list(set(fruits_01))
print(result)

