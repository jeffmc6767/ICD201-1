import random

amount = int(input("What is your principal amount?"))
time = int(input("What time period"))


def rate():
  return random.uniform(3.25, 5.75)


def sinterests(principal, years, rate):
  return principal * (rate / 100) * years


def cinterests(principal, years):
  rate = 0.05
  n = 2
  total_amount = principal * (1 + rate / n) ** (n * years)
  return total_amount - principal


amount = 1000.0
time = 3

vrate = rate()
sinterest = sinterests(amount, time, vrate)
cinterest = cinterests(amount, time)

print(vrate)
print(sinterest)
print(cinterest)
