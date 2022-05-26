def get_cs():
  s=int(input("how many string do you need?"))
  l=[]
  for i in range(0,s):
    s=input("enter string")
    l.append(s)
  return l


def cs_to_lot(l):
  n=[]
  for i in l:
    n.append((i,i[0]))

  return n
    
    


def main():
    l = get_cs()

    lot = cs_to_lot(l)
    print(lot)


if __name__ == '__main__':
    main()