def searchinfile(filename, searchvalue):
  with open(filename, "r") as file:
    for line in file:
      field1 = line[0:2]
      field2 = line[2:7]
      field3 = line[7:11]
      if field2.strip() == searchvalue:
        return field1, field3
  return None, None

filename = "words.txt"
searchvalue = input("Search Value: ")

field1_result, field3_result = searchinfile(filename, searchvalue)
if field1_result is not None and field3_result is not None:
  print(f"Field 1: {field1_result}\nField 3: {field3_result}")
else:
  print(f"Value not found: {searchvalue}")
