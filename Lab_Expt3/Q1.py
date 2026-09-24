"""WAP TO PRINT TWIN PRIME NUMBER 1 TO N"""

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Enter N: "))

print("Twin prime numbers are:")

for i in range(2, n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
