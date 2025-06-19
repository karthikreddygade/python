def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sub(a,b):
    return a-b
operations ={
    "+": add,
    "*": mul,
    "/": div,
    "-":sub,
}
def calculator():
    a= float(input("Enter the 1 numbers"))
    loop = True
    while loop == True:
        for symbols in operations:
            print(symbols)
        operators = input("Enter the operation symbol")
        b= float(input("Enter the 2 numbers"))
        ans = operations[operators](a,b)
        print(f"{a} {operators} {b} = {ans}")
        choice = input("Enter y to continue with previous answer or press n for new calculation").lower()
        #num = float(input("Enter the number"))
        if choice == "y":
            a = ans
        elif choice == "stop":
            loop = False
            break
        else:
            loop = False
            print("\n"*10)
            calculator()
calculator()

#ask = input("Do you want to countinue?")