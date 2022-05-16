# Files

filename = "dataset/mbox-short.txt"

fh = open(filename)
for lx in fh:
  ly=lx.rstrip()
  print(ly.upper())