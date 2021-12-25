#Write a Python program to update list element in a set.
#Sample: number = {1,2,3,4,5}
#Output: {1,2,3,4,5,7,8}
a=["alisha","python"]
b=[1,23,45]
set1=set(a)
set2=set(b)
print (set1)
set1.update(b)
print (set1)