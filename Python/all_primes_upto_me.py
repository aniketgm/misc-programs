# Print all prime numbers upto given number

def isPrime(num):
    halfOfNum = int(num/2)
    divisors = [i for i in range(1, halfOfNum+1) if (num % i == 0)]
    if len(divisors) == 1:
        return True
    return False

def allPrimesUptoMe(num):
    allPrimes = []
    for a in range(2,num):
        if isPrime(a):
            allPrimes.append(a)
    return allPrimes

if __name__ == '__main__':
    print()
    print(" ## Given a number to the program, it prints all primes upto that number.")
    print()
    print(allPrimesUptoMe(int(input("Enter number: "))))

