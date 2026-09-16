# nested if else condition

weeks =["sanday","monday","tuesday","wednesday","thrusday","friday","saturday","sunday"] #list is mutable 

day_of_week = str(input("enter day :")).lower()
print (":" ,day_of_week)

if day_of_week not in weeks :
   print("enter valid entry")
else:
   if day_of_week=="saturday" or day_of_week=="sunday" :
      print("Today is weekend")
           
   else :
      print("Today is working day")




