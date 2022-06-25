import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input.txt') as f:
    s = f.readline()

l = len(s)
flag = False
for k in range(l-1, 0, -1):
    for i in range(l-k):
        if s[i] == s[i+k]:
            print(k)
            flag = True
            break
    if flag:
      break
if not flag:
    print(0)


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())


'''
Чтобы найти две подстроки максимальной длины, состоящей из одних и тех же символов, достаточно найти самую длинную 
подстроку, которая начинается и оканчивается одним и тем же символом. Тогда максимальной длинной таких подстрок будет 
длина найденной подстроки без одного символа. В программе мы идем счетчиком k от l-1 до 1 – максимизируем длину 
возможных подстрок. Далее счетчиком i сравниваем i-й и (i+k)-й символы. Если они одинаковые, то выводим k. Если в 
течение циклов строки с двумя одинаковыми символами на концах не нашлось, то выводим 0.
'''

'''
abcde
Result:
0
'''

'''
abcdea
Result:
5
'''