#Write a Python script to print a dictionary where the keys are 
#numbers between 1 and 15 (both included) and the values are square of keys.
dictionary = {}
for a in range(1,16):
    dictionary[a]=a*a
print(dictionary)