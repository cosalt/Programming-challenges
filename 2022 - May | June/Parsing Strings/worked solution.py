def Parse(InString):
  temp = 0
  z = 0
  nl = "\n"
  x = InString.split(",")
  for i, j in enumerate(x):
    temp = temp + int(j)
    z = z + i
  z = z + 1
  print(f"Total: {temp}{nl}Average: {round(temp / len(x))}")
