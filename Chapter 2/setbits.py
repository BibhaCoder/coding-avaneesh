def setbits():
  x = int(input())
  p = int(input())
  n = int(input())
  y = int(input())
  y_mask = (~(~0 << n))
  print bin(y)
  y &= y_mask
  x_mask = (~(~0 << n) << (p + 1 - n))
  print bin(x_mask)
  x = x & (~x_mask)
  x = x | y << (p + 1 - n)
  print bin(x)

setbits()

