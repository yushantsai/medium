def fib(n):
  result=[]
  try:
    if n > 0:
      for i in range(n):
        result.append(i if i < 2 else result[i-2] + result[i-1])
  except:
    print "Invalid number"
  finally:
    return result

def fib2(n):
  return n if n < 2 else fib2(n-1) + fib2(n-2)

def fib3(n):
  return int(((((1 + 5 ** 0.5) / 2) ** n) - (((1 - 5 ** 0.5) / 2) ** n)) / (5 ** 0.5))
