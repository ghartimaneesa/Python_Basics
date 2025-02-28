#Set is an unordered collections with no duplicates data.
#basic use of the set is to eliminate the duplicate values.

#testo use hudaina
#it is also mutable and elements must be unique

s1 = {1,2,3,4}
s2 = {2,3,5,7,9,0}

#creating the set

empty_set= set()
p = [1,2,3,4,5,6,3,23,2,2,3]
set_from_list = set(p)
print(set_from_list)

#Adding elements
s1.add(10)
print(s1)

#removing elements and throws an error if not available
s1.remove(2)
print(s1)

#Discard and doesnot throws the error if not available
s1.discard(5)
print(s1)

#removes all the elements that is present in s1
s1.clear()
print(s1)

#set operations
s3 = {2,3,4,5,67}
s4 = {0,9,922,1,5,10}


print(s3|s4) #returns the union of two sets
print(s3.union(s4)) #alternative to find union of two sets

print(s3 & s4) #intersection of two sets
print(s3.intersection(s4))

print(s3 - s4) #difference
print(s3.difference(s4))

print(s3 ^ s4) #symmetric diference
print(s3.symmetric_difference(s4))

#checking membership

print(2 in s4)
print(0 not in s3)

#indentifying set length
print(len(s2))
print(s3.issubset(s4)) #checks whether the it is subset or not

#frozens sets (immutable sets)
fset = frozenset([1,2,3,4])
print(fset)

# # Uncommenting the below line will throw an error since frozen sets are immutable
# fset.add(5)
#it does not have attribute 'add'