import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def z_arr(s):

    Z = [0] * len(s)
    rt, lt = 0, 0

    for k in range(1, len(s)):
        if k > rt:
            n = 0
            while n + k < len(s) and s[n] == s[n+k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k+n-1
        else:
            p = k - lt
            right_part_len = rt - k + 1
            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k
                lt = k
                rt = i - 1
    return Z


if __name__ == '__main__':
    with open('input.txt') as file:
        word = file.readline()

    result = list(map(str, z_arr(word)))

    with open('output.txt', 'w') as file:
        file.write(f'{" ".join(result[1:-1])}')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Суть Z-функции состоит в нахождении количества 
одинаковых символов всех суффиксов строки и самой строки. То есть мы берем 
каждый суффикс, начиная с самого большого, и подставляем его в начало строки, 
сравнивая каждый символ
'''

'''
aaaAAA
Result:
2 1 0 0 0
'''

'''
abacaba
Result:
0 1 0 3 0 1
'''