def hoursminutes():
 number = 61
 convnumber = int(number)
 h= int(convnumber / 60)
 m = int(convnumber-(1*60))
 if h<=1 and m<=1 :
  print(h,"hour :",m,"minute")
 elif h>=1 and m>=1 :
  print(h,"hours :",m,"minutes")
 else:
   print("Abort Mission Impossible :-)")
hoursminutes()




