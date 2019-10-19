n=int(input("Enter a number:"))
def isPrime(x):
  ctr=0
  for i in range(1,x):
     if x%i==0:
      ctr+=1
   if ctr==1:
    return True
   else:
    return False
for i in range(2,n+1):
  if(isPrime(i)):
    if n%i==0:
      print(i)
      
