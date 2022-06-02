def get_cs():
  s=int(input("how many string do you need?"))
  l=[]
  for i in range(0,s):
    s=input("enter string")
    l.append(s)
  return l


def cs_to_dict(cs):
  """convert connect string to a dictionary"""
  n={}
  for i in cs:
    n[i]=i[0]
  return n


def dict_to_cs(d):
  """convert a dictionary to connect string"""
  s=d.items()
  for key,value in s:
      print(key,"=",value)
  


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)


if __name__ == '__main__':
    main()