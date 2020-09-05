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
    if n < 2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)

print fib(10)
print fib2(9)
