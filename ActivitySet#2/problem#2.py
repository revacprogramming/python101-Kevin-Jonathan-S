def input_two_numbers():
  a=int(input(""))
  b=int(input(""))
  return a,b
  
  
  
def add(a, b):
    #pass  # ...
  c=a+b
  return c
  


def output(a, b, summ):
    #pass  # ...
  print("input?",a,b)
  print(a,"+",b,"is",summ)


def main():
    a,b=input_two_numbers()
    summ = add(a, b)

    output(a, b, summ)


if __name__ == '__main__':
    main()