def gcd(m,n):
  mrcf = 1
  m = int(input("Enter first number: "))
  n = int(input("Enter second number:"))
  for i in range(1,min(m,n)+1):
    if(m%i) == 0 and (n%i) == 0:
      mrcf = i
  print(mrcf)
