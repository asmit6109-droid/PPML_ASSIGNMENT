def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end - 1):
    if isPrime(i) and isPrime(i + 2):
        print(i, i + 2)