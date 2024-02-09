def isPalindrome(word):
  temp = word.lower()
  x = temp.split()
  temp = temp[::-1]
  reversed = temp.split()
  if x == reversed:
    print("True")
  else:
    print("False")
