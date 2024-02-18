def SearchDuplicates(website,password):
  flag = False
  for i,j in enumerate(Secret):
    if Decrypt(Secret[i][2]) == password:
      print(f"Password for {website} also used for {Secret[i][1]")
      flag = True
  if flag is False:
    print("No duplicate passwords found")
