n=int(input("Enter number to be checked:"))
num=n
sum=0
while num>0:
  d=num%10
  sum+=d**3
  num//=10
if sum==n:
  print("Armstrong number")
else:
  print('Not Armstrong number')
