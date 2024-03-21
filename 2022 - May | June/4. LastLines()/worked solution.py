def LastLines(file_name):
  try:
    with open(file_name, "r") as file:
      linex, liney, linez = '','',''
      line = file.readline()
      while line:
        linex, liney, linez = liney, linez, line
        line = file.readline()
      print(linex, end="")
      print(liney, end='')
      print(linez, end='')
  except FileNotFoundError:
    print('File NOT found!!!!')
