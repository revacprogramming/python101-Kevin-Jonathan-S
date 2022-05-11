# Functions


def computepay(Working, PPW):
    if Working > 40:
      bonusrate = PPW * 1.5
      bonuspay = (Working - 40) * bonusrate
      xp = ((Working - (Working - 40)) * PPW) + bonuspay
    else:
      xp = Working * PPW
    return xp

hrs = input("Enter hours: ")
rate = input("Enter rate per hour: ")
try:
  Working = float(hrs)
  PPW = float(rate)
except:
  print("Enter in numeric form :(")
  quit()

pay = computepay(Working, PPW)

print("Your pay is: $", pay)