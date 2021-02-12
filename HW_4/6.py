from itertools import count, cycle

for el in count(3):
    print(el)
    if el == 10:
        break

my_list = ["abc", 123, True, 127.54]

i = 0

for el in cycle(my_list):
    print(el)
    i += 1
    if i == 20:
        break
