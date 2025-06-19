#To print maximum number of given list
n = list(map(int , input("Enter the numbers").split()))
maximum = 0
for i in n:
    if maximum < i:
        maximum = i
print(maximum)