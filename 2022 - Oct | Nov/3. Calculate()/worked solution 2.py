def Calculator(exp):
  for i,j in enumerate(exp):
    if j in ["+","-","/","*"]:
      expression = j
      value = i
  if expression == "+":
    return (int(exp[:value]) + int(exp[value+1:]))
  elif expression == "-":
    return int(exp[:value]) - int(exp[value+1:])
  elif expression == "/":
    return int(exp[:value]) / int(exp[value+1:])
  elif expression == "*":
    return int(exp[:value]) * int(exp[value+1:])
  else:
    return "error"
