import random

the_trap = []
key = []


def i_am_ready():
    for i in range(3, 21):
        the_trap.append(i)
    n = random.choice(the_trap)
    return n


n = i_am_ready()
a = 1


def checking_second_num():
    for i in range(1, n):
        check = a + i
        result = n % check
        if result == 0 and a != i and i not in key[0:n:1]:
            key.append(a)
            key.append(i)


while a < n:
    checking_second_num()
    a = a + 1

n = str(n)
key = list(map(str, key))
key = ' '.join(key)
key = key.replace(' ', '')
print (n,'-', key)
