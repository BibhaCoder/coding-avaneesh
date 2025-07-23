def setbits():
  x = int(input())
  p = int(input())
  n = int(input())
  y = int(input())
  mask = (~(~0 << n))
  print bin(y)
  print bin(mask)
  y &= mask
  print bin(y)
  y = (x >> (p + 1 - n) & mask)
setbits()
