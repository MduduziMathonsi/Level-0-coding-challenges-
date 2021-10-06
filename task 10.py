def commonletter():
  firstword = "fraction"
  secondword = "function"
  letterscheck=list(set(firstword)&set(secondword))
  for letter in letterscheck:
    print(letter)
commonletter()


