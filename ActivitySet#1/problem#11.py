# Tuples

filename = "dataset/mbox-short.txt"
han = open('dataset/romeo.txt')

for line in han:
  line = line.rstrip()
  wds = line.split()
  for w in wds:
    di[w] = di.get(w,0) + 1

tmp = list()
for k,v i di.items() :
  newt = (v,k)
  tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5]:
  print(k,v)