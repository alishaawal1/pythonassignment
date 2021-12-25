# Write a Python program to multiplies all the items in a list.
def multiply(items):
    m=1
    for i in items:
        m*=i
    return m
print (multiply([1,2,4,5,21,34,32,54,78]))