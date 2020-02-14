def challenge10(s):
    return ' '.join(list(sorted(set(s.split()))))

def challenge10_2(s):
    words = set(w for w in s.split())
    return ' '.join(list(sorted(words)))

print(challenge10_2("hello world and practice makes perfect and hello world again"))

def challenge11(s):
    valid = [n for n in s.split(',') if int(n, 2) % 5 == 0]
    print(','.join(valid))

challenge11("0100,0011,1010,1001")

def challenge12():
    print(','.join(str(i) for i in range(1000, 3001, 2)))

challenge12()

def challenge13(s):
    letters = digits = 0
    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
    print(f'LETTERS {letters}')
    print(f'DIGITS {digits}')

challenge13("hello world! 123")