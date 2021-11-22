def gcd(a,b):
  list1=[]
  list2=[]
  cf_list=[]
  for i1 in range(2,a+1):
    if a%i1==0:
      list1.append(i1)
  for i2 in range(2,b+1):
    if b%i2==0:
      list2.append(i2)
  for e1 in list1:
    for e2 in list2: 
      if e1==e2:
        cf_list.append(e1)
  return max(cf_list)
num1=int(input("enter the 1st num:")) 
num2=int(input("enter the 2nd num:"))  
print("the greatest common divisor is ",gcd(num1,num2))
      
    
  
  







