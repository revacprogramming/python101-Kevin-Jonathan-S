def inputt():
    a=int(input(""))
    return a


def add(a, b):
    return  a+b


def main():
    a = inputt()
    b = inputt()
    c = add(a, b)
    print("Enter 1st Number?",a)
    print("Enter 2nd Number?",b)
    print("Sum of", a ,"and ",b ,"is", c)
    
    
main()