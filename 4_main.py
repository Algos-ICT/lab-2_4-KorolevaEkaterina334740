import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def poly_hash(P, p, x=128):
    h = 0
    for i in reversed(range(len(P))):
        h = (h * x + ord(P[i])) % p
    return h % p


def precompute_hashes(T, P, p, x):
    H = [0] * (len(T) - len(P) + 1)
    S = T[len(T) - len(P) : len(T)]
    ind = len(T) - len(P)
    H[ind] = poly_hash(S, p, x)
    y = 1
    for i in range(1, len(P) + 1):
        y = (y * x) % p
    for i in range(len(T) - len(P) - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)]) + p) % p
    return H


if __name__ == '__main__':

    with open("input.txt") as file:
        word = file.readline()[:-1]
        n = int(file.readline())
        sp = []
        for _ in range(n):
            sp.append(list(map(int, file.readline().split())))

    hashes = dict()
    coll = dict()
    k = 1
    l = len(word)
    p, o = 10**9 + 7, 10**9 + 9

    while k <= l:
        hashes[k] = []
        coll[k] = []
        for i in range(l-k+1):
            hashes[k].append(poly_hash(word[i:i+k], p))
            coll[k].append(poly_hash(word[i:i+k], o))
        k += 1

    with open('output.txt', 'w') as file:
        for i in range(n):
            count = sp[i][-1]
            first = sp[i][0]
            second = sp[i][1]
            if hashes[count][first] == hashes[count][second] and coll[count][first] == coll[count][second]:
                file.write(f'YES\n')
            else:
                file.write(f'NO\n')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем строку и записываем хэши каждой ее подстроки 
в словарь с количеством символов этой подстроки. Создаем второй словарь с таким же 
условием, чтобы избежать коллизии. Затем проходим по командам, считываем индекс 
первого элемента первой подстроки и индекс первого элемента второй подстроки, и 
количество элементов этих подстрок. Затем в словарях сравниваем значения индексов 
первых элементов в ключе количества символов. Если значения совпадают в обоих 
словарях, то выводим YES, в противном случае NO
'''

'''
trololo
4
0 0 7
2 4 3
3 5 1
1 3 2
Result:
Yes
Yes
Yes
No
'''