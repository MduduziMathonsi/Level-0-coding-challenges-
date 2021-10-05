def commonletter():
  firstword = input("Enter a first word: ")
  secondword = input("Enter a second word: ")
  wordscheck=list(set(firstword)&set(secondword))
  for letter in wordscheck:
    print(letter)
commonletter()


