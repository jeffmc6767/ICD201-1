inches = int(input("Enter a dimension in inches "))
pounds = int(input("Enter a dimension in pounds "))
gallons = int(input("Enter a dimension in gallons "))


def itom(inches):
    return inches * 2.54
mm = itom(inches)

def ptok(pounds):
    return pounds * 0.453592
kg = ptok(pounds)

def gtol(gallons):
    return gallons * 3.78541
liters = gtol(gallons)

print(mm)
print(kg)
print(liters)

