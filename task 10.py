def commonletter(firstword,secondword):
  words=set(firstword)&set(secondword)
  for letter in words:
    print(letter,end = ",")
commonletter("fraction","function")
#hi the code compiles on my end Output : f,c,i,o,n,t,

