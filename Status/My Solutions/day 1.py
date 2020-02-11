#challenge 1

def challenge1():
    return ','.join([i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0])

# more readable
def challenge1_2():
    l = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            l.append(str(i))
    return ', '.join(l)

#print(challenge1_2())

#
# challenge 2
def fact_recurse(n):
    if n == 0:
        return 1
    return n * fact_recurse(n - 1)

def fact_iter(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# challenge 3

def challenge3(n):
    if n == 0:
        return {}
    return {i : i * i for i in range(1, n + 1)}

#print(challenge3(20))