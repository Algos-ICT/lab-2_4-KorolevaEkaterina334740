import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def pref(S):
    l = len(S)
    P = [0] * l
    i, j = 0, 1
    while j < l:
        if S[i] == S[j]:
            P[j] = i + 1
            i += 1
            j += 1
        elif i:
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return P


def kmp(text, sub):
    sub_len, text_len = len(sub), len(text)
    if not text_len or sub_len > text_len:
        return []
    P = pref(sub)
    entries = []
    i = j = 0
    while i < text_len and j < sub_len:
        if text[i] == sub[j]:
            if j == sub_len - 1:
                entries.append(str(i - sub_len + 2))
                j = P[j]
            else:
                j += 1
            i += 1
        elif j:
            j = P[j - 1]
        else:
            i += 1
    return entries


if __name__ == '__main__':
    file = open('input.txt')
    sub = file.readline()[:-1]
    s = file.readline()
    P = kmp(s, sub)
    file = open('output.txt', 'w')
    file.write(f'{len(P)}\n')
    file.write(f'{" ".join(P)}')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем строку и подстроку и запускаем функцию  Кнутта-Морриса-Пратта. С помощью префикс функции мы считаем для 
каждого символа образа количество совпадений, то есть количество символов, на которые мы можем сдвинуть образ вдоль 
строки. Количество этих символов считается как количество префиксов и суффиксов подстроки одинаковой длины и равных по 
значению. То есть префикс-функция для i-ого символа образа возвращает значение, равное максимальной длине совпадающих 
префикса и суффикса подстроки в образе, которая заканчивается i-м символом. На выходе мы получаем массив образа. 
Затем проходим АКМП по строке. Индексы i и j указывают на начальные символы строки и образа. В случае совпадения 
символов мы сдвигаем оба индекса вправо на 1. В случае несовпадения мы обращаем внимание на символ в образе, 
предшествующий не совпавшему. Его значение в массиве образа является индексом того символа, который нужно сдвинуть 
на j-ый индекс. В случае совпадения записываем индекс начала.
'''

'''
aba
abacaba
Result:
2
1 5
'''

'''
Test
testTesttesT
Result:
1
5
'''

'''
aaaaa
baaaaaaa
Result:
3
2 3 4
'''
