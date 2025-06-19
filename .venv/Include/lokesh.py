x = int(input("Enter no of test cases"))
while x:
    n = int(input("Enter the number"))

    for i in range(1,11):
        a = i*n
        print(f"{n} X {i} = {a}")
    x -= 1