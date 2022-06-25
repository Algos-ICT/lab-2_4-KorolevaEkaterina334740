import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def areEqual(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def FindPattern(t, p):
    result = []
    for i in range(len(t) - len(p) + 1):
        if areEqual(t[i:i + len(p)], p):
            result.append(str(i + 1))
    return result


if __name__ == '__main__':
    file = open('input.txt')
    p = file.readline()[:-1]
    t = file.readline()
    file = open('output.txt', 'w')
    result = FindPattern(t, p)
    file.write(f'{len(result)}\n')
    file.write(' '.join(result))


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем подстроку p и ищем все ее вхождения в строку t наивным алгоритмом. Функция FindPattern проходится по всем 
подстрокам длины p основной строки, для каждой из них запускает фунцию areEqual, которая сравнивает  каждый символ двух 
строк. Если все символы совпадает, возвращает True и записывает индекс начала подстроки в основной строке.
'''

'''
aba
abaCaba
Result:
2
1 5
'''
