def maximum():
 num1 = input("Enter the first number :")
 num2 = input("Enter the second number :")
 num3 = input("Enter the third number :")
 if num1 > num2 and num1 > num3 :
   print(num1)
 elif num2 > num1 and num2 > num3 :
     print(num2)
 elif num3 > num1 and num3 > num2 :
     print(num3)
 else:
     #if user entered two or more same numbers and it happens to be the highest numbers
     print("Two or more number/s are equal and are maximum numbers") 

maximum()