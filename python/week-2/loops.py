# 2.3
def fizzbuzz():
    for x in range(1, 101):
        if(x % 3 == 0 and x % 5 == 0):
            print('fizzbuzz')
        elif(x % 3 == 0):
            print('fizz')
        elif(x % 5 == 0):
            print('buzz')
        else:
            print(x)

# 2.4


def primes(n):
    primes = []
    for x in range(2, n):
        for i in range(2, x):
            if(x % i) == 0:
                break
        else:
            primes.append(x)
    print(primes)

# 2.5


def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2),
        n = n / 2
    while n % 3 == 0:
        factors.append(3),
        n = n / 3
    while n % 5 == 0:
        factors.append(5),
        n = n / 5
    print(factors)

# 2.6


def my_sort(list):
    newList = []
    for x in range(len(list)-1, -1, -1):
        newList.append(list[x])
    print(newList)
