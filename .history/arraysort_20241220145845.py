newarray = [7,4,6,7,5,3,2,1,0]


def sorting(array):

  i = 0
  list_a = []
  for value in newarray:
    if value == i and value not in list_a:
      list_a.append(value)
      newarray.remove(value)
    i+=1
  
  print(list_a)

print(sorting(newarray))