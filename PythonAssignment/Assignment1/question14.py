#Write a Python script to check if a given key already exists in a dictionary.
dict = {"first":"python","second":"is","third":"a","fourth":"programming","fifth":"language"}
if "first" in dict:
    print ("It is present in dictionary.")
else: 
    print ("It is not present in dictionary.") 
if "four" in dict.items():
    print ("It is present in dictionary.")
else:
    print ("It is not present in dictionary.")