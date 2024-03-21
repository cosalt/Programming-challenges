import string
import random
final = ""
asc = list((string.ascii_lowercase)+(string.ascii_uppercase)+(string.digits))
def RandomChar():
  global final
  for i in range(4):
    for j in range(4):
      num = random.randint(0,61)
      temp = asc[num]
      final = final+temp
    final=final+"-"
  return final[0:-1]
