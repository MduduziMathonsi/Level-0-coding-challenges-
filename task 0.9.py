def vowels():
 word=input("Enter word: ")
 word = str.lower(word)
 for letter in word:
  if letter in "aAeEiIoOuU":
    print(letter)
    
vowels()
    