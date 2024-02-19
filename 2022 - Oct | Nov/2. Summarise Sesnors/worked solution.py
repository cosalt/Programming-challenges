import random
Array1, Array2 = random.sample(range(0,1000),600),[]
def summarise():
  count, sum = 0,0
  for i in range(600):
    if count == 2:
      sum = round(sum / 3)
      Array2.append(sum)
      count,sum = 0,Array1[i]
    else:
      count += 1
      sum += Array1[i]
  return Array2
summarise()
print(f"Array1: {Array1}\n\n\nArray2: {Array2}")
