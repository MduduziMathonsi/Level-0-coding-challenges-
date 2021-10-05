def commonletter():
  firstword = input("Enter a first word: ")
  secondword = input("Enter a second word: ")
  wordscheck=list(set(firstword)&set(secondword))
  for i in wordscheck:
    print(i)
commonletter()


