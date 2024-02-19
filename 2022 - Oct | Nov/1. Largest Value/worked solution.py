def largest_number(array):
  largest = 0
  for i in array:
    if i > largest:
      largest = i
  return largest
