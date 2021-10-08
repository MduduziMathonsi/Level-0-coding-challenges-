def vowels(word):
 word = str.lower(word)
 print(*{letter for letter in word if letter in 'aeiou'},sep=(','))
vowels("Sunshine") 


