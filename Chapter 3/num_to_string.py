num = int(input())
while num != 0:
  r = num % 10
  num = num // 10
  string_num = ""
  string_num = ("" + str(r))
  print string_num
