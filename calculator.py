#기본 계산기
def add(a, b):
  return a+b

def subtract(a, b):
  return a-b

def multiply(a, b):
    return a*b

def divide_new(a, b):
    return a/b
 
 def getMedian(a, b):
    return (a+b/2)

def getSum_ver2(n):
    sum = 0
  for i in range(1, n+1):
        sum = sum + i


    return sum

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
      return num