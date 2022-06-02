def get_cs():
  s=int(input("how many string do you need?"))
  l=[]
  for i in range(0,s):
    s=input("enter string")
    l.append(s)
  return l


def cs_to_lot(cs):
  """convert connected string to list of strings"""
  n=[]
  for i in cs:
    n.append((i,i[0]))
  return n


def lot_to_cs(lot):
  """convert list of strings to connected string"""
  for i in lot:
    print(i[0],"=",i[1],end = "  ")
  print()



def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string


if __name__ == '__main__':
    main()