def seven(startnum, endnum):
  while True:
    startnum = startnum + 1
    if startnum <= endnum:
      if startnum%10 == 7:
        print(startnum)
        continue
      continue
    else:
      break
