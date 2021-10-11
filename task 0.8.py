def hoursminutes(number):
 convnumber = int(number)
 h= int(convnumber / 60)
 m = int(convnumber-(1*60))
 if h<=0 and m<=0:
  print(number,"minutes")
 elif h<=1 and m<=1 :
  print(h,"hour :",m,"minute")
 elif h>=1 and m>=1 :
  print(h,"hours :",m,"minutes")
 else:
   print("Abort Mission Impossible :-)")
hoursminutes(59)




