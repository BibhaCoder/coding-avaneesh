

lines = []
while True:
  line = input()
  if line == "":
    break
  lines.append(line)

i = 0
longest_line = ""
longest_lenght = 0
for element in lines:
  if len(lines[i]) > longest_lenght:
    longest_lenght = len(lines[i])
    longest_line = lines[i]
  i += 1

print  ("longest line is: " + longest_line)
