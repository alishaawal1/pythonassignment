# Write a Python program to count the number of strings where the string length is 2 or more.
#The first and last character are same from a given list of strings.
#Sample: list1 = [‘aba’,’121’,’kgf’,’abc’]
name = ["alisha","hey","Nepali","995249","helloh"]
total = 0
for a in range(0,len(name)):
    b = name[a]
    if len(b)>=2:
        first = b[0]
        last = b[len(b)-1]
        if first == last:
            total = total+1
print("The Number of string having first and last character same and string length 2 is:",total)