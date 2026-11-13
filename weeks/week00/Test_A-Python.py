# Write classify(n) returning "fizz", "buzz", "fizzbuzz" or the number as a string, then print results for 1 to 30.

def classify(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)


for i in range(1, 31):
    print(classify(i))
