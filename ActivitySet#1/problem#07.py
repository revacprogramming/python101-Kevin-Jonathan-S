# Strings

text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
piece = text[ipos+2:]
value = float(piece)
print(value)