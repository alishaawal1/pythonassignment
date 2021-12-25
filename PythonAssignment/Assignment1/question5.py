#Write a Python program to print a specified list after removing the 4th elements.
abc = ["alisha","hey","Nepali","995249","helloh","98130","ksd","654","copy","append"]
abc_new =[]
for i in range(0,len(abc)):
    if i==0 or i==4 or i==5:
        continue
    else:
        abc_new.append(abc[i])
print (abc_new)