import random

"""def sorting(array):
    i = 1
    list_a = []
    while i in array:
        if i not in list_a:
            list_a.append(i)
            array.remove(i)
        i += 1
    return list_a

newarray = [7, 4, 6, 7, 5, 3, 2, 1]
print(sorting(newarray))
"""

def newsorting(array):
    return sorted(array)

def sortgame():
  numofvalues = int(input('how many values are you going to sort?\n'))

  randomarray = []
  for i in range(numofvalues + 1):
      randomarray.append(random.randint(0,9))

  return sorted(randomarray)

print(sortgame())