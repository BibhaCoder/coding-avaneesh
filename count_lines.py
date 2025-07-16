print("Line count; press enter to exit")

lines = []
while True:
  line = input()
  if line == "":
    break
  lines.append(line)

print ("You printed this much lines:")
print (str(len(lines)))
