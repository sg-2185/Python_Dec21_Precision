##Sets are lists with no duplicate entries.They are unordered and are iterable which has no duplicate elements.
##Set are ideal over lists where there is a need to check for a spcific
#element is a list of data.
##Set stores data as a hash table, hence its more efficient for searching
#an element in it.
## >* There are Immutable and Mutable sets

## >* Below is a demonstration of a Mutable or changable set
"""""""""""
set1 = {1,2,3,4}
print(set1)

s1 = set(["USA", "CHINA", "INDIA",])
print(s1)
s1.add("RUSSIA")
print(s1)

#Frozen or immutable sets - cannot be changed. Once created, they can only be read.
FS1 = frozenset([1,2,3])
FS1.add(5)
"""""
#Combine sets with the UNION function
S1 = {1,2,3}
S2 = {"A","B","C"}
S3 = S1.union(S2)
print(S3)
S4 = S1 | S2
#print(S4)

#Set operation intersect - get the common element between two sets
S11 = {1,2,3}
S12 = {1,4,5}
print(S11.intersection(S12))

#Set operation difference - gets the elements not in one over the another
S11 = {1,2,3}
S12 = {1,4,5}
print(S11.difference(S12))

#Set operation symmetric difference
SET1 = {0,1,2}
SET2 = {0,"A","B"}
print(SET1 ^ SET2)

#Discard & Remove -
# KeyError will be raised when REMOVE is used on
# non exsistant element in set
A1 = {"a","b","c","d"}
A1.discard("a")
print(A1)

A1 = {"a","b","c","d"}
A1.remove("a")
print(A1)

#Set operation Clear - remove all elements
S11 = {1,2,3}
print('Before Clear',S11)
S11.clear()
print('After Clear',S11)

#Set operation issuperset()
#checks if input is a superset of the given set
D1 = {1,2,3,4,5}
S1 = {2,3,4}
print(D1.issuperset(S1))

#loop through set elements
S1 = {"A","B","C","D","E"}
for c in S1:
    print(c)

#Using if....else with SET
R1 = {1,2,3,4}
R2 = {2,3,4}

if R1 > R2:
    print("R1 Has more elements")

if R1 == R2:
    print("R1 Has equal elements")
else:
    print("R1 and R2 are notequal in element count")




