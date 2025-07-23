def setbits():
  x = int(input())
  p = int(input())
  n = int(input())
  y = int(input())
  y_mask = (~(~0 << n))
  print bin(y)
  print bin(y_mask)
  y &= y_mask
  print bin(y)
  x_mask = ~(~0 << n) << (p + 1 - n)

setbits()
