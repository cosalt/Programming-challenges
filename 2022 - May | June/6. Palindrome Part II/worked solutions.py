def removewhitespaces(instring):
  outstring = ""
  for char in instring:
    if char != " ":
      outstring += char
  return outstring
