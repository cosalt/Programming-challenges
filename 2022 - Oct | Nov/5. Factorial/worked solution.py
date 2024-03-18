def findbasenumber(num):
  base_number = factorial = 1

  while factorial < num:
      base_number += 1
      factorial *= base_number

  if factorial == num:
      return base_number
  else:
      return -1
