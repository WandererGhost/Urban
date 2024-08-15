import random
the_trap = []
def i_am_ready():
    for i in range (3, 21):
        the_trap.append (i)
    n = random.choice(the_trap)
    return n
n = i_am_ready()

key = []
a = 1

def checking_second_num():
    for i in range (1, n):
        check = a + i
        result = n % check
        if result == 0 and a != i:
            key.append (a)
            key.append (i)

def search_copy(key):
    index = 1
    index_ = 0
    while index <= (len(key)-1):
        if key[index_] != key[index]:
            index = index + 1
            index_ = index_ + 1
        else:
            break
    return index

while a < n:
    checking_second_num()
    a = a + 1
index = search_copy (key)

print (n, '=', *key[0:index])
