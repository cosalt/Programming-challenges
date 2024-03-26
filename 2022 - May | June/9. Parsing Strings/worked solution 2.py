def Parse(InString):
  numbers = [int(num) for num in InString.split(',')]
  return (f"Total: {sum(numbers)}\nAverage: {sum(numbers)/(len(numbers)+1)}")
