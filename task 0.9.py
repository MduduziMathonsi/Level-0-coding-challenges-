def vowels():
 word="Sunshine"
 word = str.lower(word)
 for letter in 'a', 'e', 'i', 'o', 'u':
  if letter in word:
    print(letter)
vowels()
    
