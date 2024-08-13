import random

the_trap = []
key = []
def i_am_ready():
    for i in range (3, 21):
        the_trap.append (i)
    n = random.choice(the_trap)
    print ('Выпало ', n)
    return n
n = i_am_ready()
a = 1
def checking_second_num():
        for i in range (1, n):
            check = a + i
            result = n % check
            if result == 0 and a != i:
                key.append (a)
                key.append (i)

while a < n and a not in key:
    checking_second_num()
    a = a + 1

print (*key)
print ('И да, пока я ломала голову над задачей меня уже мнооооооооооого раз раздавили шипы с потолка XD')