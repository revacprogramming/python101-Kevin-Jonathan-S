# Lists

filename = "dataset/romeo.txt"
han = open('dataset/romeo.txt')

for line in han:
  line = line.rstrip()
  wds = line.split()
  if len(wds) < 3 or wds[0] != 'From':
    continue
  print(wds[2])