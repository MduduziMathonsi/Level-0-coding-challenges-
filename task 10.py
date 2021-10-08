def commonletter(firstword,secondword):
  words=set(firstword)&set(secondword)
  print(*{letter for letter in words},sep=(','))
commonletter("fraction","function")


