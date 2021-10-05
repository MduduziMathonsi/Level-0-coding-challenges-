def commonletter():
  firstword = input("Enter a first word: ")
  secondword = input("Enter a second word: ")
  twowords=list(set(firstword)&set(secondword))
  print("The common letters are:")
  for i in twowords:
    print(i)
commonletter()


