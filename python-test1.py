#My code starts here
x = int(input())
y = float(input())
# I assigned x and y for weight and height
if x/(y*y) <= 18.5:
 print("Underweight")
else:
 if x/(y*y) >= 18.5 and x/(y*y)< 25 :
  print("Normal")
 else:
  if x/(y*y) >= 25 and x/(y*y)< 30:
   print("Overweight")
  else:
   if x/(y*y) >= 30:
    print("Obesity")
# Else and ifs finishes and BMI Calculator Starts working
# :)