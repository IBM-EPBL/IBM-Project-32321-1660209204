import random 
print(random.random())
humidity=int(input("Enter humidity value:"))
temp=int(input("Enter temperature value:"))
tem=temp*random.random()
if humidity>90:
   print("Hazard")
else:
   print("Humidity is normal")
if temp>80:
   k=0
   while k<=10:
       print("********High temperature*********")
       k=k+1
elif temp<80:
   print("Temperature is normal")
elif temp==80:
   print("Temperature is at max level")