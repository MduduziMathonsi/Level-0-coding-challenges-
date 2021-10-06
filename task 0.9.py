def vowels():
 word=input("Enter word: ")
 word = str.lower(word)
 #My logic can be wrong here as it print vowels as long as the finds one eg umuzi U will be printed twice 
 #not sure how to avoid this but working on it.
 vowel= ('a', 'e', 'i', 'o', 'u')
 for letter in word:
  if letter in vowel:
    print(letter)
    
vowels()
    
