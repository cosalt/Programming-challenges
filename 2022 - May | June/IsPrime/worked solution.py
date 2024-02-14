def IsPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


def count_prime_numbers():
  count = 0
  while True:
    num = int(input("Interger: "))
    if num < 0:
      break
    if IsPrime(num):
      count += 1
  print(f"Count of prime numbers is: {count}")
