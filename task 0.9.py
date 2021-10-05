def vowels():
 word=input("Enter word: ")
 word = str.lower(word)
 vowel= ('a', 'e', 'i', 'o', 'u')
 for letter in word:
  if letter in vowel:
    print(letter)
    
vowels()
    
