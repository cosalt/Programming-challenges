total, index, average, userid = 0, 4, (GetAverage(userid)), input("input userid: ")
while index < 7:
  last = SameMonth[index]
  if average > last:
    total = total + average
  else:
    total = total + last
