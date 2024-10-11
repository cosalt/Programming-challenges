# used to call multiple functions based on a condition

def a():
  print("a")

def b():
  print("b")

def c():
  print("c")

def default():
  print("Default")


# can be input
option = "b"
# traditional, if statement

if option == 'a':
  a()
elif option == 'b':
  b()
elif option == 'c':
  c()
else:
  default()

# match case statement
match option:
  case 'a':
    a()
  case 'b':
    b()
  case 'c':
    c()
  case _:
    default()

# more efficient way, use dictionary and .get() method
funcs = {'a': a, 'b': b, 'c': c}
f = funcs.get(option, default)
# use .get(), grab the option, if can't execute default
f()
