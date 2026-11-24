from random import randint

# 3. Greet
def greet():
    for _ in range(3):
        print("Hello!")

# 4. Greet N
def greetN(n):
    for _ in range(n):
        print("Hello!")

# 5. Greet Name
def greetName(name, n):
    for _ in range(n):
        print(f"Hello, {name}!")

# 6. Random Letter
def random_letter():
    return chr(randint(65, 90))

# 7. Cube
def cube(number):
    return number ** 3


###
print("3")
greet()

print("4")
greetN(2)

print("5")
greetName("Alice", 2)

print("6")
print("Random letter:", random_letter())

print("7")
print("Cube of 3:", cube(3))