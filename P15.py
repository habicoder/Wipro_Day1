marks=[]
while True:
  x=int(input("Enter value for marks  , To stop give negative value "))
  if x >=0 :
    marks.append(x) 
  else:
    break
print(marks)