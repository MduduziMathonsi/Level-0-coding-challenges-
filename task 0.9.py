def vowels(word):
 word = str.lower(word)
 for letter in "aeiou":
  if letter in word:
    print(letter,end = ",")
vowels("Sunshine")  
    
