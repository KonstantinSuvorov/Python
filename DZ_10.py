# Задача 1. «Пересечение множеств»
# Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список
# и выведите их в порядке возрастания.
# Примечание: И даже эту задачу на Питоне можно решить в одну строчку.
# 
# Sample Input 1:
# 1 3 2 
# 4 3 2
# Sample Output 1:
# 2 3

# Sample Input 2:
# 1 2 6 4 5 7 
# 10 2 3 4 8
# Sample Output 2:
# 2 4

# A = sorted(list(set([int(s) for s in input().split()]) & set([int(s) for s in input().split()])))
# for elem in A:
#     print(elem, end=' ')



# Задача 2
# Во входной строке записана последовательность чисел через пробел. 
# Для каждого числа выведите слово YES (в отдельной строке), 
# если это число ранее встречалось в последовательности или N0 , если не встречалось.
# 
# Sample Input 1:
# 1 2 3 2 3 4
# Sample Output 1:
# N0
# N0
# N0
# YES
# YES
# N0
# Sample Input 2:
# 1111111111

# L = [int(i) for i in input().split()]
# S = set()
# for i in L:
#     if i in S:
#         print('YES')
#     else:
#         print('NO')
#     S.add(i)



# Задача 3 
# Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

# Sample Input:
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.

# Sample Output:
# 19

n = int(input())
A = set()
for i in range(n):
    S = input().split()
    for elem in S:
        A.add(elem)
print(len(A))
