#Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary: dic1= {1:10, 2:20} dic2= {3:30, 4:40} dic3= {5:50,6:60}
#Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
int1 = {"first":"python","second":"is"}
int2 = {"third":"a","fourth":"programming","fifth":"language"}
int3 = {}
for i in (int1,int2):
    int3.update(i)
print(int3)