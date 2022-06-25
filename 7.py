import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def poly_hash(P, p, x=128):
    h = 0
    for i in reversed(range(len(P))):
        h = (h * x + ord(P[i])) % p
    return h % p


if __name__ == '__main__':
    p, o = 10 ** 9 + 7, 10 ** 9 + 9
    with open('input.txt') as file:
        text = list(map(str, file.read().split('\n')))
        file = open('output.txt', 'w')
        for i in range(len(text)):
            word1, word2 = text[i].split(' ')
            hashes, coll = dict(), dict()
            k = 1
            w1, w2 = len(word1), len(word2)

            while k <= w1:
                hashes[k] = []
                coll[k] = []
                for i in range(w1 - k + 1):
                    hashes[k].append(poly_hash(word1[i:i + k], p))
                    coll[k].append(poly_hash(word1[i:i + k], o))
                k += 1

            k = 1
            maxim = 0
            result, indexes = [], [0, 0]
            while k <= w1:
                for i in range(w2 - k + 1):
                    x = poly_hash(word2[i:i+k], p)
                    y = poly_hash(word2[i:i+k], o)
                    if x in hashes[k] and y in coll[k]:
                        if k > maxim:
                            maxim = k
                            indexes[1], indexes[0] = i, hashes[k].index(x)
                            k += 1
                            break
                k += 1

            result = list(map(str, (*indexes, maxim)))
            file.write(f'{" ".join(result)}\n')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем строки, первое слово разделяем на подстроки и 
хэшируем каждую. Второе слово начинаем разделять на подстроки начиная с 1, 
хэшируем и проверяем, есть ли такой хэш в словаре с количеством символов. Если 
такой хэш есть, то переменную максим обновляем и увеличиваем количество символов 
в подстроке второго слова. На выходе пишем максимальную длину совпавшей 
подстроки.
'''

'''
cool toolbox
aaa bb
aabaa babbaab
Result:
1 1 3
0 1 0
0 4 3
'''