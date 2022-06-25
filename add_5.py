import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input.txt') as f:
    t = f.readline()[:-1]
    p = f.readline()[:-1]

res = []
for i in range(len(t) - len(p) + 1):
    if t[i] == p[0]:
        part = t[i:i+len(p)]
        if part == p:
            res.append(str(i))

print(' '.join(res))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Для решения данной задачи в рамках ограничений хватило обычного 
наивного поиска подстроки.
'''

'''
ababbababa
aba
Result:
0 5 7
'''