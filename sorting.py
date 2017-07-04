
# prints stuff in order
print("sorting: ")
def mySort(theList):
  for number in range(len(theList)-1,0,-1):
    for item in range(number):
      if theList[item]>theList[item+1]:
        theList[item],theList[item+1]=theList[item+1],theList[item]
  print(theList)


list1 = [67,45,2,13,1,998]
mySort(list1)

list2=[89,23,33,45,10,12,45,45,45]
mySort(list2)

