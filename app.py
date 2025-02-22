<<<<<<< HEAD
def is_prime(n):
def is_odd(n):
ief is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a odd number.")
else:
    print(f"{num} is a prime number.")
>>>>>>> 267a7823f4dcf10c58565817fbcac4296f561858
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

