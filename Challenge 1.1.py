def fact_num(number):
  if number == 0:
    return 1
  else:
    return number * fact_num(number - 1)


number = int(input("enter a value:"))
res = fact_num(number)
print("factorial of{}is{}".format(number, res))
