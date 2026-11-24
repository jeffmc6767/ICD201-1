import random
import math

num1x, num1y = random.randint(-100,100), random.randint(-100,100)

num2x, num2y = random.randint(-100,100), random.randint(-100,100)


def VerticalDistance(y1, y2):
    return abs(y2 - y1)


def HorizontalDistance(x1, x2):
    return abs(x2 - x1)


def CalculateDistance(x1, y1, x2, y2):
    dx = HorizontalDistance(x1, x2)
    dy = VerticalDistance(y1, y2)
    return math.hypot(dx, dy)  


distance = CalculateDistance(num1x, num1y, num2x, num2y)

print(distance)
