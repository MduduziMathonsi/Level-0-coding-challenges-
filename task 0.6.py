def maximum(num1,num2,num3):
 if num1 > num2 and num1 > num3 :
   print("Highest Number:",num1)
 elif num2 > num1 and num2 > num3 :
     print("Highest Number:",num2)
 elif num3 > num1 and num3 > num2 :
     print("Highest Number:",num3)
 else:
     #if two or more same numbers happens to be the highest numbers
     print("Two or more number/s are equal and are maximum numbers") 

maximum(10,30,15)