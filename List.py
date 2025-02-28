# #Here the list can hold the multiple values.
# #list are created by using []
# #lists are ordered, changable and allow the duplicate values
# #Here, in list we can change, add, remove the itrems in the list after it has been created.

# #Here, it stores the single varaiable.
x = 10

# # List

y = [10,1,2, 3]
z = ["manisha","Gharti","Infinite"]
a = [10,"maniasha",10.5,10]

print(a[1])
print(type(a))

# #List Methods in python

cities = ["Kathmandu", "Bhaktapur","Lalitpur","Banepa"] 
#list.append(a)
cities.append("Kritipur")
print(cities)

# #list.insert(i,x)
# #here if i want to insert the value into the specific location then i use insert method give the index where i want to insert the particular value
cities.insert(0,"manakamana")
print(cities)

# #list.remove(a): here we have to specify the value that we want to remove.
cities.remove("Lalitpur")
print(cities)

# #list.pop : here we can provide the index of the particular vlauee that we want to remove from the list
cities.pop(1)
print(cities)

#list.index : i want to get the index of the particular item in the list then we use list.index
cities.append("manakamana")
print(cities)

print(cities.index("manakamana"))

#list.count
print(cities.count("manakamana"))

#list.sort
cities.sort()
cities.reverse()

print(cities)
cities.copy()
cities.remove("manakamana")
print(cities)

