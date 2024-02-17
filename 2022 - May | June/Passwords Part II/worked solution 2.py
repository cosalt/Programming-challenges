def Exists(string, char):
  flag = False
  for i in string:
    if i == char:
      flag = True
  if flag == True:
    return True
  else:
    return False
